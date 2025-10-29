"""Base model and mixins for SQLAlchemy models."""

from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass


class TimestampMixin:
    """Mixin for created_at timestamp field."""

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False, index=True
    )


class UUIDMixin:
    """Mixin for UUID primary key."""

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True), primary_key=True, default=uuid4
    )


def utcnow() -> datetime:
    """Get current UTC datetime.

    Returns:
        datetime: Current UTC datetime
    """
    return datetime.now(UTC)
