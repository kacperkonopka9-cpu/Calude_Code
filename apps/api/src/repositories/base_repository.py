"""Base repository with common database operations."""

from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Base repository with common CRUD operations.

    Attributes:
        model: SQLAlchemy model class
        session: AsyncSession for database operations
    """

    def __init__(self, model: type[ModelType], session: AsyncSession):
        """Initialize repository with model and session.

        Args:
            model: SQLAlchemy model class
            session: Async database session
        """
        self.model = model
        self.session = session

    async def get_by_id(self, id: UUID) -> ModelType | None:
        """Get entity by ID.

        Args:
            id: Entity UUID

        Returns:
            Entity if found, None otherwise
        """
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)  # type: ignore[attr-defined]
        )
        return result.scalar_one_or_none()

    async def create(self, **kwargs: object) -> ModelType:
        """Create new entity.

        Args:
            **kwargs: Entity fields

        Returns:
            Created entity with generated ID
        """
        entity = self.model(**kwargs)
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def delete(self, id: UUID) -> bool:
        """Delete entity by ID.

        Args:
            id: Entity UUID

        Returns:
            True if deleted, False if not found
        """
        entity = await self.get_by_id(id)
        if entity:
            await self.session.delete(entity)
            await self.session.commit()
            return True
        return False
