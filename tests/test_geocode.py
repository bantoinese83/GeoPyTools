import unittest
from unittest.mock import patch
from geotools.geocode import geocode_address, async_geocode_address

class TestGeocodeAddress(unittest.IsolatedAsyncioTestCase):

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_valid(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address)
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_invalid(self):
        address = "Invalid Address"
        with self.assertRaises(ValueError) as context:
            geocode_address(address)
        self.assertIn("Unsupported address format", str(context.exception))

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_invalid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        with self.assertRaises(ValueError) as context:
            geocode_address(address)
        self.assertIn("Invalid API key", str(context.exception))

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_caching(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        result1 = geocode_address(address)
        result2 = geocode_address(address)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_valid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        valid_api_key = "mock-google-api-key"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="google", api_key=valid_api_key)
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_opencage(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="opencage")
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_mapquest(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="mapquest")
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    def test_geocode_address_mapquest_json_decode_error(self):
        address = "Invalid Address"
        with self.assertRaises(ValueError) as context:
            geocode_address(address, api="mapquest")
        self.assertIn("Response could not be decoded", str(context.exception))

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_valid(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address)
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_invalid(self):
        address = "Invalid Address"
        with self.assertRaises(ValueError) as context:
            await async_geocode_address(address)
        self.assertIn("Unsupported address format", str(context.exception))

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_invalid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        with self.assertRaises(ValueError) as context:
            await async_geocode_address(address)
        self.assertIn("Invalid API key", str(context.exception))

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_caching(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        result1 = await async_geocode_address(address)
        result2 = await async_geocode_address(address)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_valid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        valid_api_key = "mock-google-api-key"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="google", api_key=valid_api_key)
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_opencage(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="opencage")
        self.assertEqual(result, expected_location)

    @patch('geotools.geocode.Config.GOOGLE_API_KEY', 'mock-google-api-key')
    @patch('geotools.geocode.Config.OPENCAGE_API_KEY', 'mock-opencage-api-key')
    @patch('geotools.geocode.Config.MAPQUEST_API_KEY', 'mock-mapquest-api-key')
    async def test_async_geocode_address_mapquest(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="mapquest")
        self.assertEqual(result, expected_location)

if __name__ == '__main__':
    unittest.main()
