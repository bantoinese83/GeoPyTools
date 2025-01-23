import unittest
from geotools.analysis import calculate_centroid, batch_iterator

class TestFindCentroid(unittest.TestCase):

    def test_find_centroid(self):
        points = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]  # NYC, LA, Chicago
        expected_centroid = (38.881033333333335, -93.29316666666666)  # Expected centroid coordinates
        result = calculate_centroid(points)
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_find_centroid_single_point(self):
        points = [(40.7128, -74.0060)]  # NYC
        expected_centroid = (40.7128, -74.0060)  # Expected centroid coordinates
        result = calculate_centroid(points)
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_find_centroid_empty_list(self):
        points = []
        with self.assertRaises(ValueError) as context:
            calculate_centroid(points)
        self.assertIn("No points provided", str(context.exception))

    def test_find_centroid_invalid_points(self):
        points = [(40.7128, -74.0060), (34.0522, 'invalid'), (41.8781, -87.6298)]  # NYC, LA (invalid), Chicago
        with self.assertRaises(ValueError) as context:
            calculate_centroid(points)
        self.assertIn("Invalid point", str(context.exception))

    def test_find_centroid_batch_processing(self):
        points = [(i, i) for i in range(10000)]  # Large dataset
        result = calculate_centroid(points, batch_size=1000)
        expected_centroid = (4999.5, 4999.5)  # Expected centroid coordinates
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_find_centroid_iterators(self):
        points = ((i, i) for i in range(10000))  # Large dataset using generator
        result = calculate_centroid(points, batch_size=1000)
        expected_centroid = (4999.5, 4999.5)  # Expected centroid coordinates
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

    def test_batch_iterator(self):
        data = list(range(10))
        batch_size = 3
        expected_batches = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9]
        ]
        result_batches = list(batch_iterator(data, batch_size))
        self.assertEqual(result_batches, expected_batches)

    def test_find_centroid_valid_points_batch_processing(self):
        points = [(i, i) for i in range(10000)]  # Large dataset
        result = calculate_centroid(points, batch_size=1000)
        expected_centroid = (4999.5, 4999.5)  # Expected centroid coordinates
        self.assertAlmostEqual(result[0], expected_centroid[0], places=5)
        self.assertAlmostEqual(result[1], expected_centroid[1], places=5)

if __name__ == '__main__':
    unittest.main()
