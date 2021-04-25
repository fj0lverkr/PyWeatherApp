from requests import get, ConnectionError, Timeout


class MetaDataProvider:
    def __init__(self, api_key, location=""):
        self.api_key = api_key
        self.location = location
        try:
            get("https://api.ipify.org", timeout=20)
            self.internet_connected = True
            if self.location == "":
                self.ip = get("https://api.ipify.org").text
                self.latlong = get(
                    f"https://ipapi.co/{self.ip}/latlong/").text.split(',')
            else:
                self.ip = "127.0.0.1"
                self.latlong = get(
                    f"https://api.opencagedata.com/geocode/v1/json?q={self.location}&key={self.api_key}").json()

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
