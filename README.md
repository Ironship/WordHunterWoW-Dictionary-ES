# QuestWordHunter — Spanish Dictionary

Optional Spanish→English vocabulary packs for [QuestWordHunter](https://github.com/Ironship/WordHunterWoW), built from actual World of Warcraft quest text.

The addon contains separate dictionaries for European Spanish (`esES`, 58,211 entries) and Latin American Spanish (`esMX`, 56,081 entries). QuestWordHunter automatically uses the one matching the selected target language.

## Quality

These packs are raw machine translation. Unlike the [German dictionary](https://github.com/Ironship/WordHunterWoW-Dictionary-DE), where a large share of entries has been reviewed by hand against the quest sentence it appears in, nothing here has been through that review. Expect the usual machine-translation failures: false friends, the wrong sense of an ambiguous word, official WoW names translated literally. Treat a gloss as a starting point, and edit it when it is wrong — your edit wins over the pack.

The exception is a short hand-written list in `Data/CuratedESES.jsonl` and `Data/CuratedESMX.jsonl` covering the one-letter words `a`, `y`, `o`, `e` and `u`. Those are among the most frequent words in the language and a machine translator has no context to get them right: asked in isolation, Google renders `o` as "either". These are glossed by hand and override the machine output.

## What you need

- Retail 12.1 (`Interface 120100`)
- [QuestWordHunter](https://github.com/Ironship/WordHunterWoW) **1.6.0 or newer**
- Target language set to **Spanish (EU)** or **Spanish (MX)**

1.6.0 is a hard requirement, not a suggestion: earlier versions lowercase only ASCII, so every word starting with an accented capital — `Él`, `Ébano`, `Últimamente` — missed the dictionary and opened a second entry in the word list. That affected 1,163 occurrences in the esES corpus and 1,246 in esMX.

## Rebuild (maintainers)

1. Blizzard API keys in `Tools/keys.env`.
2. Nothing. `fetch_quests.py` asks the API which quests exist. An optional
   `Data/quest_ids.csv` with an `ID` column is merged in when present.
3. Run `Tools/build_all.ps1`.

Never commit `Tools/keys.env` or `Data/cache/`. Commit generated `Data/DictionaryESES.lua` and `Data/DictionaryESMX.lua`.

### Filling the gaps the API leaves

Blizzard's quest endpoint returns a title and the offer text only. `objectives`
comes back empty for all 30,815 quests, and there is no progress or hand-in
text and no NPC gossip at all, so a word living solely in one of those passages
can never enter this corpus. With **Collect quest and NPC text** enabled in
WordHunterWoW, `/whw harvest export` writes what a player has seen to
SavedVariables; fold it in with

```
python Tools/import_harvest.py --saved "<WoW>/_retail_/WTF/Account/<ACCT>/SavedVariables/WordHunterWoW.lua"
```

then rebuild from `build_wordlist.py` onward. Existing corpus text is never
overwritten -- only empty fields are filled.


All rights reserved.
