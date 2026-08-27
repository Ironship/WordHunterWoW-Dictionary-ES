foreach ($locale in @("esES", "esMX")) {
  & "$PSScriptRoot/build_locale.ps1" -Locale $locale
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
Write-Host "Dictionary-ES data complete"
