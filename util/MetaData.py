from requests import get

class MetaDataProvider:
    def __init__(self):
        self.ip = get("https://api.ipify.org").text
        self.latlong = get(f"https://ipapi.co/{self.ip}/latlong/").text.split(',')

    @property
    def client_ip(self):
        return self.ip

    @property
    def derived_location(self):
        return self.latlong