from pydantic_settings import BaseSettings
from pydantic import Field
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables.
    
    Attributes:
        database_url: PostgreSQL connection URL with asyncpg driver
        api_keys: Comma-separated list of API keys for external services
        openai_api_key: OpenAI API key for LLM-powered SQL generation
    """
    database_url: str = Field(
        ...,
        description="PostgreSQL connection URL (must use postgresql+asyncpg://)",
        pattern="^postgresql\\+asyncpg://.*",
        alias="DATABASE_URL"
    )
    api_keys: str = Field(
        ...,
        description="Comma-separated list of API keys for external services",
        min_length=1,
        alias="API_KEYS"
    )
    openai_api_key: str = Field(
        ...,
        description="OpenAI API key for LLM-powered SQL generation",
        min_length=1,
        alias="OPENAI_API_KEY"
    )

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        case_sensitive = True

# Global settings instance
settings = Settings()