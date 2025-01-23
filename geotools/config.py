DEFAULT_UNIT = "km"
GOOGLE_API_KEY = "your-default-api-key"
OPENCAGE_API_KEY = "your-opencage-api-key"
MAPQUEST_API_KEY = "your-mapquest-api-key"

class Config:
    """
    Configuration class for GeoPyTools.

    Attributes:
    unit (str): The unit of measurement for distances (default is "km").
    timeout (int): The timeout value for API requests (default is 10 seconds).
    GOOGLE_API_KEY (str): The API key for Google Geocoding API.
    OPENCAGE_API_KEY (str): The API key for OpenCage Geocoding API.
    MAPQUEST_API_KEY (str): The API key for MapQuest Geocoding API.
    """
    unit = "km"
    timeout = 10
    GOOGLE_API_KEY = GOOGLE_API_KEY
    OPENCAGE_API_KEY = OPENCAGE_API_KEY
    MAPQUEST_API_KEY = MAPQUEST_API_KEY

    @classmethod
    def update_config(cls, **kwargs):
        """
        Update configuration values at runtime.

        Parameters:
        kwargs (dict): A dictionary of configuration values to update.
        """
        for key, value in kwargs.items():
            if hasattr(cls, key):
                setattr(cls, key, value)

    @classmethod
    def reset_config(cls):
        """
        Reset configuration values to defaults.
        """
        cls.unit = DEFAULT_UNIT
        cls.timeout = 10
        cls.GOOGLE_API_KEY = GOOGLE_API_KEY
        cls.OPENCAGE_API_KEY = OPENCAGE_API_KEY
        cls.MAPQUEST_API_KEY = MAPQUEST_API_KEY
