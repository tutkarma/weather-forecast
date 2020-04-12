from flask import Flask

from forecast.handlers.weather import weather


def create_app():
    app = Flask(__name__)
    app.register_blueprint(weather)
    return app
