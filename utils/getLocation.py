from loader import geolocator

def get_location(latitude, longitude):
    location = geolocator.reverse(str(latitude) + "," + str(longitude))
    address = location.raw["address"]
    city = address.get("city", "")
    country = address.get("country", "")

    return city, country