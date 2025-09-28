from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def get_lat_long(city, state, country):
    geolocator = Nominatim(user_agent="my_geocoder_app") # Replace with a unique user agent
    address = f"{city}, {state}, {country}"
    
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        print("Geocoding service timed out. Please try again.")
        return None, None
    except GeocoderServiceError as e:
        print(f"Geocoding service error: {e}")
        return None, None

# Example usage:
city_name = "Salt Lake City"
state_name = "UT"
country_name = "USA"

latitude, longitude = get_lat_long(city_name, state_name, country_name)

if latitude is not None and longitude is not None:
    print(f"The latitude and longitude for {city_name}, {state_name}, {country_name} are: ({latitude}, {longitude})")
else:
    print(f"Could not find coordinates for {city_name}, {state_name}, {country_name}.")