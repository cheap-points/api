from pydantic_settings import BaseSettings
import os 
class Settings(BaseSettings):
    PROJECT_NAME: str = "Meu App"
    API_V1: str = "/api/v1"
    
    MONGO_HOST:       str = os.getenv("MONGO_HOST")
    MONGO_USERNAME:   str = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD:   str = os.getenv("MONGO_PASSWORD")
    MONGO_DATABASE:   str = os.getenv("MONGO_DATABASE")

settings = Settings()
