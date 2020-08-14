import os

from flask import Flask

from forecast.config import AppConfig
from forecast.handlers.weather import construct_blueprint
from forecast.utils import WeatherAPI, GeocoderAPI, RecSysOutfit


class WeatherApp:
    def __init__(self):
        self.config = AppConfig()
        self.weather_api = WeatherAPI(self.config.WEATHERBIT_API_TOKEN)
        self.geocoder_api = GeocoderAPI(self.config.GEO_NAMES_USERNAME)
        self.recsys = RecSysOutfit(outfit_path='data/outfit.json',
                                   scores_path='data/intervals.json')

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(construct_blueprint(self.weather_api,
                                                   self.geocoder_api,
                                                   self.recsys))
        return app
