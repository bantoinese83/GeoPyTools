import unittest
from geotools.geocode import geocode_address, async_geocode_address

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

    def test_geocode_address_caching(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        result1 = geocode_address(address)
        result2 = geocode_address(address)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

    def test_geocode_address_valid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        valid_api_key = "your-valid-api-key"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="google", api_key=valid_api_key)
        self.assertEqual(result, expected_location)

    def test_geocode_address_opencage(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="opencage")
        self.assertEqual(result, expected_location)

    def test_geocode_address_mapquest(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = geocode_address(address, api="mapquest")
        self.assertEqual(result, expected_location)

    def test_geocode_address_mapquest_json_decode_error(self):
        address = "Invalid Address"
        with self.assertRaises(ValueError) as context:
            geocode_address(address, api="mapquest")
        self.assertIn("Response could not be decoded", str(context.exception))

    async def test_async_geocode_address_valid(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address)
        self.assertEqual(result, expected_location)

    async def test_async_geocode_address_invalid(self):
        address = "Invalid Address"
        with self.assertRaises(ValueError) as context:
            await async_geocode_address(address)
        self.assertIn("Unsupported address format", str(context.exception))

    async def test_async_geocode_address_invalid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        with self.assertRaises(ValueError) as context:
            await async_geocode_address(address)
        self.assertIn("Invalid API key", str(context.exception))

    async def test_async_geocode_address_caching(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        result1 = await async_geocode_address(address)
        result2 = await async_geocode_address(address)
        self.assertEqual(result1, result2)
        self.assertIs(result1, result2)

    async def test_async_geocode_address_valid_api_key(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        valid_api_key = "your-valid-api-key"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="google", api_key=valid_api_key)
        self.assertEqual(result, expected_location)

    async def test_async_geocode_address_opencage(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="opencage")
        self.assertEqual(result, expected_location)

    async def test_async_geocode_address_mapquest(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        expected_location = (37.4224764, -122.0842499)  # Expected coordinates
        result = await async_geocode_address(address, api="mapquest")
        self.assertEqual(result, expected_location)

if __name__ == '__main__':
    unittest.main()
