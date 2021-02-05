from requests import get
from datetime import datetime

from data.constants import WEATHER_ICONS as IC


class WeatherDataProvider:
    def __init__(self, api_key, ip, latlong, lang, units, city):
        self.api_key = api_key
        self.ip = ip
        self.lati, self.longi = latlong
        self.lang = lang
        self.units = units
        self.city = city

    def get_weather_data(self):
        if self.city == "":
            return get(f"http://api.openweathermap.org/data/2.5/weather?lat={self.lati}&lon={self.longi}&appid={self.api_key}&lang={self.lang}&units={self.units}").json()
        else:
            return get(f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&lang={self.lang}&units={self.units}").json()


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
        sunrise_icon = IC['time']['sunrise']
        sunset_icon = IC['time']['sunset']
        temp, feels_like, min, max, pressure, humidity = self.data['main'].values()

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

        weather = f" {location} {current_time_pretty} ({sunrise_icon}{sunrise_pretty} - {sunset_icon}{sunset_pretty}):"
        weather += f"\n {weather_icon}{weather_description} {temp}{IC['units'][temp_unit]}"

        print(weather)

        print(f"\n\nRAW DATA:\n")
        for key, val in self.data.items():
            print(f"{key} -> {val}")
