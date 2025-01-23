import unittest
from geopytools.analysis import find_centroid

class TestFindCentroid(unittest.TestCase):

    def test_find_centroid(self):
        points = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]  # NYC, LA, Chicago
        expected_centroid = (38.21436666666667, -93.95983333333334)  # Expected centroid coordinates
        result = find_centroid(points)
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_find_centroid_single_point(self):
        points = [(40.7128, -74.0060)]  # NYC
        expected_centroid = (40.7128, -74.0060)  # Expected centroid coordinates
        result = find_centroid(points)
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_find_centroid_empty_list(self):
        points = []
        with self.assertRaises(ValueError) as context:
            find_centroid(points)
        self.assertIn("No points provided", str(context.exception))

    def test_find_centroid_invalid_points(self):
        points = [(40.7128, -74.0060), (34.0522, 'invalid'), (41.8781, -87.6298)]  # NYC, LA (invalid), Chicago
        with self.assertRaises(ValueError) as context:
            find_centroid(points)
        self.assertIn("Invalid point", str(context.exception))

if __name__ == '__main__':
    unittest.main()
