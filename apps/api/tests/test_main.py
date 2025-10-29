"""Tests for main FastAPI application and health check endpoint."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check_returns_200_with_status(
    client: AsyncClient, override_get_db
) -> None:
    """Test that health endpoint returns 200 with healthy status."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_health_check_returns_version(
    client: AsyncClient, override_get_db
) -> None:
    """Test that health endpoint includes version information."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["version"] == "1.0.0"


@pytest.mark.asyncio
async def test_health_check_returns_database_status(
    client: AsyncClient, override_get_db
) -> None:
    """Test that health endpoint includes database connection status."""
    response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "database" in data
    assert data["database"] == "connected"
