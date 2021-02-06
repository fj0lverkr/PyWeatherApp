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
    def __init__(self, json_data, u, tf):
        self.data = json_data
        self.units = u
        self.timeformat = '%H:%M' if tf == "24" else '%I:%M %p'

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
        beaufort = self.convert_to_beaufort(float(self.data['wind']['speed']))
        wind_degrees = int(self.data['wind']['deg'])

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

        # Icons
        temp_icon = IC['units'][temp_unit]
        sunrise_icon, sunset_icon = IC['time'].values()
        feels_icon, max_icon, min_icon, press_icon, humid_icon, visibility_icon = IC['misc'].values(
        )
        beaufort_icon = IC['wind']['speed'][beaufort]

        if 199 < weather_icon_id < 233:
            weather_icon = IC[day_night]['thunderstorm']
        elif (299 < weather_icon_id < 322) or 499 < weather_icon_id < 532:
            weather_icon = IC[day_night]['rain']
        elif 599 < weather_icon_id < 623:
            weather_icon = IC[day_night]['snow']
        elif 700 < weather_icon_id < 782:
            weather_icon = IC[day_night]['mist']
        elif weather_icon_id == 800:
            weather_icon = IC[day_night]['clear_sky']
        elif weather_icon_id == 801:
            weather_icon = IC[day_night]['few_clouds']
        elif weather_icon_id == 802:
            weather_icon = IC[day_night]['scattered_clouds']
        elif weather_icon_id in [803, 804]:
            weather_icon = IC[day_night]['broken_clouds']
        else:
            weather_icon = IC[day_night]['clear_sky']

        # Parse String
        weather = f" {location} {current_time_pretty} ({sunrise_icon}{sunrise_pretty} - {sunset_icon}{sunset_pretty}):"
        weather += f"\n {weather_icon}{weather_description}, {temp}{temp_icon} ({feels_icon} {feels_like}{temp_icon}, {min_icon} {min}{temp_icon} - {max_icon} {max}{temp_icon})"
        weather += f"\n {press_icon}{pressure}hPa, {humid_icon} {humidity}%, {visibility_icon} {visibility}m, {beaufort_icon} {beaufort} BFT"

        # Temp prints
        print(weather)
        print(f"\n\nRAW DATA:\n")
        for key, val in self.data.items():
            print(f"{key} -> {val}")

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
