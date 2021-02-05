OPTIONS = "hu:l:c:t:"
LONG_OPTIONS = ["help", "units=", "language=", "city=", "timeformat=", "listlangs"]
UNITS = ["metric", "imperial"]
TIMEFORMATS = ["12", "24"]
USAGE = "Usage: main.py -h -u -l -c -t"
USAGE += "\n\t-h, --help: print this menu."
USAGE += "\n\t-u, --units: units (metric or imperial), defaults to metric."
USAGE += "\n\t-l, --language: language code (see --listlangs for available options), defaults to 'en' (English)."
USAGE += "\n\t-c, --city: city for which the weather should be retrieved. Defaults to approximate location (based on IP address)."
USAGE += "\n\t-t, --timeformat: preferred time format (12 or 24), defaults to 24."
USAGE += "\n\t--listlangs: slow a list of available languages."
USAGE += "\nNote that none of these options are required, the program will run on defaults."

WEATHER_ICONS = {
    "day": {
        "clear_sky": "盛",
        "few_clouds": "杖",
        "scattered_clouds": "摒",
        "broken_clouds": "樂",
        "shower_rain": "殺",
        "rain": "殺",
        "thunderstorm": "朗",
        "snow": "流",
        "mist": "敖"
    },
    "night": {
        "clear_sky": "望",
        "few_clouds": "摒",
        "scattered_clouds": "摒",
        "broken_clouds": "樂",
        "shower_rain": "殺",
        "rain": "殺",
        "thunderstorm": "朗",
        "snow": "流",
        "mist": "敖"
    },
    "units": {
        "celsius": "糖",
        "fahrenheit": "宅",
        "kelvin": "洞",
    },
    "time": {
        "sunrise": "瀞",
        "sunset": "漢"
    },
    "wind": {
        "speed": [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
    },
    "misc": {
        "feelslike": "",
        "max": "ﬢ",
        "min": "ﬠ",
        "pressure": "猪",
        "humidity": "",
        "eye": ""
    }
}
LANGUAGES = [
    "af",  # Afrikaans
    "al",  # Albanian
    "ar",  # Arabic
    "az",  # Azerbaijani
    "bg",  # Bulgarian
    "ca",  # Catalan
    "cz",  # Czech
    "da",  # Danish
    "de",  # German
    "el",  # Greek
    "en",  # English
    "eu",  # Basque
    "fa",  # Persian (Farsi)
    "fi",  # Finnish
    "fr",  # French
    "gl",  # Galician
    "he",  # Hebrew
    "hi",  # Hindi
    "hr",  # Croatian
    "hu",  # Hungarian
    "id",  # Indonesian
    "it",  # Italian
    "ja",  # Japanese
    "kr",  # Korean
    "la",  # Latvian
    "lt",  # Lithuanian
    "mk",  # Macedonian
    "no",  # Norwegian
    "nl",  # Dutch
    "pl",  # Polish
    "pt",  # Portuguese
    "pt_br",  # Português Brasil
    "ro",  # Romanian
    "ru",  # Russian
    "sv",  # Swedish
    "sk",  # Slovak
    "sl",  # Slovenian
    "es",  # Spanish
    "sr",  # Serbian
    "th",  # Thai
    "tr",  # Turkish
    "ua",  # Ukrainian
    "vi",  # Vietnamese
    "zh_cn",  # Chinese Simplified
    "zh_tw",  # Chinese Traditional
    "zu"  # Zulu
]

LANGUAGES_PRINTABLE = {
    "af":  "Afrikaans",
    "al":  "Albanian",
    "ar":  "Arabic",
    "az":  "Azerbaijani",
    "bg":  "Bulgarian",
    "ca":  "Catalan",
    "cz":  "Czech",
    "da":  "Danish",
    "de":  "German",
    "el":  "Greek",
    "en":  "English",
    "eu":  "Basque",
    "fa":  "Persian (Farsi)",
    "fi":  "Finnish",
    "fr":  "French",
    "gl":  "Galician",
    "he":  "Hebrew",
    "hi":  "Hindi",
    "hr":  "Croatian",
    "hu":  "Hungarian",
    "id":  "Indonesian",
    "it":  "Italian",
    "ja":  "Japanese",
    "kr":  "Korean",
    "la":  "Latvian",
    "lt":  "Lithuanian",
    "mk":  "Macedonian",
    "no":  "Norwegian",
    "nl":  "Dutch",
    "pl":  "Polish",
    "pt":  "Portuguese",
    "pt_br":  "Português Brasil",
    "ro":  "Romanian",
    "ru":  "Russian",
    "sv":  "Swedish",
    "sk":  "Slovak",
    "sl":  "Slovenian",
    "es":  "Spanish",
    "sr":  "Serbian",
    "th":  "Thai",
    "tr":  "Turkish",
    "ua":  "Ukrainian",
    "vi":  "Vietnamese",
    "zh_cn":  "Chinese Simplified",
    "zh_tw":  "Chinese Traditional",
    "zu":  "Zulu"
}