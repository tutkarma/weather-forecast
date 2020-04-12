import requests


class WeatherAPI:
    def __init__(self, token):
        self.token = token
        self.url = ' https://api.weatherbit.io/v2.0/current'

    def get(self, data):
        payload = {
            'key': self.token,
            'lat': data['lat'],
            'lon': data['lon']
        }

        r = requests.get(self.url, params=payload)
        if r.status_code != 200:
            raise Exception('Weather not received')

        response = r.json()

        return response['data'][0]
