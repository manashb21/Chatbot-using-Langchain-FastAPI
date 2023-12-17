from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = "config/.env"

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()

#this must be in the new branch
