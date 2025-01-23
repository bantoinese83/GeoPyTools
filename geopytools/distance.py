import math

def calculate_distance(point1, point2):
    """
    Calculate the distance between two points using the Haversine formula.

    Parameters:
    point1 (tuple): The latitude and longitude of the first point.
    point2 (tuple): The latitude and longitude of the second point.

    Returns:
    float: The distance between the two points in kilometers.
    """
    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of Earth in kilometers (mean radius)
    R = 6371.01

    # Calculate the distance
    distance = R * c

    return distance
