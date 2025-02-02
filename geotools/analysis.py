import numpy as np


def batch_iterator(data, size):
    """
    Generate batches of data for processing.

    Parameters:
    data (list or generator): The data to be processed in batches.
    size (int): The size of each batch.

    Yields:
    list: A batch of data.
    """
    if isinstance(data, list):
        for i in range(0, len(data), size):
            yield data[i : i + size]
    else:
        batch = []
        for item in data:
            batch.append(item)
            if len(batch) == size:
                yield batch
                batch = []
        if batch:
            yield batch


def calculate_centroid(points, batch_size=1000):
    """
    Calculate the centroid of a set of points.

    Parameters:
    points (list or generator): A list or generator of tuples, where each tuple contains the latitude and longitude of a point.
    batch_size (int): The size of each batch for processing large inputs.

    Returns:
    tuple: The latitude and longitude of the centroid.

    Raises:
    ValueError: If the points list is empty or contains invalid points.
    """
    if not points:
        raise ValueError("No points provided. Please provide a list of points.")

    total_latitude = 0
    total_longitude = 0
    total_points = 0

    for batch in batch_iterator(points, batch_size):
        for point in batch:
            if (
                not isinstance(point, tuple)
                or len(point) != 2
                or not all(isinstance(coord, (int, float)) for coord in point)
            ):
                raise ValueError(
                    f"Invalid point: {point}. Each point must be a tuple of two numeric values."
                )

        latitudes = [point[0] for point in batch]
        longitudes = [point[1] for point in batch]

        total_latitude += np.sum(latitudes)
        total_longitude += np.sum(longitudes)
        total_points += len(batch)

    centroid_latitude = total_latitude / total_points
    centroid_longitude = total_longitude / total_points

    return centroid_latitude, centroid_longitude
