import math
from geopytools.config import DEFAULT_UNIT
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_distance(point1, point2, unit=DEFAULT_UNIT):
    """
    Calculate the distance between two points using the Haversine formula.

    Parameters:
    point1 (tuple): The latitude and longitude of the first point.
    point2 (tuple): The latitude and longitude of the second point.
    unit (str): The unit of measurement for the distance (default is "km").

    Returns:
    float: The distance between the two points in the specified unit.

    Raises:
    ValueError: If the coordinates are invalid.
    """
    if not (-90 <= point1[0] <= 90 and -180 <= point1[1] <= 180):
        raise ValueError("Invalid coordinates for point1. Latitude must be between -90 and 90, and longitude must be between -180 and 180.")
    if not (-90 <= point2[0] <= 90 and -180 <= point2[1] <= 180):
        raise ValueError("Invalid coordinates for point2. Latitude must be between -90 and 90, and longitude must be between -180 and 180.")

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

    if unit == "miles":
        distance *= 0.621371

    return distance

@lru_cache(maxsize=128)
def calculate_distance_vincenty(point1, point2, unit=DEFAULT_UNIT):
    """
    Calculate the distance between two points using the Vincenty formula.

    Parameters:
    point1 (tuple): The latitude and longitude of the first point.
    point2 (tuple): The latitude and longitude of the second point.
    unit (str): The unit of measurement for the distance (default is "km").

    Returns:
    float: The distance between the two points in the specified unit.

    Raises:
    ValueError: If the coordinates are invalid.
    """
    if not (-90 <= point1[0] <= 90 and -180 <= point1[1] <= 180):
        raise ValueError("Invalid coordinates for point1. Latitude must be between -90 and 90, and longitude must be between -180 and 180.")
    if not (-90 <= point2[0] <= 90 and -180 <= point2[1] <= 180):
        raise ValueError("Invalid coordinates for point2. Latitude must be between -90 and 90, and longitude must be between -180 and 180.")

    lat1, lon1 = point1
    lat2, lon2 = point2

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Vincenty formula
    a = 6378137.0  # Semi-major axis of the Earth (meters)
    f = 1 / 298.257223563  # Flattening of the Earth
    b = (1 - f) * a

    U1 = math.atan((1 - f) * math.tan(lat1))
    U2 = math.atan((1 - f) * math.tan(lat2))
    L = lon2 - lon1
    Lambda = L

    sinU1 = math.sin(U1)
    cosU1 = math.cos(U1)
    sinU2 = math.sin(U2)
    cosU2 = math.cos(U2)

    for _ in range(1000):
        sinLambda = math.sin(Lambda)
        cosLambda = math.cos(Lambda)
        sinSigma = math.sqrt((cosU2 * sinLambda) ** 2 + (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) ** 2)
        cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
        sigma = math.atan2(sinSigma, cosSigma)
        sinAlpha = cosU1 * cosU2 * sinLambda / sinSigma
        cos2Alpha = 1 - sinAlpha ** 2
        cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cos2Alpha
        C = f / 16 * cos2Alpha * (4 + f * (4 - 3 * cos2Alpha))
        Lambda_prev = Lambda
        Lambda = L + (1 - C) * f * sinAlpha * (sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM ** 2)))
        if abs(Lambda - Lambda_prev) < 1e-12:
            break

    u2 = cos2Alpha * (a ** 2 - b ** 2) / (b ** 2)
    A = 1 + u2 / 16384 * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
    B = u2 / 1024 * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))
    deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (cosSigma * (-1 + 2 * cos2SigmaM ** 2) - B / 6 * cos2SigmaM * (-3 + 4 * sinSigma ** 2) * (-3 + 4 * cos2SigmaM ** 2)))

    # Calculate the distance
    distance = b * A * (sigma - deltaSigma) / 1000  # Convert meters to kilometers

    if unit == "miles":
        distance *= 0.621371

    return distance
