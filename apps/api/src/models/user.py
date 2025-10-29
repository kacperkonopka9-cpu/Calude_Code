"""User model for Polish tax consultants."""

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from .batch import Batch


class User(Base, UUIDMixin, TimestampMixin):
    """User model representing a Polish tax consultant.

    Attributes:
        id: UUID primary key
        email: User email (unique)
        name: User full name
        company: Optional company name
        cognito_sub: AWS Cognito user ID (unique)
        preferences: User preferences stored as JSONB
        last_login_at: Timestamp of last login
        created_at: Timestamp of user creation
        batches: Relationship to user's batches
    """

    __tablename__ = "users"

    # Fields
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    company: Mapped[str | None] = mapped_column(String(255), nullable=True)
    cognito_sub: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    preferences: Mapped[dict[str, str | bool]] = mapped_column(
        JSONB,
        nullable=False,
        default={
            "defaultAiModel": "claude",
            "language": "pl",
            "notificationsEnabled": True,
        },
    )
    last_login_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    # Relationships
    batches: Mapped[list["Batch"]] = relationship(  # noqa: F821
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        """String representation of User."""
        return f"<User(id={self.id}, email='{self.email}', name='{self.name}')>"
