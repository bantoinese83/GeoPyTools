import requests
from geotools.config import Config
from functools import lru_cache

@lru_cache(maxsize=128)
def geocode_address(address, api="google"):
    """
    Geocode an address using a geocoding API.

    Parameters:
    address (str): The address to geocode.
    api (str): The geocoding API to use ("google", "opencage", "mapquest").

    Returns:
    tuple: The latitude and longitude of the address.

    Raises:
    ValueError: If the API key is invalid or the address format is unsupported.
    """
    if api == "google":
        api_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": address,
            "key": Config.API_KEY
        }
    elif api == "opencage":
        api_url = "https://api.opencagedata.com/geocode/v1/json"
        params = {
            "q": address,
            "key": Config.OPENCAGE_API_KEY
        }
    elif api == "mapquest":
        api_url = "http://www.mapquestapi.com/geocoding/v1/address"
        params = {
            "location": address,
            "key": Config.MAPQUEST_API_KEY
        }
    else:
        raise ValueError("Unsupported API. Please use 'google', 'opencage', or 'mapquest'.")

    response = requests.get(api_url, params=params)
    
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise ValueError("Response could not be decoded. The response is empty or invalid.")

    if api == "google":
        if data["status"] == "REQUEST_DENIED":
            raise ValueError("Invalid API key. Please provide a valid API key.")
        elif data["status"] == "ZERO_RESULTS":
            raise ValueError("Unsupported address format. Please provide a valid address.")
        elif data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Geocoding API error: " + data["status"])
    elif api == "opencage":
        if data["status"]["code"] == 403:
            raise ValueError("Invalid API key. Please provide a valid API key.")
        elif data["status"]["code"] == 404:
            raise ValueError("Unsupported address format. Please provide a valid address.")
        elif data["status"]["code"] == 200:
            location = data["results"][0]["geometry"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Geocoding API error: " + data["status"]["message"])
    elif api == "mapquest":
        if data["info"]["statuscode"] == 403:
            raise ValueError("Invalid API key. Please provide a valid API key.")
        elif data["info"]["statuscode"] == 0:
            location = data["results"][0]["locations"][0]["latLng"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Geocoding API error: " + str(data["info"]["statuscode"]))

async def async_geocode_address(address, api="google"):
    """
    Asynchronously geocode an address using a geocoding API.

    Parameters:
    address (str): The address to geocode.
    api (str): The geocoding API to use ("google", "opencage", "mapquest").

    Returns:
    tuple: The latitude and longitude of the address.

    Raises:
    ValueError: If the API key is invalid or the address format is unsupported.
    """
    return geocode_address(address, api)
