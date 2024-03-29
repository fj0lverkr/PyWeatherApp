APPNAME = "PyWeatherApp"
APPAUTHOR = "Fj0lverkr"

OPTIONS = "hu:l:c:t:"
LONG_OPTIONS = ["help", "units=", "language=",
                "city=", "timeformat=", "listlangs", "boring", "veryboring"]
UNITS = ["metric", "imperial"]
TIMEFORMATS = ["12", "24"]
USAGE = "Usage: main.py -h -u -l -c -t"
USAGE += "\n\t-h, --help: print this menu."
USAGE += "\n\t-u, --units: units (metric or imperial), defaults to metric."
USAGE += "\n\t-l, --language: language code (see --listlangs for available options), defaults to 'en' (English)."
USAGE += "\n\t-c, --city: city for which the weather should be retrieved. Defaults to approximate location (based on IP address)."
USAGE += "\n\t-t, --timeformat: preferred time format (12 or 24), defaults to 24."
USAGE += "\n\t--listlangs: show a list of available languages."
USAGE += "\n\t--boring: removes the pretty colors, if used together with --veryboring it will overrule it."
USAGE += "\n\t--veryboring removes the pretty colors and (most) of the icons, if used after with --boring it will overrule it."
USAGE += "\ntNote that none of these options are required, the program will run on defaults."

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
        ],
        "direction": {
            "N": "",
            "NNE": "",
            "NE": "",
            "ENE": "",
            "E": "",
            "ESE": "",
            "SE": "",
            "SSE": "",
            "S": "",
            "SSW": "",
            "SW": "",
            "WSW": "",
            "W": "",
            "WNW": "",
            "NW": "",
            "NNW": ""
        }
    },
    "misc": {
        "feelslike": "",
        "max": "",
        "min": "",
        "pressure": "猪",
        "humidity": "",
        "eye": ""
    }
}

COLORS = {
    'powershell': {
        'main': {
            'day': 'green',
            'night': 'blue'
        },
        'clear': {'day': 'yellow',
                  'night': 'blue'},
        'stormy': 'red',
        'rainy': 'blue',
        'cloudy': 'cyan',
        'snowy': 'white',
        'misty': 'cyan',
        'sunset': 'magenta',
        'temp': {
            'hot': 'red',
            'warm': 'yellow',
            'nice': 'magenta',
            'cold': 'blue',
            'freezing': 'white'
        },
        'wind': {
            'danger': 'red',
            'rough': 'yellow',
            'mild': 'green',
            'calm': 'white'
        }
    },
    'unix': {
        'main': {
            'day': 'spring_green2',
            'night': 'slate_blue3'
        },
        'clear': {'day': 'light_goldenrod1',
                  'night': 'light_slate_grey'},
        'stormy': 'light_slate_grey',
        'rainy': 'sky_blue2',
        'cloudy': 'grey70',
        'snowy': 'light_cyan1',
        'misty': 'grey78',
        'sunset': 'orange3',
        'temp': {
            'hot': 'red1',
            'warm': 'orange1',
            'nice': 'honeydew2',
            'cold': 'light_steel_blue1',
            'freezing': 'bright_white'
        },
        'wind': {
            'danger': 'red1',
            'rough': 'orange1',
            'mild': 'honeydew2',
            'calm': 'spring_green2'
        }
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
