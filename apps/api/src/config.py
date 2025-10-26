"""Application configuration using Pydantic Settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API Server
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # Frontend
    FRONTEND_URL: str = "http://localhost:5173"

    # Database (future story)
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/rnd_cards"

    # Redis (future story)
    REDIS_URL: str = "redis://localhost:6379/0"

    # AWS (future stories)
    AWS_REGION: str = "eu-central-1"
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""

    # Cognito (Epic 8 - Auth)
    COGNITO_USER_POOL_ID: str = ""
    COGNITO_CLIENT_ID: str = ""

    # S3 (Story 1.4)
    S3_BUCKET: str = "rnd-cards-storage"

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
