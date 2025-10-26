"""Batch repository for database operations on batches."""

from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.batch import Batch
from .base_repository import BaseRepository


class BatchRepository(BaseRepository[Batch]):
    """Repository for Batch model operations.

    Provides methods for batch CRUD operations and queries.
    """

    def __init__(self, session: AsyncSession):
        """Initialize BatchRepository.

        Args:
            session: Async database session
        """
        super().__init__(Batch, session)

    async def create(  # type: ignore[override]
        self, user_id: UUID, name: str, total_projects: int
    ) -> Batch:
        """Create new batch.

        Args:
            user_id: User UUID who owns the batch
            name: Batch name
            total_projects: Total number of projects (1-20)

        Returns:
            Created batch with generated ID and expiration date
        """
        batch = Batch(user_id=user_id, name=name, total_projects=total_projects)
        self.session.add(batch)
        await self.session.commit()
        await self.session.refresh(batch)
        return batch

    async def list_by_user(
        self, user_id: UUID, limit: int = 10, offset: int = 0
    ) -> list[Batch]:
        """List batches for a user.

        Args:
            user_id: User UUID
            limit: Maximum number of batches to return
            offset: Number of batches to skip

        Returns:
            List of batches ordered by created_at DESC
        """
        result = await self.session.execute(
            select(Batch)
            .where(Batch.user_id == user_id, Batch.status != "archived")
            .order_by(Batch.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(result.scalars().all())

    async def update_status(self, batch_id: UUID, status: str) -> None:
        """Update batch status.

        Args:
            batch_id: Batch UUID
            status: New status
        """
        await self.session.execute(
            update(Batch).where(Batch.id == batch_id).values(status=status)
        )
        await self.session.commit()

    async def get_by_id_with_projects(self, batch_id: UUID) -> Batch | None:
        """Get batch by ID with related projects loaded.

        Args:
            batch_id: Batch UUID

        Returns:
            Batch with projects if found, None otherwise
        """
        from sqlalchemy.orm import selectinload

        result = await self.session.execute(
            select(Batch)
            .where(Batch.id == batch_id)
            .options(selectinload(Batch.projects))
        )
        return result.scalar_one_or_none()

    async def count_by_user(self, user_id: UUID) -> int:
        """Count total batches for a user (excluding archived).

        Args:
            user_id: User UUID

        Returns:
            Total count of non-archived batches
        """
        from sqlalchemy import func

        result = await self.session.execute(
            select(func.count(Batch.id)).where(
                Batch.user_id == user_id, Batch.status != "archived"
            )
        )
        return result.scalar_one()
