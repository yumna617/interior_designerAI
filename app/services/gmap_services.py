import googlemaps
import os

gmaps = googlemaps.Client(key=os.getenv('ORS_API_KEY'))

def geocode_address(address):
    return gmaps.geocode(address)