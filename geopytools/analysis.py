import numpy as np

def find_centroid(points, batch_size=1000):
    """
    Find the centroid of a set of points.

    Parameters:
    points (list): A list of tuples, where each tuple contains the latitude and longitude of a point.
    batch_size (int): The size of each batch for processing large inputs.

    Returns:
    tuple: The latitude and longitude of the centroid.

    Raises:
    ValueError: If the points list is empty.
    """
    if not points:
        raise ValueError("No points provided. Please provide a list of points.")

    def batch_iterator(data, size):
        for i in range(0, len(data), size):
            yield data[i:i + size]

    total_latitude = 0
    total_longitude = 0
    total_points = 0

    for batch in batch_iterator(points, batch_size):
        latitudes = [point[0] for point in batch]
        longitudes = [point[1] for point in batch]

        total_latitude += np.sum(latitudes)
        total_longitude += np.sum(longitudes)
        total_points += len(batch)

    centroid_latitude = total_latitude / total_points
    centroid_longitude = total_longitude / total_points

    return centroid_latitude, centroid_longitude
