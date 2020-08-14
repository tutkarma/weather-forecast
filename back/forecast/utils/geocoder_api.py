from geopy import geocoders


class GeocoderAPI:
    def __init__(self, username):
        self.username = username
        self.gn = geocoders.GeoNames(username=username)

    def get(self, query):
        coords = self.gn.geocode(query)

        if coords is None:
            raise Exception('Failed to get city coordinates')

        d = {
            'lat': coords.latitude,
            'lon': coords.longitude
        }

        return d
