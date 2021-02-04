import sys
import getopt

from api import OWMKEY
from data.constants import OPTIONS, LONG_OPTIONS, UNITS, LANGUAGES, LANGUAGES_PRINTABLE, USAGE, TIMEFORMATS
from data.WeatherData import WeatherDataProvider, WeatherDataParser
from util.MetaData import MetaDataProvider


def main(argv):
    temperature_units = "metric"
    language = "en"
    city = ""
    timeformat = "24"
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
                    print_languages()
                    sys.exit(0)
            else:
                print(USAGE)
                sys.exit(2)

    mdp = MetaDataProvider()
    wdp = WeatherDataProvider(
        OWMKEY, mdp.client_ip, mdp.derived_location, language, temperature_units, city)
    wdparser = WeatherDataParser(wdp.get_weather_data(), timeformat)
    wdparser.parse_data()

def print_languages():
    print("These are the languages supported by Openweathermap:")
    for k, l in LANGUAGES_PRINTABLE.items():
        print(f"\t{l}: {k}")

if __name__ == "__main__":
    main(sys.argv[1:])
