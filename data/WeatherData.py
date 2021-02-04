from requests import get
from datetime import datetime

from data.constants import WEATHER_ICONS as IC


class WeatherDataProvider:
    def __init__(self, api_key, ip, latlong, lang, units):
        self.api_key = api_key
        self.ip = ip
        self.lati, self.longi = latlong
        self.lang = lang
        self.units = units

    def get_weather_data(self):
        return get(f"http://api.openweathermap.org/data/2.5/weather?lat={self.lati}&lon={self.longi}&appid={self.api_key}&lang={self.lang}&units={self.units}").json()


class WeatherDataParser:
    def __init__(self, json_data):
        self.data = json_data

    def parse_data(self):
        location = self.data['name']
        weather_icon_id = int(self.data['weather'][0]['id'])
        weather_description = self.data['weather'][0]['description']
        sunrise = int(self.data['sys']['sunrise'])
        sunset = int(self.data['sys']['sunset'])
        current_time = int(self.data['dt'])
        sunrise_pretty = datetime.fromtimestamp(
            sunrise).strftime('%H:%M:%S')
        sunset_pretty = datetime.fromtimestamp(
            sunset).strftime('%H:%M:%S')
        current_time_pretty = datetime.fromtimestamp(
            current_time).strftime('%H:%M:%S')

        if sunrise <= current_time < sunset:
            day_night = "day"
        else:
            day_night = "night"

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

        weather = f"{location} ({current_time_pretty}):\n\t{weather_icon}{weather_description}"

        print(weather)

        for key, val in self.data.items():
            print(f"{key} -> {val}")
