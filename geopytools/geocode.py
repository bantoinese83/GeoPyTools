import requests

def geocode_address(address):
    """
    Geocode an address using a geocoding API.

    Parameters:
    address (str): The address to geocode.

    Returns:
    tuple: The latitude and longitude of the address.
    """
    api_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": "YOUR_API_KEY"
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        raise Exception("Geocoding API error: " + data["status"])
