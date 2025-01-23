import unittest
import os
from geotools.config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.original_google_api_key = os.getenv("GOOGLE_API_KEY")
        self.original_opencage_api_key = os.getenv("OPENCAGE_API_KEY")
        self.original_mapquest_api_key = os.getenv("MAPQUEST_API_KEY")

    def tearDown(self):
        if self.original_google_api_key is not None:
            os.environ["GOOGLE_API_KEY"] = self.original_google_api_key
        if self.original_opencage_api_key is not None:
            os.environ["OPENCAGE_API_KEY"] = self.original_opencage_api_key
        if self.original_mapquest_api_key is not None:
            os.environ["MAPQUEST_API_KEY"] = self.original_mapquest_api_key

    def test_load_api_keys_from_env(self):
        os.environ["GOOGLE_API_KEY"] = "test-google-api-key"
        os.environ["OPENCAGE_API_KEY"] = "test-opencage-api-key"
        os.environ["MAPQUEST_API_KEY"] = "test-mapquest-api-key"

        Config.load_api_keys_from_env()

        self.assertEqual(Config.GOOGLE_API_KEY, "test-google-api-key")
        self.assertEqual(Config.OPENCAGE_API_KEY, "test-opencage-api-key")
        self.assertEqual(Config.MAPQUEST_API_KEY, "test-mapquest-api-key")

    def test_load_api_keys_from_env_with_defaults(self):
        if "GOOGLE_API_KEY" in os.environ:
            del os.environ["GOOGLE_API_KEY"]
        if "OPENCAGE_API_KEY" in os.environ:
            del os.environ["OPENCAGE_API_KEY"]
        if "MAPQUEST_API_KEY" in os.environ:
            del os.environ["MAPQUEST_API_KEY"]

        Config.load_api_keys_from_env()

        self.assertEqual(Config.GOOGLE_API_KEY, "your-default-api-key")
        self.assertEqual(Config.OPENCAGE_API_KEY, "your-opencage-api-key")
        self.assertEqual(Config.MAPQUEST_API_KEY, "your-mapquest-api-key")


if __name__ == "__main__":
    unittest.main()
