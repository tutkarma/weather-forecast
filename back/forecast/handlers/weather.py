import os

from werkzeug.exceptions import BadRequest, NotFound
from flask import Blueprint, request, Response, current_app, json
from flask_cors import CORS


def construct_blueprint(
    weather_api,
    geocoder_api,
    recsys
):
    weather = Blueprint('weather', __name__)
    CORS(weather)

    @weather.route('/weather', methods=['POST'])
    def get_weather():
        data = request.get_json(force=True)

        try:
            query = data['query']
        except KeyError:
            raise BadRequest('Query not defined')

        try:
            coords = geocoder_api.get(query)
        except Exception:
            raise NotFound('Failed to get city coordinates')

        try:
            weather_response = weather_api.get(coords)
        except Exception:
            raise BadRequest('Failed to get weather forecast')

        info_for_recomendation = {
            'wind_spd': weather_response['wind_spd'],
            'app_temp': weather_response['app_temp'],
            'clouds': weather_response['clouds'],
            'snow': weather_response['snow'],
            'rh': weather_response['rh'],
        }
        recomendation = recsys.get_recomendation(info_for_recomendation)

        data = {
            'data': {
                'weather': weather_response,
                'recomendation': recomendation,
            }
        }

        return Response(
            json.dumps(data),
            status=200,
            mimetype='application/json'
        )

    return weather
