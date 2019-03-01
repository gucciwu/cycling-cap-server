import googlemaps
from entry.settings import ACCESS_KEYS

gmaps = googlemaps.Client(key=ACCESS_KEYS.GOOGLE_MAP)


def get_elevation_by_location(location):
    pass


def get_elevation_by_path(from_location, to_location):
    pass

