from typing import Optional, Dict, Any
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_TITLE: str = "Zeus API"
    API_DESCRIPTION: str = "Zeus API"
    API_VERSION: str = "0.1.0"
    API_TERMS_OF_SERVICE: Optional[str] = None
    API_CONTACT: Optional[Dict[str, Any]] = None
    API_LICENSE_INFO: Optional[Dict[str, Any]] = None

settings = Settings()