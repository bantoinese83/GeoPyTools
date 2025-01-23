import unittest
from geopytools.geocode import geocode_address

class TestGeocodeAddress(unittest.TestCase):

    def test_geocode_address_valid(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address)
        self.assertEqual(result, expected_location)

    def test_geocode_address_invalid(self):
        address = "Invalid Address"
        with self.assertRaises(Exception) as context:
            geocode_address(address)
        self.assertIn("Geocoding API error", str(context.exception))

if __name__ == '__main__':
    unittest.main()
