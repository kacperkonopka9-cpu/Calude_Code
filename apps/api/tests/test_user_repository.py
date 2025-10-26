"""Tests for UserRepository."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.user_repository import UserRepository


@pytest.mark.asyncio
async def test_create_user_success(async_session: AsyncSession):
    """Test that create_user creates a user with all fields."""
    repo = UserRepository(async_session)

    user = await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
        company="Test Company",
    )

    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.cognito_sub == "cognito-123"
    assert user.company == "Test Company"
    assert user.preferences == {
        "defaultAiModel": "claude",
        "language": "pl",
        "notificationsEnabled": True,
    }
    assert user.created_at is not None
    assert user.last_login_at is None


@pytest.mark.asyncio
async def test_get_user_by_id_found(async_session: AsyncSession):
    """Test that get_by_id returns user when found."""
    repo = UserRepository(async_session)

    # Create user
    created_user = await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Get by ID
    found_user = await repo.get_by_id(created_user.id)

    assert found_user is not None
    assert found_user.id == created_user.id
    assert found_user.email == created_user.email


@pytest.mark.asyncio
async def test_get_user_by_id_not_found(async_session: AsyncSession):
    """Test that get_by_id returns None when user not found."""
    from uuid import uuid4

    repo = UserRepository(async_session)

    user = await repo.get_by_id(uuid4())

    assert user is None


@pytest.mark.asyncio
async def test_get_user_by_email(async_session: AsyncSession):
    """Test that get_by_email returns user when found."""
    repo = UserRepository(async_session)

    # Create user
    await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Get by email
    found_user = await repo.get_by_email("test@example.com")

    assert found_user is not None
    assert found_user.email == "test@example.com"


@pytest.mark.asyncio
async def test_get_user_by_cognito_sub(async_session: AsyncSession):
    """Test that get_by_cognito_sub returns user when found."""
    repo = UserRepository(async_session)

    # Create user
    await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Get by cognito_sub
    found_user = await repo.get_by_cognito_sub("cognito-123")

    assert found_user is not None
    assert found_user.cognito_sub == "cognito-123"


@pytest.mark.asyncio
async def test_update_last_login(async_session: AsyncSession):
    """Test that update_last_login updates timestamp."""
    repo = UserRepository(async_session)

    # Create user
    user = await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    assert user.last_login_at is None

    # Update last login
    await repo.update_last_login(user.id)

    # Refresh user
    updated_user = await repo.get_by_id(user.id)

    assert updated_user is not None
    assert updated_user.last_login_at is not None


@pytest.mark.asyncio
async def test_update_preferences(async_session: AsyncSession):
    """Test that update_preferences updates user preferences."""
    repo = UserRepository(async_session)

    # Create user
    user = await repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Update preferences
    new_preferences = {
        "defaultAiModel": "gpt4",
        "language": "en",
        "notificationsEnabled": False,
    }
    await repo.update_preferences(user.id, new_preferences)

    # Refresh user
    updated_user = await repo.get_by_id(user.id)

    assert updated_user is not None
    assert updated_user.preferences == new_preferences
