"""Tests for BatchRepository."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.batch_repository import BatchRepository
from src.repositories.user_repository import UserRepository


@pytest.mark.asyncio
async def test_create_batch_success(async_session: AsyncSession):
    """Test that create_batch creates a batch with all fields."""
    # Create user first
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create batch
    batch_repo = BatchRepository(async_session)
    batch = await batch_repo.create(
        user_id=user.id, name="Test Batch", total_projects=10
    )

    assert batch.id is not None
    assert batch.user_id == user.id
    assert batch.name == "Test Batch"
    assert batch.status == "uploading"
    assert batch.total_projects == 10
    assert batch.completed_projects == 0
    assert batch.average_quality_score == 0.0
    assert batch.created_at is not None
    assert batch.expires_at is not None
    assert batch.completed_at is None


@pytest.mark.asyncio
async def test_list_batches_by_user(async_session: AsyncSession):
    """Test that list_by_user returns batches for a user."""
    # Create user
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create batches
    batch_repo = BatchRepository(async_session)
    batch1 = await batch_repo.create(
        user_id=user.id, name="Batch 1", total_projects=5
    )
    batch2 = await batch_repo.create(
        user_id=user.id, name="Batch 2", total_projects=10
    )

    # List batches
    batches = await batch_repo.list_by_user(user.id)

    assert len(batches) == 2
    # Should be ordered by created_at DESC
    assert batches[0].id == batch2.id
    assert batches[1].id == batch1.id


@pytest.mark.asyncio
async def test_list_batches_excludes_archived(async_session: AsyncSession):
    """Test that list_by_user excludes archived batches."""
    # Create user
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create batches
    batch_repo = BatchRepository(async_session)
    batch1 = await batch_repo.create(
        user_id=user.id, name="Active Batch", total_projects=5
    )
    batch2 = await batch_repo.create(
        user_id=user.id, name="Archived Batch", total_projects=10
    )

    # Archive batch2
    await batch_repo.update_status(batch2.id, "archived")

    # List batches
    batches = await batch_repo.list_by_user(user.id)

    assert len(batches) == 1
    assert batches[0].id == batch1.id


@pytest.mark.asyncio
async def test_update_batch_status(async_session: AsyncSession):
    """Test that update_status updates batch status."""
    # Create user
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create batch
    batch_repo = BatchRepository(async_session)
    batch = await batch_repo.create(
        user_id=user.id, name="Test Batch", total_projects=10
    )

    assert batch.status == "uploading"

    # Update status
    await batch_repo.update_status(batch.id, "processing")

    # Refresh batch
    updated_batch = await batch_repo.get_by_id(batch.id)

    assert updated_batch is not None
    assert updated_batch.status == "processing"


@pytest.mark.asyncio
async def test_list_batches_with_limit_offset(async_session: AsyncSession):
    """Test that list_by_user respects limit and offset."""
    # Create user
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create 5 batches
    batch_repo = BatchRepository(async_session)
    for i in range(5):
        await batch_repo.create(
            user_id=user.id, name=f"Batch {i + 1}", total_projects=5
        )

    # Get first 2 batches
    batches_page1 = await batch_repo.list_by_user(user.id, limit=2, offset=0)
    assert len(batches_page1) == 2

    # Get next 2 batches
    batches_page2 = await batch_repo.list_by_user(user.id, limit=2, offset=2)
    assert len(batches_page2) == 2

    # Ensure they're different batches
    assert batches_page1[0].id != batches_page2[0].id


@pytest.mark.asyncio
async def test_count_by_user(async_session: AsyncSession):
    """Test that count_by_user returns correct count."""
    # Create user
    user_repo = UserRepository(async_session)
    user = await user_repo.create(
        email="test@example.com",
        name="Test User",
        cognito_sub="cognito-123",
    )

    # Create batches
    batch_repo = BatchRepository(async_session)
    await batch_repo.create(user_id=user.id, name="Batch 1", total_projects=5)
    await batch_repo.create(user_id=user.id, name="Batch 2", total_projects=10)

    # Count batches
    count = await batch_repo.count_by_user(user.id)

    assert count == 2
