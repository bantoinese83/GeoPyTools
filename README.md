# GeoPyTools

GeoPyTools is a utility to calculate distances, geocode addresses, and analyze geospatial data easily. It provides a set of tools for geospatial analysis, including distance calculations, geocoding, and data analysis.

## Features

- Calculate distances between two points using the Haversine formula
- Calculate distances between two points using the Vincenty formula
- Geocode addresses using a geocoding API
- Analyze geospatial data, such as finding the centroid of a set of points

## Installation

To install GeoPyTools, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   ```
2. Navigate to the project directory:
   ```
   cd workspace-blank
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Here are some examples of how to use GeoPyTools:

### Calculate Distance

```python
from geopytools.distance import calculate_distance

point1 = (40.7128, -74.0060)  # New York City
point2 = (34.0522, -118.2437)  # Los Angeles

distance = calculate_distance(point1, point2)
print(f"The distance between New York City and Los Angeles is {distance} km")
```

### Calculate Distance using Vincenty formula

```python
from geopytools.distance import calculate_distance_vincenty

point1 = (40.7128, -74.0060)  # New York City
point2 = (34.0522, -118.2437)  # Los Angeles

distance = calculate_distance_vincenty(point1, point2)
print(f"The distance between New York City and Los Angeles using Vincenty formula is {distance} km")
```

### Geocode Address

```python
from geopytools.geocode import geocode_address

address = "1600 Amphitheatre Parkway, Mountain View, CA"
location = geocode_address(address)
print(f"The coordinates of the address are {location}")
```

### Analyze Geospatial Data

```python
from geopytools.analysis import find_centroid

points = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]  # NYC, LA, Chicago
centroid = find_centroid(points)
print(f"The centroid of the points is {centroid}")
```

## Contributing

We welcome contributions to GeoPyTools! If you would like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bugfix.
2. Write tests for your changes and ensure all tests pass.
3. Submit a pull request with a clear description of your changes.

## License

GeoPyTools is licensed under the MIT License. See the LICENSE file for more information.
