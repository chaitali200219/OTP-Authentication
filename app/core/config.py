import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")
    APP_ENV: str = os.getenv("APP_ENV", "development")

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    REDIS_URL: str = os.getenv("REDIS_URL")

    OTP_EXPIRE_SECONDS: int = int(os.getenv("OTP_EXPIRE_SECONDS", 300))

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND")

    class Config:
        case_sensitive = True

settings = Settings()
