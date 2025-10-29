"""Tests for application configuration."""

import os

import pytest

from src.config import Settings, get_settings


def test_settings_loads_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that Settings loads values from environment variables."""
    monkeypatch.setenv("API_HOST", "localhost")
    monkeypatch.setenv("API_PORT", "9000")
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")

    # Clear the cache to get fresh settings
    get_settings.cache_clear()

    settings = get_settings()

    assert settings.API_HOST == "localhost"
    assert settings.API_PORT == 9000
    assert settings.FRONTEND_URL == "http://localhost:3000"

    # Clean up
    get_settings.cache_clear()


def test_settings_applies_defaults() -> None:
    """Test that Settings applies default values when env vars not set."""
    # Clear any environment variables
    for key in ["API_HOST", "API_PORT", "FRONTEND_URL"]:
        os.environ.pop(key, None)

    # Clear the cache to get fresh settings
    get_settings.cache_clear()

    settings = Settings()

    assert settings.API_HOST == "0.0.0.0"
    assert settings.API_PORT == 8000
    assert settings.FRONTEND_URL == "http://localhost:5173"

    # Clean up
    get_settings.cache_clear()
