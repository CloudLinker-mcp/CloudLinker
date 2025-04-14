from pydantic_settings import BaseSettings  # type: ignore
class Settings(BaseSettings):
    database_url: str
    api_keys: str

    class Config:
        env_file = ".env"

settings = Settings()