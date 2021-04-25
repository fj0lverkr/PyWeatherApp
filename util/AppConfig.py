import os

from configparser import ConfigParser

from appdirs import user_config_dir


class AppConfig:
    def __init__(self, app_name, app_author, dict_colors, dict_icons):
        self.config_path = user_config_dir(
            appname=app_name, appauthor=app_author)
        self.constants_file = self.config_path + "/const.conf"
        self.api_key_file = self.config_path + "/api.conf"
        self.colors = dict_colors
        self.icons = dict_icons

    def init_app(self):
        if not os.path.exists(self.config_path):
            os.makedirs(self.config_path)

        if not os.path.exists(self.constants_file):
            const_conf = ConfigParser()
            const_conf["WEATHER_ICONS"] = self.icons
            const_conf["COLORS"] = self.colors
            with open(self.constants_file, 'w') as f:
                const_conf.write(f)

        if not os.path.exists(self.api_key_file):
            api_conf = ConfigParser()
            api_conf["API_KEYS"] = {
                "OWMKEY": "",
                "OPENCAGE": ""
            }
            with open(self.api_key_file, 'w') as f:
                api_conf.write(f)
            print(
                f"Config files were newly created, please add your API keys to {self.api_key_file} before running again.")
            exit(0)

    def get_api_keys(self):
        api_config = ConfigParser()
        api_config.read(self.api_key_file)
        api_keys = {
            "OWMKEY": api_config.get("API_KEYS", "owmkey"),
            "OPENCAGE": api_config.get("API_KEYS", "opencage")
        }
        if api_keys['OWMKEY'] == "" or api_keys['OPENCAGE'] == "":
            print(
                f"No API keys found in {self.api_key_file}, please add them!")
            exit(0)
        return api_keys
