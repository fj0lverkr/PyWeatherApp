import configparser
from appdirs import user_config_dir


class AppConfig:
    def __init__(self):
        self.constants_file = "const.conf"
        self.api_key_file = "api.conf"
