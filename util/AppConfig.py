import os

from configparser import ConfigParser

from appdirs import user_config_dir


class AppConfig:
    def __init__(self, app_name, app_author, dict_colors, dict_icons):
        sep = '\\' if os.name == 'nt' else '/'
        self.colors_root = 'powershell' if os.name == 'nt' else 'unix'
        self.config_path = user_config_dir(
            appname=app_name, appauthor=app_author)
        self.colors_file = self.config_path + f"{sep}colors.conf"
        self.api_key_file = self.config_path + f"{sep}api.conf"
        self.colors = dict_colors
        self.icons = dict_icons

    def init_app(self):
        if not os.path.exists(self.config_path):
            os.makedirs(self.config_path)

        if not os.path.exists(self.colors_file):
            colors_conf = ConfigParser()
            colors_conf['APP_COLORS'] = {}
            colors_conf['APP_COLORS']['main_day'] = self.colors[self.colors_root]['main']['day']
            colors_conf['APP_COLORS']['main_night'] = self.colors[self.colors_root]['main']['night']
            colors_conf['APP_COLORS']['clear_day'] = self.colors[self.colors_root]['clear']['day']
            colors_conf['APP_COLORS']['clear_night'] = self.colors[self.colors_root]['clear']['night']
            colors_conf['APP_COLORS']['stormy'] = self.colors[self.colors_root]['stormy']
            colors_conf['APP_COLORS']['rainy'] = self.colors[self.colors_root]['rainy']
            colors_conf['APP_COLORS']['cloudy'] = self.colors[self.colors_root]['cloudy']
            colors_conf['APP_COLORS']['snowy'] = self.colors[self.colors_root]['snowy']
            colors_conf['APP_COLORS']['misty'] = self.colors[self.colors_root]['misty']
            colors_conf['APP_COLORS']['sunset'] = self.colors[self.colors_root]['sunset']
            colors_conf['APP_COLORS']['temp_hot'] = self.colors[self.colors_root]['temp']['hot']
            colors_conf['APP_COLORS']['temp_warm'] = self.colors[self.colors_root]['temp']['warm']
            colors_conf['APP_COLORS']['temp_nice'] = self.colors[self.colors_root]['temp']['nice']
            colors_conf['APP_COLORS']['temp_cold'] = self.colors[self.colors_root]['temp']['cold']
            colors_conf['APP_COLORS']['temp_freezing'] = self.colors[self.colors_root]['temp']['freezing']
            colors_conf['APP_COLORS']['wind_danger'] = self.colors[self.colors_root]['wind']['danger']
            colors_conf['APP_COLORS']['wind_rough'] = self.colors[self.colors_root]['wind']['rough']
            colors_conf['APP_COLORS']['wind_mild'] = self.colors[self.colors_root]['wind']['mild']
            colors_conf['APP_COLORS']['wind_calm'] = self.colors[self.colors_root]['wind']['calm']

            with open(self.colors_file, 'w') as f:
                colors_conf.write(f)

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

    def get_colors(self):
        colors_config = ConfigParser()
        colors_config.read(self.colors_file)
        colors = {}
        for key in colors_config['APP_COLORS']:
            value = colors_config['APP_COLORS'][key]
            colors[key] = value if not value == "" else "white"
        return colors