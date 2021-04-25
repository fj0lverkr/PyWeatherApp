from requests import get
from datetime import datetime

from data.constants import WEATHER_ICONS as IC


class WeatherDataProvider:
    def __init__(self, api_key, ip, latlong, lang, units):
        self.api_key = api_key
        self.ip = ip
        self.lati, self.longi = latlong.values()
        self.lang = lang
        self.units = units

    def get_weather_data(self):
        return get(f"http://api.openweathermap.org/data/2.5/weather?lat={self.lati}&lon={self.longi}&appid={self.api_key}&lang={self.lang}&units={self.units}").json()


class WeatherDataParser:
    def __init__(self, json_data, u, tf, colors, color_off, color_icons_off):
        self.data = json_data
        self.units = u
        self.colors = colors
        self.color_off = color_off
        self.color_icons_off = color_icons_off
        if self.color_icons_off:
            self.timeformat = '%H:%M' if tf == "24" else '%I:%M %p'
        else:
            self.timeformat = '%H[blink]:[/blink]%M' if tf == "24" else '%I[blink]:[/blink]%M %p'

    def parse_data(self):
        location = self.data['name']
        weather_icon_id = int(self.data['weather'][0]['id'])
        weather_description = self.data['weather'][0]['description']
        sunrise = int(self.data['sys']['sunrise'])
        sunset = int(self.data['sys']['sunset'])
        current_time = int(self.data['dt'])
        shift_seconds = int(self.data['timezone'])
        sunrise_pretty = datetime.utcfromtimestamp(
            sunrise + shift_seconds).strftime(self.timeformat)
        sunset_pretty = datetime.utcfromtimestamp(
            sunset + shift_seconds).strftime(self.timeformat)
        current_time_pretty = datetime.utcfromtimestamp(
            current_time + shift_seconds).strftime(self.timeformat)
        temp, feels_like, min, max, pressure, humidity = self.data['main'].values(
        )
        visibility = self.data['visibility']
        self.beaufort = self.convert_to_beaufort(
            float(self.data['wind']['speed']))
        wind_direction = self.convert_to_cardinal_direction(
            float(self.data['wind']['deg']))

        if sunrise <= current_time < sunset:
            day_night = "day"
        else:
            day_night = "night"

        if self.units == "imperial":
            temp_unit = "fahrenheit"
        elif self.units == "metric":
            temp_unit = "celsius"
        else:
            temp_unit = "kelvin"

        # The following are only present in the response depending on the presence of the phenomena
        # clouds
        if 'clouds' in self.data:
            clouds_pct = self.data['clouds']['all']
        else:
            clouds_pct = -1

        # rain
        if 'rain' in self.data:
            rain_1h = self.data['rain']['1h']
            if '3h' in self.data['rain']:
                rain_3h = self.data['rain']['3h']
            else:
                rain_3h = -1
        else:
            rain_1h = -1
            rain_3h = -1

        # snow
        if 'snow' in self.data:
            snow_1h = self.data['snow']['1h']
            if '3h' in self.data['snow']:
                snow_3h = self.data['snow']['3h']
            else:
                snow_3h = -1
        else:
            snow_1h = -1
            snow_3h = -1

        # Icons and colors
        temp_icon = IC['units'][temp_unit]
        sunrise_icon, sunset_icon = IC['time'].values()
        feels_icon, max_icon, min_icon, press_icon, humid_icon, visibility_icon = IC['misc'].values(
        )
        beaufort_icon = IC['wind']['speed'][self.beaufort]
        wind_direction_icon = IC['wind']['direction'][wind_direction]

        if 199 < weather_icon_id < 233:
            weather_icon = IC[day_night]['thunderstorm']
            descr_color = self.colors['stormy']
        elif (299 < weather_icon_id < 322) or 499 < weather_icon_id < 532:
            weather_icon = IC[day_night]['rain']
            descr_color = self.colors['rainy']
            if rain_1h > 0 and rain_3h > 0:
                weather_description += f" ({rain_1h} mm/1h, {rain_3h} mm/3h)"
            elif rain_1h > 0:
                weather_description += f" ({rain_1h} mm/1h)"
        elif 599 < weather_icon_id < 623:
            weather_icon = IC[day_night]['snow']
            descr_color = self.colors['snowy']
            if snow_1h > 0 and snow_3h > 0:
                weather_description += f" ({snow_1h} mm/1h, {snow_3h} mm/3h)"
            elif snow_1h > 0:
                weather_description += f" ({snow_1h} mm/1h)"
        elif 700 < weather_icon_id < 782:
            weather_icon = IC[day_night]['mist']
            descr_color = self.colors['misty']
        elif weather_icon_id == 800:
            weather_icon = IC[day_night]['clear_sky']
            descr_color = self.colors[f'clear_{day_night}']
        elif weather_icon_id == 801:
            weather_icon = IC[day_night]['few_clouds']
            descr_color = self.colors['cloudy']
            if clouds_pct > 0:
                weather_description += f" ({clouds_pct}%)"
        elif weather_icon_id == 802:
            weather_icon = IC[day_night]['scattered_clouds']
            descr_color = self.colors['cloudy']
            if clouds_pct > 0:
                weather_description += f" ({clouds_pct}%)"
        elif weather_icon_id in [803, 804]:
            weather_icon = IC[day_night]['broken_clouds']
            descr_color = self.colors['cloudy']
            if clouds_pct > 0:
                weather_description += f" ({clouds_pct}%)"
        else:
            weather_icon = IC[day_night]['clear_sky']
            descr_color = self.colors[f'clear_{day_night}']

        base_color = self.colors[f'main_{day_night}']
        temp_color = self.color_code_temp(temp)
        feels_color = self.color_code_temp(feels_like)
        min_color = self.color_code_temp(min)
        max_color = self.color_code_temp(max)
        bft_color = self.color_code_bf()

        # Parse substrings
        if self.color_off:
            location = f" {location}"
            time = f"{current_time_pretty} ({sunrise_icon}{sunrise_pretty} {sunset_icon}{sunset_pretty}):"
            descr = f"\n {weather_icon}{weather_description},"
            temp = f"{temp}{temp_icon}({feels_icon} {feels_like}{temp_icon} "
            temp += f"{min_icon} {min}{temp_icon} "
            temp += f"{max_icon} {max}{temp_icon})"
            extras = f"\n {press_icon}{pressure}hPa, {humid_icon} {humidity}%, {visibility_icon} {visibility}m, {beaufort_icon} {self.beaufort} BFT {wind_direction_icon}"
        elif self.color_icons_off:
            location = f" {location}"
            time = f"{current_time_pretty} ({sunrise_pretty} - {sunset_pretty}):"
            descr = f"\n {weather_description},"
            temp = f"{temp}{temp_icon}(feels like {feels_like}{temp_icon}, "
            temp += f"min. {min}{temp_icon}, "
            temp += f"max. {max}{temp_icon})"
            extras = f"\n {pressure}hPa, {humidity}%, {visibility}m, {self.beaufort} BFT {wind_direction}"
        else:
            location = f" [{base_color}]{location}"
            time = f"{current_time_pretty} ([/{base_color}][{self.colors['clear_day']}]{sunrise_icon}{sunrise_pretty}[/{self.colors['clear_day']}] [{self.colors['sunset']}]{sunset_icon}{sunset_pretty}[/{self.colors['sunset']}][{base_color}]):[/{base_color}]"
            descr = f"\n [{descr_color}]{weather_icon}{weather_description},[/{descr_color}]"
            temp = f"[{temp_color}]{temp}{temp_icon}([{feels_color}]{feels_icon} {feels_like}{temp_icon}[/{feels_color}] "
            temp += f"[{min_color}]{min_icon} {min}{temp_icon}[/{min_color}] "
            temp += f"[{max_color}]{max_icon} {max}{temp_icon}[/{max_color}])[/{temp_color}]"
            extras = f"\n [{base_color}]{press_icon}{pressure}hPa, {humid_icon} {humidity}%, {visibility_icon} {visibility}m, [{bft_color}]{beaufort_icon} {self.beaufort} BFT {wind_direction_icon}[/{bft_color}][/{base_color}]"

        # Parse String
        weather = f"[bold]{location} {time}{descr} {temp}{extras}[/bold]\n"

        return weather

    def convert_to_beaufort(self, speed):
        if self.units == "imperial":
            if speed < 1.0:
                return 0
            elif 1.0 <= speed < 4.0:
                return 1
            elif 4.0 <= speed < 8.0:
                return 2
            elif 8.0 <= speed < 13.0:
                return 3
            elif 13.0 <= speed < 19.0:
                return 4
            elif 19.0 <= speed < 25.0:
                return 5
            elif 25.0 <= speed < 32.0:
                return 6
            elif 32.0 <= speed < 39.0:
                return 7
            elif 39.0 <= speed < 47.0:
                return 8
            elif 47.0 <= speed < 55.0:
                return 9
            elif 55.0 <= speed < 64.0:
                return 10
            elif 64.0 <= speed < 73.0:
                return 11
            else:
                return 12
        else:
            if 0.0 <= speed < 0.3:
                return 0
            elif 0.3 <= speed < 1.6:
                return 1
            elif 1.6 <= speed < 3.4:
                return 2
            elif 3.4 <= speed < 5.5:
                return 3
            elif 5.5 <= speed < 8.0:
                return 4
            elif 8.0 <= speed < 10.8:
                return 5
            elif 10.8 <= speed < 13.9:
                return 6
            elif 13.9 <= speed < 17.2:
                return 7
            elif 17.2 <= speed < 20.8:
                return 8
            elif 20.8 <= speed < 24.5:
                return 9
            elif 24.5 <= speed < 28.5:
                return 10
            elif 28.5 <= speed < 32.7:
                return 11
            else:
                return 12

    def convert_to_cardinal_direction(self, degrees):
        if 348.75 <= degrees < 11.25:
            return "N"
        elif 11.25 <= degrees < 33.75:
            return "NNE"
        elif 33.75 <= degrees < 56.25:
            return "NE"
        elif 56.25 <= degrees < 78.75:
            return "ENE"
        elif 78.75 <= degrees < 101.25:
            return "E"
        elif 101.25 <= degrees < 123.75:
            return "ESE"
        elif 123.75 <= degrees < 146.25:
            return "SE"
        elif 146.25 <= degrees < 168.75:
            return "SSE"
        elif 168.75 <= degrees < 191.25:
            return "S"
        elif 191.25 <= degrees < 213.75:
            return "SSW"
        elif 213.75 <= degrees < 236.25:
            return "SW"
        elif 236.25 <= degrees < 258.75:
            return "WSW"
        elif 258.75 <= degrees < 281.25:
            return "W"
        elif 281.25 <= degrees < 303.75:
            return "WNW"
        elif 303.75 <= degrees < 326.25:
            return "NW"
        else:
            return "NNW"

    def color_code_temp(self, temp):
        temp = float(temp)
        if self.units == "imperial":
            if 32.0 < temp < 60.8:
                color = 'cold'
            elif 60.8 <= temp <= 77.0:
                color = 'nice'
            elif 77.0 < temp <= 95.0:
                color = 'warm'
            elif 95.0 < temp:
                color = 'hot'
            elif temp <= 32.0:
                color = 'freezing'
            else:
                color = 'nice'
        elif self.units == "metric":
            if 0.0 < temp < 16.0:
                color = 'cold'
            elif 16.0 <= temp <= 25.0:
                color = 'nice'
            elif 25.0 < temp <= 35.0:
                color = 'warm'
            elif 35.0 < temp:
                color = 'hot'
            elif temp <= 0:
                color = 'freezing'
            else:
                color = 'nice'
        else:
            if 273.0 < temp < 289.15:
                color = 'cold'
            elif 289.15 <= temp <= 298.15:
                color = 'nice'
            elif 298.15 < temp <= 308.15:
                color = 'warm'
            elif 308.0 < temp:
                color = 'hot'
            elif temp <= 273.0:
                color = 'freezing'
            else:
                color = 'nice'
        return self.colors[f'temp_{color}']

    def color_code_bf(self):
        if 0 <= self.beaufort < 6:
            color = 'calm'
        elif 6 <= self.beaufort < 8:
            color = 'mild'
        elif 8 <= self.beaufort < 10:
            color = 'rough'
        else:
            color = 'danger'
        return self.colors[f'wind_{color}']
