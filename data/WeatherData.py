from requests import get

class WeatherDataProvider:
    def __init__(self, api_key, ip, latlong):
        self.api_key = api_key
        self.ip = ip
        self.lati, self.longi = latlong 

    def get_weather_data(self):
        return get(f"http://api.openweathermap.org/data/2.5/weather?lat={self.lati}&lon={self.longi}&appid={self.api_key}").json()
