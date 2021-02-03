from requests import get


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
        for key, val in self.data.items():
            print(f"{key} -> {val}")
