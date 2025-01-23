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
        with self.assertRaises(ValueError) as context:
            geocode_address(address)
        self.assertIn("Unsupported address format", str(context.exception))

    def test_geocode_address_invalid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        with self.assertRaises(ValueError) as context:
            geocode_address(address)
        self.assertIn("Invalid API key", str(context.exception))

if __name__ == '__main__':
    unittest.main()
