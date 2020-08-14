import os

class AppConfig:
    WEATHERBIT_API_TOKEN = os.environ.get('WEATHERBIT_API_TOKEN')
    GEO_NAMES_USERNAME = os.environ.get('GEO_NAMES_USERNAME')

    if WEATHERBIT_API_TOKEN is None:
        raise Exception('Environment variable WEATHERBIT_API_TOKEN not set')

    if GEO_NAMES_USERNAME is None:
        raise Exception('Environment variable GEO_NAMES_USERNAME not set')
