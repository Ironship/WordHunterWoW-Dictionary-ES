# QuestWordHunter — Spanish Dictionary

Optional Spanish→English vocabulary packs for [QuestWordHunter](https://github.com/Ironship/WordHunterWoW), built from actual World of Warcraft quest text.

The addon contains separate dictionaries for European Spanish (`esES`) and Latin American Spanish (`esMX`). QuestWordHunter automatically uses the one matching the selected target language.

## What you need

- Retail 12.1 (`Interface 120100`)
- QuestWordHunter / WordHunterWoW
- Target language set to **Spanish (EU)** or **Spanish (MX)**

## Rebuild (maintainers)

1. Blizzard API keys in `Tools/keys.env`.
2. Wago QuestV2 CSV in `Data/QuestV2.csv`.
3. Run `Tools/build_all.ps1`.

Never commit `Tools/keys.env`, `Data/cache/`, or `Data/QuestV2.csv`. Commit generated `Data/DictionaryESES.lua` and `Data/DictionaryESMX.lua`.

All rights reserved.
