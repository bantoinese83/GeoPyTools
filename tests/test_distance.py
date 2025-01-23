import unittest
from geopytools.distance import haversine_distance, vincenty_distance

class TestCalculateDistance(unittest.TestCase):

    def test_calculate_distance(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        expected_distance = 3940.07  # Expected distance in kilometers
        result = haversine_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_same_point(self):
        point = (40.7128, -74.0060)  # New York City
        expected_distance = 0.0  # Expected distance in kilometers
        result = haversine_distance(point, point)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_different_points(self):
        point1 = (51.5074, -0.1278)  # London
        point2 = (48.8566, 2.3522)  # Paris
        expected_distance = 343.77  # Expected distance in kilometers
        result = haversine_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_invalid_coordinates(self):
        point1 = (91.0, -74.0060)  # Invalid latitude
        point2 = (34.0522, -118.2437)  # Los Angeles
        with self.assertRaises(ValueError) as context:
            haversine_distance(point1, point2)
        self.assertIn("Invalid coordinates for point1", str(context.exception))

        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -190.2437)  # Invalid longitude
        with self.assertRaises(ValueError) as context:
            haversine_distance(point1, point2)
        self.assertIn("Invalid coordinates for point2", str(context.exception))

    def test_calculate_distance_vincenty(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        expected_distance = 3935.75  # Expected distance in kilometers using Vincenty formula
        result = vincenty_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty_same_point(self):
        point = (40.7128, -74.0060)  # New York City
        expected_distance = 0.0  # Expected distance in kilometers using Vincenty formula
        result = vincenty_distance(point, point)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty_different_points(self):
        point1 = (51.5074, -0.1278)  # London
        point2 = (48.8566, 2.3522)  # Paris
        expected_distance = 342.66  # Expected distance in kilometers using Vincenty formula
        result = vincenty_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty_invalid_coordinates(self):
        point1 = (91.0, -74.0060)  # Invalid latitude
        point2 = (34.0522, -118.2437)  # Los Angeles
        with self.assertRaises(ValueError) as context:
            vincenty_distance(point1, point2)
        self.assertIn("Invalid coordinates for point1", str(context.exception))

        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -190.2437)  # Invalid longitude
        with self.assertRaises(ValueError) as context:
            vincenty_distance(point1, point2)
        self.assertIn("Invalid coordinates for point2", str(context.exception))

    def test_calculate_distance_caching(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        result1 = haversine_distance(point1, point2)
        result2 = haversine_distance(point1, point2)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

    def test_calculate_distance_vincenty_caching(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        result1 = vincenty_distance(point1, point2)
        result2 = vincenty_distance(point1, point2)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

if __name__ == '__main__':
    unittest.main()
