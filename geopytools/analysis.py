import numpy as np

def find_centroid(points):
    """
    Find the centroid of a set of points.

    Parameters:
    points (list): A list of tuples, where each tuple contains the latitude and longitude of a point.

    Returns:
    tuple: The latitude and longitude of the centroid.

    Raises:
    ValueError: If the points list is empty.
    """
    if not points:
        raise ValueError("No points provided. Please provide a list of points.")

    latitudes = [point[0] for point in points]
    longitudes = [point[1] for point in points]

    centroid_latitude = np.mean(latitudes)
    centroid_longitude = np.mean(longitudes)

    return centroid_latitude, centroid_longitude
