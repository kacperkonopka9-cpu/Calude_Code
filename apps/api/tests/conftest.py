"""Pytest configuration and fixtures."""

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.database import get_db
from src.main import app
from src.models.base import Base

# Test database URL (use separate test database)
TEST_DATABASE_URL = "postgresql+asyncpg://postgres:claude_pass@localhost:5432/rnd_cards_test"


@pytest.fixture
async def client() -> AsyncClient:
    """Create async HTTP client for testing FastAPI endpoints."""
    async with AsyncClient(
        transport=ASGITransport(app=app),  # type: ignore
        base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture
async def async_engine():
    """Create async engine for test database."""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    # Drop all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest.fixture
async def async_session(async_engine):
    """Create async session for test database."""
    AsyncSessionLocal = async_sessionmaker(
        async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
def override_get_db(async_session):
    """Override get_db dependency to use test database."""
    async def _override_get_db():
        yield async_session

    app.dependency_overrides[get_db] = _override_get_db
    yield
    app.dependency_overrides.clear()
