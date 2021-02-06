from requests import get
from api import OPENCAGE

"""
TODO: find a more accurate way to get location since this off by +/- 150 KM, or use agument to provide city name in script?
"""


class MetaDataProvider:
    def __init__(self, location=""):
        self.location = location
        if self.location == "":
            self.ip = get("https://api.ipify.org").text
            self.latlong = get(
                f"https://ipapi.co/{self.ip}/latlong/").text.split(',')
        else:
            self.ip = "127.0.0.1"
            self.latlong = get(
                f"https://api.opencagedata.com/geocode/v1/json?q={self.location}&key={OPENCAGE}").json()

    @property
    def client_ip(self):
        return self.ip

    @property
    def derived_location(self):
        if self.location == "":
            lat, lon = self.latlong
            return {'lat': lat, 'lon': lon}
        return self.latlong['results'][0]['geometry']
