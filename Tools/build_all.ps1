$ErrorActionPreference = "Stop"
$root = Split-Path $PSScriptRoot -Parent
Set-Location $root
foreach ($locale in @("esES", "esMX")) {
  python Tools/fetch_quests.py --locale $locale --workers 6 --interval 0.25
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  python Tools/build_wordlist.py --locale $locale
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  python Tools/translate_google.py --locale $locale --workers 4 --interval 0.25
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
  python Tools/build_dictionary_lua.py --locale $locale
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
Write-Host "Dictionary-ES data complete"
