import sys
import getopt

from api import OWMKEY
from data.constants import *
from data.WeatherData import WeatherDataProvider, WeatherDataParser
from util.MetaData import MetaDataProvider


def main(argv):
    temperature_units = "metric"
    language = "en"
    try:
        opts, _ = getopt.getopt(argv, OPTIONS, LONG_OPTIONS)
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    if len(opts) == 0:
        print(USAGE)
        sys.exit(2)

    for opt, arg in opts:
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
        else:
            print(USAGE)
            sys.exit(2)

    mdp = MetaDataProvider()
    wdp = WeatherDataProvider(
        OWMKEY, mdp.client_ip, mdp.derived_location, language, temperature_units)
    wdparser = WeatherDataParser(wdp.get_weather_data())
    # wdparser.parse_data()
    print(WEATHER_ICONS)


if __name__ == "__main__":
    main(sys.argv[1:])
