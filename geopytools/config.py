DEFAULT_UNIT = "km"
API_KEY = "your-default-api-key"
OPENCAGE_API_KEY = "your-opencage-api-key"
MAPQUEST_API_KEY = "your-mapquest-api-key"

class Config:
    """
    Configuration class for GeoPyTools.

    Attributes:
    unit (str): The unit of measurement for distances (default is "km").
    timeout (int): The timeout value for API requests (default is 10 seconds).
    """
    unit = "km"
    timeout = 10
