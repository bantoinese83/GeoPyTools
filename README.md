# GeoPyTools

![Build Status](https://img.shields.io/github/workflow/status/bantoinese83/GeoPyTools/Lint)
![Coverage](https://img.shields.io/codecov/c/github/bantoinese83/GeoPyTools)
![License](https://img.shields.io/github/license/bantoinese83/GeoPyTools)

GeoPyTools is a utility to calculate distances, geocode addresses, and analyze geospatial data easily. It provides a set of tools for geospatial analysis, including distance calculations, geocoding, and data analysis.

## Purpose

GeoPyTools aims to provide a comprehensive set of tools for geospatial analysis, allowing users to calculate distances, geocode addresses, and analyze geospatial data with ease. The package is designed to be modular, extensible, and user-friendly, enabling users to mix and match the components they need without unnecessary overhead.

## Features

| Feature | Description |
|---------|-------------|
| Distance Calculation | Calculate distances between two points using the Haversine and Vincenty formulas |
| Geocoding | Geocode addresses using a geocoding API |
| Data Analysis | Analyze geospatial data, such as finding the centroid of a set of points |

## Installation

To install GeoPyTools, follow these steps:

| Step | Command |
|------|---------|
| Clone the repository | `git clone https://github.com/bantoinese83/GeoPyTools.git` |
| Navigate to the project directory | `cd GeoPyTools` |
| Install the required dependencies | `pip install .` |

## Quickstart Guide

Here are some examples of how to use GeoPyTools:

### Calculate Distance

```python
from geopytools.distance import haversine_distance

point1 = (40.7128, -74.0060)  # New York City
point2 = (34.0522, -118.2437)  # Los Angeles

distance = haversine_distance(point1, point2)
print(f"The distance between New York City and Los Angeles is {distance} km")
```

### Calculate Distance using Vincenty formula

```python
from geopytools.distance import vincenty_distance

point1 = (40.7128, -74.0060)  # New York City
point2 = (34.0522, -118.2437)  # Los Angeles

distance = vincenty_distance(point1, point2)
print(f"The distance between New York City and Los Angeles using Vincenty formula is {distance} km")
```

### Calculate Distance Asynchronously

```python
import asyncio
from geopytools.distance import async_haversine_distance, async_vincenty_distance

async def main():
    point1 = (40.7128, -74.0060)  # New York City
    point2 = (34.0522, -118.2437)  # Los Angeles

    distance_haversine = await async_haversine_distance(point1, point2)
    print(f"The distance between New York City and Los Angeles using Haversine formula is {distance_haversine} km")

    distance_vincenty = await async_vincenty_distance(point1, point2)
    print(f"The distance between New York City and Los Angeles using Vincenty formula is {distance_vincenty} km")

asyncio.run(main())
```

### Geocode Address

```python
from geopytools.geocode import geocode_address

address = "1600 Amphitheatre Parkway, Mountain View, CA"
location = geocode_address(address)
print(f"The coordinates of the address are {location}")
```

### Geocode Address using OpenCage API

```python
from geopytools.geocode import geocode_address

address = "1600 Amphitheatre Parkway, Mountain View, CA"
location = geocode_address(address, api="opencage")
print(f"The coordinates of the address using OpenCage API are {location}")
```

### Geocode Address using MapQuest API

```python
from geopytools.geocode import geocode_address

address = "1600 Amphitheatre Parkway, Mountain View, CA"
location = geocode_address(address, api="mapquest")
print(f"The coordinates of the address using MapQuest API are {location}")
```

### Geocode Address Asynchronously

```python
import asyncio
from geopytools.geocode import async_geocode_address

async def main():
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    location = await async_geocode_address(address)
    print(f"The coordinates of the address are {location}")

asyncio.run(main())
```

### Analyze Geospatial Data

```python
from geopytools.analysis import calculate_centroid

points = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]  # NYC, LA, Chicago
centroid = calculate_centroid(points)
print(f"The centroid of the points is {centroid}")
```

## API Reference

| Function | Description |
|----------|-------------|
| `haversine_distance` | Calculate the distance between two points using the Haversine formula. |
| `vincenty_distance` | Calculate the distance between two points using the Vincenty formula. |
| `async_haversine_distance` | Asynchronously calculate the distance between two points using the Haversine formula. |
| `async_vincenty_distance` | Asynchronously calculate the distance between two points using the Vincenty formula. |
| `geocode_address` | Geocode an address using a geocoding API. |
| `async_geocode_address` | Asynchronously geocode an address using a geocoding API. |
| `calculate_centroid` | Find the centroid of a set of points. |

### `haversine_distance`

Calculate the distance between two points using the Haversine formula.

**Parameters:**
- `point1` (tuple): The latitude and longitude of the first point.
- `point2` (tuple): The latitude and longitude of the second point.

**Returns:**
- `float`: The distance between the two points in kilometers.

**Raises:**
- `ValueError`: If the coordinates are invalid.

### `vincenty_distance`

Calculate the distance between two points using the Vincenty formula.

**Parameters:**
- `point1` (tuple): The latitude and longitude of the first point.
- `point2` (tuple): The latitude and longitude of the second point.

**Returns:**
- `float`: The distance between the two points in kilometers.

**Raises:**
- `ValueError`: If the coordinates are invalid.

### `async_haversine_distance`

Asynchronously calculate the distance between two points using the Haversine formula.

**Parameters:**
- `point1` (tuple): The latitude and longitude of the first point.
- `point2` (tuple): The latitude and longitude of the second point.

**Returns:**
- `float`: The distance between the two points in kilometers.

**Raises:**
- `ValueError`: If the coordinates are invalid.

### `async_vincenty_distance`

Asynchronously calculate the distance between two points using the Vincenty formula.

**Parameters:**
- `point1` (tuple): The latitude and longitude of the first point.
- `point2` (tuple): The latitude and longitude of the second point.

**Returns:**
- `float`: The distance between the two points in kilometers.

**Raises:**
- `ValueError`: If the coordinates are invalid.

### `geocode_address`

Geocode an address using a geocoding API.

**Parameters:**
- `address` (str): The address to geocode.
- `api` (str): The geocoding API to use ("google", "opencage", "mapquest").

**Returns:**
- `tuple`: The latitude and longitude of the address.

**Raises:**
- `ValueError`: If the API key is invalid or the address format is unsupported.

### `async_geocode_address`

Asynchronously geocode an address using a geocoding API.

**Parameters:**
- `address` (str): The address to geocode.
- `api` (str): The geocoding API to use ("google", "opencage", "mapquest").

**Returns:**
- `tuple`: The latitude and longitude of the address.

**Raises:**
- `ValueError`: If the API key is invalid or the address format is unsupported.

### `calculate_centroid`

Find the centroid of a set of points.

**Parameters:**
- `points` (list): A list of tuples, where each tuple contains the latitude and longitude of a point.

**Returns:**
- `tuple`: The latitude and longitude of the centroid.

**Raises:**
- `ValueError`: If the points list is empty.

## Configuration

GeoPyTools allows you to override default configurations using the `config.py` file. You can set default values for units and API keys.

### Default Configuration

The default configuration is defined in the `config.py` file:

```python
DEFAULT_UNIT = "km"
API_KEY = "your-default-api-key"
OPENCAGE_API_KEY = "your-opencage-api-key"
MAPQUEST_API_KEY = "your-mapquest-api-key"

class Config:
    unit = "km"
    timeout = 10
```

### Overriding Default Configuration

You can override the default configuration at runtime by setting the desired values in the `Config` class:

```python
from geopytools.config import Config

Config.unit = "miles"
Config.timeout = 20
```

### Updating Configuration Values at Runtime

You can update configuration values at runtime using the `update_config` method of the `Config` class. For example, to update the unit of measurement to miles and the timeout value to 20 seconds, you can do the following:

```python
from geopytools.config import Config

Config.update_config(unit="miles", timeout=20)
```

### Resetting Configuration Values to Defaults

You can reset configuration values to their default values using the `reset_config` method of the `Config` class. For example, to reset the configuration values to their default values, you can do the following:

```python
from geopytools.config import Config

Config.reset_config()
```

## Using the `batch_size` Parameter in `calculate_centroid`

The `calculate_centroid` function allows you to calculate the centroid of a set of points. It has an optional `batch_size` parameter that can be used to process large inputs in batches. Here is how you can use the `batch_size` parameter:

### `calculate_centroid` Function

The `calculate_centroid` function calculates the centroid of a set of points. It has the following parameters:

- `points` (list): A list of tuples, where each tuple contains the latitude and longitude of a point.
- `batch_size` (int): The size of each batch for processing large inputs. The default value is 1000.

### Example Usage

Here is an example of how to use the `batch_size` parameter in the `calculate_centroid` function:

```python
from geopytools.analysis import calculate_centroid

points = [(i, i) for i in range(10000)]  # Large dataset
centroid = calculate_centroid(points, batch_size=1000)
print(f"The centroid of the points is {centroid}")
```

## Handling Exceptions

GeoPyTools functions may raise exceptions in certain situations. Here is a list of exceptions that may be raised and how to handle them:

### `ValueError`

- Raised by `haversine_distance` and `vincenty_distance` if the coordinates are invalid.
- Raised by `geocode_address` if the API key is invalid or the address format is unsupported.
- Raised by `calculate_centroid` if the points list is empty.

### `Exception`

- Raised by `geocode_address` if there is a geocoding API error.

### Example Usage

Here is an example of how to handle exceptions raised by GeoPyTools functions:

```python
from geopytools.distance import haversine_distance
from geopytools.geocode import geocode_address
from geopytools.analysis import calculate_centroid

try:
    point1 = (40.7128, -74.0060)  # New York City
    point2 = (34.0522, -118.2437)  # Los Angeles
    distance = haversine_distance(point1, point2)
    print(f"The distance between New York City and Los Angeles is {distance} km")
except ValueError as e:
    print(f"Error calculating distance: {e}")

try:
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    location = geocode_address(address)
    print(f"The coordinates of the address are {location}")
except ValueError as e:
    print(f"Error geocoding address: {e}")
except Exception as e:
    print(f"Geocoding API error: {e}")

try:
    points = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]  # NYC, LA, Chicago
    centroid = calculate_centroid(points)
    print(f"The centroid of the points is {centroid}")
except ValueError as e:
    print(f"Error calculating centroid: {e}")
```

## Versioning and Changelogs

GeoPyTools follows Semantic Versioning. Here are the versioning details:

- **1.0.0**: Initial stable release.
- **1.1.0**: Minor updates (new features).
- **1.1.1**: Bug fixes or patches.

## Contributing

We welcome contributions to GeoPyTools! If you would like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bugfix.
2. Write tests for your changes and ensure all tests pass.
3. Submit a pull request with a clear description of your changes.

## Roadmap

We have a roadmap to let users know what's planned next. Here are some of the upcoming features:

- Support for additional geocoding APIs
- Asynchronous versions of functions
- Performance optimizations for bulk calculations
- Real-life examples and use-case scenarios

## License

GeoPyTools is licensed under the MIT License. See the LICENSE file for more information.

## Linting and Formatting

To ensure code quality and consistency, we use `black` for code formatting and `flake8` for linting. You can run these tools locally to check your code before committing.

### Running Black

To check the code formatting using `black`, run the following command:

```sh
black --check .
```

If you want to automatically format the code, run:

```sh
black .
```

### Running Flake8

To check the code for linting issues using `flake8`, run the following command:

```sh
flake8 .
```
