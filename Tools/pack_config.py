PACK_NAME = "WordHunterWoW-Dictionary-ES"

LOCALES = {
    "esES": {
        "api": "es_ES",
        "source": "es",
        "variable": "WordHunterWoW_Dictionary_ES_ES",
        "output": "DictionaryESES.lua",
        "curated": "CuratedESES.jsonl",
        # Function words. A quest field thick with the English ones and thin
        # on these is an untranslated row sitting in the locale file, and its
        # words are not Spanish words.
        "stopwords": ("el", "la", "los", "las", "un", "una", "de", "del", "que", "para",
                      "con", "no", "es", "son", "este", "esta", "en", "al", "por",
                      "se", "lo", "su", "como"),
        "single_char_words": "ayoeu",
    },
    "esMX": {
        "api": "es_MX",
        "source": "es",
        "variable": "WordHunterWoW_Dictionary_ES_MX",
        "output": "DictionaryESMX.lua",
        "curated": "CuratedESMX.jsonl",
        # Function words. A quest field thick with the English ones and thin
        # on these is an untranslated row sitting in the locale file, and its
        # words are not Spanish words.
        "stopwords": ("el", "la", "los", "las", "un", "una", "de", "del", "que", "para",
                      "con", "no", "es", "son", "este", "esta", "en", "al", "por",
                      "se", "lo", "su", "como"),
        "single_char_words": "ayoeu",
    },
}

ENGLISH_STOPWORDS = ("the", "and", "you", "your", "with", "from", "that",
                     "this", "have", "will", "they", "them", "been", "must",
                     "into", "there", "their", "what", "when", "would")
