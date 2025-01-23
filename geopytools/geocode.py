import requests
from geopytools.config import API_KEY

def geocode_address(address):
    """
    Geocode an address using a geocoding API.

    Parameters:
    address (str): The address to geocode.

    Returns:
    tuple: The latitude and longitude of the address.

    Raises:
    ValueError: If the API key is invalid or the address format is unsupported.
    """
    api_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": API_KEY
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    if data["status"] == "REQUEST_DENIED":
        raise ValueError("Invalid API key. Please provide a valid API key.")
    elif data["status"] == "ZERO_RESULTS":
        raise ValueError("Unsupported address format. Please provide a valid address.")
    elif data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        raise Exception("Geocoding API error: " + data["status"])
