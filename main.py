from requests import get

from api import OWMKEY
from data.WeatherData import WeatherDataProvider

ip = get("https://api.ipify.org").text
latlong = get(f"https://ipapi.co/{ip}/latlong/").text.split(',')

wdp = WeatherDataProvider(OWMKEY, ip, latlong)
print(wdp.get_weather_data())
