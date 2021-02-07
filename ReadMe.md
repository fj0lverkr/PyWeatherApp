# A small weather script in Python
This is a small but versatile weather data script written in Python (3.8).

Run main.py to get local weather data.

Run main.py *-h* (*--help*) to get available parameters.

Full example:
```
python main.py -c 'las vegas' -u imperial -t 12 -l nl
```
![screenshot on GNU/Linux Manjaro](/screenshots/screenshot1.png)
You can add something like the line above at the top of your $PROFILE (PowerShell) or .bashrc (.zshrc, etc) to have it set as a greeter each time you run your terminal of choice.

Tested on both Linux and Windows 10 (PowerShell) using the following Nerdfonts font:
- MesloLGS NF

## Python modules
The script uses *requests* and *rich*, you can add them to you system with pip:
```
pip install requests rich
```
## API keys
To make this work you should add a file 'api.py' to the root of the project (at the level opf main.py) which contains your api keys:
```
OWMKEY = "YOUR_API_KEY"
OPENCAGE = "YOUR_API_KEY"
```
The openweathermap key (OWMKEY) can be obtained by creating a free acount on https://openweathermap.org/, the Opencage key (OPENCAGE) can be obtained similarly (and also for free) on https://opencagedata.com/

## What are the API's for?
- The openweathermap API is used to get weather data using a given location in latitude and longitude.
- To get the location, the user either provides one using the *-c* (*--city*) option, which then gets translated to lat/long using the Opencagedata API.
- Alternatively, when the user doesn't provide a location, the current location is estimated from the user's IP, making use of the following API's:
  - https://api.ipify.org for the user's public IP
  - https://ipapi.co/{your_ip}/latlong/ to translate this IP to lat/long.
  - Neither of these require a key or account.

## Icons
This script uses Nerdfont glyphs to display weather icons. Please install a compatible Nerdfont from https://www.nerdfonts.com/font-downloads

These icons are defined in a dictionary in the file data/constants.py:
```
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
```
Should you want to use different icons, they can be easily replaced here.

The script should technically also work with different glyph providers (e.g. FontAwesome) if you replace the icons in the above mentioned dictionary and use a compatible font in your terminal.

Icons can be disabled using the *--veryboring* option, this will also disable the use of colors.

## Colors
The script displays colors when neither the *--boring* nor *--veryboring* flags are used.

The colors are defined in a dictionary in the file data/constants.py:
```
COLORS = {
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
```
Supported colors, should you want to change the current ones, can be found here: https://rich.readthedocs.io/en/latest/appendix/colors.html?highlight=colors

- The base color changes depending on the time of day (daytime color when the current time is between sunrise and sunset).
- The colors for sunrise and sunset are fixed.
- The color for the weather description changes depending on the type of weather.
- The color for the temperatures changes depending on a temperature scale.
- The color for the wind data (Beaufort and direction) change depending on the Beaufort value.
