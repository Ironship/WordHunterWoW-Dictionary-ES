#!/usr/bin/env python3
"""Split Spanish words into per-agent audit batches.

    python Tools/prepare_audit.py --limit 6000 --batch-size 150

Spanish ships as two dictionaries, esES and esMX, because Blizzard translates
the two separately. They share 46,179 words and differ on about 22,000, so the
order words are audited in decides how much of that work counts twice.

Shared words come first, commonest first. A word audited once is merged into
both dictionaries, so an hour spent on the shared vocabulary moves both packs;
an hour spent on an esMX-only word moves one. The words either dictionary has
on its own are still audited -- later, and by the same standard.
"""
import argparse, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCALES = ("esES", "esMX")
WORKDIR = ROOT / "Data/cache/audit_work"
CONTEXT_CHARS = 300


def load(path):
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=6000)
    ap.add_argument("--batch-size", type=int, default=150)
    ap.add_argument("--offset", type=int, default=0)
    args = ap.parse_args()

    # Anything already audited, in either dictionary or in a wave still on disk.
    done = set()
    for loc in LOCALES:
        for r in load(ROOT / f"Data/Curated{loc.upper()}.jsonl"):
            if r.get("key"):
                done.add(r["key"])
    outdir = WORKDIR / "out"
    if outdir.exists():
        for path in sorted(outdir.glob("*.jsonl")):
            done.update(r["key"] for r in load(path) if r.get("key"))

    # One row per word. A shared word keeps the esES translation as the starting
    # point and is marked, so the prompt can warn that the two dictionaries may
    # want different wording for it.
    rows, locales_of = {}, {}
    for loc in LOCALES:
        for r in load(ROOT / f"Data/cache/translations_{loc}_en.jsonl"):
            key = r.get("key")
            if not key or key in done:
                continue
            locales_of.setdefault(key, set()).add(loc)
            if key not in rows or loc == "esES":
                rows[key] = r

    context, counts = {}, {}
    for loc in LOCALES:
        for r in load(ROOT / f"Data/cache/wordlist_{loc}.jsonl"):
            key = r.get("key")
            if not key:
                continue
            counts[key] = max(counts.get(key, 0), r.get("count", 0))
            if key not in context and r.get("context"):
                context[key] = r["context"]

    ordered = sorted(rows,
                     key=lambda k: (-len(locales_of[k]), -counts.get(k, 0), k))
    ordered = ordered[args.offset:args.offset + args.limit]

    indir = WORKDIR / "in"
    indir.mkdir(parents=True, exist_ok=True)
    outdir.mkdir(parents=True, exist_ok=True)
    for old in indir.glob("batch_*.jsonl"):
        old.unlink()

    batches = 0
    shared = 0
    for i in range(0, len(ordered), args.batch_size):
        chunk = ordered[i:i + args.batch_size]
        slim = []
        for key in chunk:
            r = rows[key]
            both = len(locales_of[key]) == 2
            shared += 1 if both else 0
            slim.append({"key": key, "word": r["word"],
                         "current": r.get("translation", ""),
                         "count": counts.get(key, 0),
                         "locales": "".join(sorted(locales_of[key])) if not both else "both",
                         "context": " ".join(context.get(key, "").split())[:CONTEXT_CHARS]})
        path = indir / f"batch_{batches:02d}.jsonl"
        path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in slim) + "\n",
                        encoding="utf-8")
        batches += 1

    print(f"selected={len(ordered)} shared={shared} batches={batches} already_done={len(done)}")


if __name__ == "__main__":
    main()
