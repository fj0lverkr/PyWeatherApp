from api import OWMKEY
from data.WeatherData import WeatherDataProvider
from util.MetaData import MetaDataProvider

mdp = MetaDataProvider()
wdp = WeatherDataProvider(OWMKEY, mdp.client_ip, mdp.derived_location)
print(wdp.get_weather_data())
