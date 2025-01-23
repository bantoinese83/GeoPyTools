import unittest
from geopytools.distance import calculate_distance, calculate_distance_vincenty

class TestCalculateDistance(unittest.TestCase):

    def test_calculate_distance(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        expected_distance = 3940.07  # Expected distance in kilometers
        result = calculate_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_same_point(self):
        point = (40.7128, -74.0060)  # New York City
        expected_distance = 0.0  # Expected distance in kilometers
        result = calculate_distance(point, point)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_different_points(self):
        point1 = (51.5074, -0.1278)  # London
        point2 = (48.8566, 2.3522)  # Paris
        expected_distance = 343.77  # Expected distance in kilometers
        result = calculate_distance(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty(self):
        point1 = (40.7128, -74.0060)  # New York City
        point2 = (34.0522, -118.2437)  # Los Angeles
        expected_distance = 3935.75  # Expected distance in kilometers using Vincenty formula
        result = calculate_distance_vincenty(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty_same_point(self):
        point = (40.7128, -74.0060)  # New York City
        expected_distance = 0.0  # Expected distance in kilometers using Vincenty formula
        result = calculate_distance_vincenty(point, point)
        self.assertAlmostEqual(result, expected_distance, places=2)

    def test_calculate_distance_vincenty_different_points(self):
        point1 = (51.5074, -0.1278)  # London
        point2 = (48.8566, 2.3522)  # Paris
        expected_distance = 342.66  # Expected distance in kilometers using Vincenty formula
        result = calculate_distance_vincenty(point1, point2)
        self.assertAlmostEqual(result, expected_distance, places=2)

if __name__ == '__main__':
    unittest.main()
