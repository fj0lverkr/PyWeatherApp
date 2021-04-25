import sys
import getopt

from rich.console import Console
from rich.table import Table

from data.constants import OPTIONS, LONG_OPTIONS, UNITS, LANGUAGES, LANGUAGES_PRINTABLE, USAGE, TIMEFORMATS, APPNAME, APPAUTHOR, COLORS, WEATHER_ICONS
from data.WeatherData import WeatherDataProvider, WeatherDataParser
from util.MetaData import MetaDataProvider
from util.AppConfig import AppConfig


def main(argv):
    app_config = AppConfig(APPNAME, APPAUTHOR, COLORS, WEATHER_ICONS)
    app_config.init_app()
    api_keys = app_config.get_api_keys()
    app_colors = app_config.get_colors()

    console = Console()
    temperature_units = "metric"
    language = "en"
    city = ""
    timeformat = "24"
    boring = False
    very_boring = False
    spinner = 'circleHalves'

    try:
        opts, _ = getopt.getopt(argv, OPTIONS, LONG_OPTIONS)
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    if len(opts) != 0:
        for opt, arg in opts:
            opt = opt.lower()
            if opt in ["-h", "--help"]:
                print(USAGE)
                sys.exit(0)
            elif opt in ["-u", "--unit"]:
                if arg.lower() in UNITS:
                    temperature_units = arg.lower()
                else:
                    print(
                        f"Invalid value for option {opt}, {arg} is not in {UNITS}.")
                    sys.exit(2)
            elif opt in ["-l", "--language"]:
                if arg.lower() in LANGUAGES:
                    language = arg.lower()
                else:
                    print(
                        f"Invalid value for option {opt}, {arg} is not in {LANGUAGES}.")
                    sys.exit(2)
            elif opt in ["-c", "--city"]:
                if arg.lower() == "":
                    print(
                        f"Invalid value for option {opt}, this option requires a value, nothing was given.")
                    sys.exit(2)
                else:
                    city = arg.lower()
            elif opt in ["-t", "--timeformat"]:
                if arg.lower() in TIMEFORMATS:
                    timeformat = arg.lower()
                else:
                    print(
                        f"Invalid value for option {opt}, {arg} is not in {LANGUAGES}.")
                    sys.exit(2)
            elif opt == "--listlangs":
                print_languages(console)
                sys.exit(0)
            elif opt == "--boring":
                boring = True
                very_boring = False
            elif opt == "--veryboring":
                very_boring = True
                boring = False
            else:
                print(USAGE)
                sys.exit(2)

    with console.status("Fetching weather...", spinner=spinner) as _:
        mdp = MetaDataProvider(api_keys['OPENCAGE'], location=city)
        if mdp.client_online:
            wdp = WeatherDataProvider(
                api_keys['OWMKEY'], mdp.client_ip, mdp.derived_location, language, temperature_units)
            wdparser = WeatherDataParser(
                wdp.get_weather_data(), temperature_units, timeformat, app_colors, boring, very_boring)
            console.print(wdparser.parse_data())
        else:
            console.print("Unable to fetch weather data in time.")


def print_languages(console):
    print("These are the languages supported by Openweathermap:")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Value")
    table.add_column("Language")
    for k, l in LANGUAGES_PRINTABLE.items():
        table.add_row(f"{l}", f"{k}")
    console.print(table)


if __name__ == "__main__":
    main(sys.argv[1:])
