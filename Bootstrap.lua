local addonName = ...

local function registerDictionaries()
  local addon = WordHunterWoW_Addon
  if not addon or not addon.RegisterDictionaryProvider then return end
  if type(WordHunterWoW_Dictionary_ES_ES) == "table" then
    addon.RegisterDictionaryProvider("esES", addonName .. "-esES", WordHunterWoW_Dictionary_ES_ES)
  end
  if type(WordHunterWoW_Dictionary_ES_MX) == "table" then
    addon.RegisterDictionaryProvider("esMX", addonName .. "-esMX", WordHunterWoW_Dictionary_ES_MX)
  end
end

local events = CreateFrame("Frame")
events:RegisterEvent("ADDON_LOADED")
events:SetScript("OnEvent", function(_, _, loaded)
  if loaded == addonName then registerDictionaries() end
end)
