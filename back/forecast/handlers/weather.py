import os

from geopy import geocoders
from werkzeug.exceptions import BadRequest, NotFound
from flask import Blueprint, request, Response, current_app, json
from flask_cors import CORS

from forecast.utils.weather_api import WeatherAPI

WEATHERBIT_API_TOKEN = os.environ.get('WEATHERBIT_API_TOKEN')
GEO_NAMES_USERNAME = os.environ.get('GEO_NAMES_USERNAME')


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
        gn = geocoders.GeoNames(username=GEO_NAMES_USERNAME)
    except Exception:
        raise BadRequest('Service is unavailable')

    try:
        coords = gn.geocode(query)
    except Exception:
        raise BadRequest('Service is unavailable')

    if coords is None:
        raise NotFound('Failed to get city coordinates')

    d = {
        'lat': coords.latitude,
        'lon': coords.longitude
    }

    api = WeatherAPI(WEATHERBIT_API_TOKEN)

    try:
        response = api.get(d)
    except Exception:
        raise BadRequest('Failed to get weather forecast')

    return Response(
        json.dumps({'data': response}),
        status=200,
        mimetype='application/json'
    )

