from typing import List
from pydantic.v1 import BaseSettings, AnyHttpUrl
from decouple import config


class Settings(BaseSettings):
    APP_URL: str = config('APP_URL', cast=str)
    PORT: int = config('PORT', cast=str)
    API_V1_STR: str = '/api/v1'
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str)
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 DAYS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = 'Festum Evento'

    # DATABASE
    MONGO_CONNECTION_STRING: str = config('MONGO_CONNECTION_STRING', cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
