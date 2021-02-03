from requests import get

"""
TODO: find a more accurate way to get location since this off by +/- 150 KM, or use agument to provide city name in script?
"""


class MetaDataProvider:
    def __init__(self):
        self.ip = get("https://api.ipify.org").text
        self.latlong = get(
            f"https://ipapi.co/{self.ip}/latlong/").text.split(',')

    @property
    def client_ip(self):
        return self.ip

    @property
    def derived_location(self):
        return self.latlong
