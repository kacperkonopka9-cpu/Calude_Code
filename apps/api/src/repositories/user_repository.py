"""User repository for database operations on users."""

from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.user import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for User model operations.

    Provides methods for user CRUD operations and queries.
    """

    def __init__(self, session: AsyncSession):
        """Initialize UserRepository.

        Args:
            session: Async database session
        """
        super().__init__(User, session)

    async def create(  # type: ignore[override]
        self, email: str, name: str, cognito_sub: str, company: str | None = None
    ) -> User:
        """Create new user.

        Args:
            email: User email
            name: User full name
            cognito_sub: AWS Cognito user ID
            company: Optional company name

        Returns:
            Created user with generated ID
        """
        user = User(email=email, name=name, cognito_sub=cognito_sub, company=company)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_by_email(self, email: str) -> User | None:
        """Get user by email.

        Args:
            email: User email

        Returns:
            User if found, None otherwise
        """
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_by_cognito_sub(self, cognito_sub: str) -> User | None:
        """Get user by Cognito sub (user ID).

        Args:
            cognito_sub: AWS Cognito user ID

        Returns:
            User if found, None otherwise
        """
        result = await self.session.execute(
            select(User).where(User.cognito_sub == cognito_sub)
        )
        return result.scalar_one_or_none()

    async def update_last_login(self, user_id: UUID) -> None:
        """Update user's last login timestamp.

        Args:
            user_id: User UUID
        """
        from ..models.base import utcnow

        await self.session.execute(
            update(User)
            .where(User.id == user_id)
            .values(last_login_at=utcnow())
        )
        await self.session.commit()

    async def update_preferences(
        self, user_id: UUID, preferences: dict[str, str | bool]
    ) -> None:
        """Update user preferences.

        Args:
            user_id: User UUID
            preferences: New preferences dict
        """
        await self.session.execute(
            update(User).where(User.id == user_id).values(preferences=preferences)
        )
        await self.session.commit()
