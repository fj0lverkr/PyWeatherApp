from requests import get, ConnectionError, Timeout
from api import OPENCAGE

class MetaDataProvider:
    def __init__(self, location=""):
        self.location = location
        try: 
            get("https://api.ipify.org", timeout=10)
            self.internet_connected = True
            if self.location == "":
                self.ip = get("https://api.ipify.org").text
                self.latlong = get(
                    f"https://ipapi.co/{self.ip}/latlong/").text.split(',')
            else:
                self.ip = "127.0.0.1"
                self.latlong = get(
                    f"https://api.opencagedata.com/geocode/v1/json?q={self.location}&key={OPENCAGE}").json()
            
        except(ConnectionError, Timeout):
            self.ip = "127.0.0.1"
            self.latlong = [0, 0]
            self.location = ""
            self.internet_connected = False

    @property
    def client_online(self):
        return self.internet_connected

    @property
    def client_ip(self):
        return self.ip

    @property
    def derived_location(self):
        if self.location == "":
            lat, lon = self.latlong
            return {'lat': lat, 'lon': lon}
        return self.latlong['results'][0]['geometry']
