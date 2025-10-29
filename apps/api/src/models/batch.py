"""Batch model for groups of project cards."""

from datetime import datetime, timedelta
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDMixin, utcnow

if TYPE_CHECKING:
    from .project import Project
    from .user import User


class Batch(Base, UUIDMixin, TimestampMixin):
    """Batch model representing a group of 1-20 project cards.

    Attributes:
        id: UUID primary key
        user_id: Foreign key to users table
        name: Batch name
        status: Batch processing status
        total_projects: Total number of projects in batch (1-20)
        completed_projects: Number of completed projects
        average_quality_score: Average quality score (0-100)
        created_at: Timestamp of batch creation
        completed_at: Timestamp when batch completed
        expires_at: Expiration timestamp (created_at + 90 days)
        user: Relationship to user
        projects: Relationship to projects in batch
    """

    __tablename__ = "batches"

    # Fields
    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), nullable=False, default="uploading", index=True
    )
    total_projects: Mapped[int] = mapped_column(Integer, nullable=False)
    completed_projects: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    average_quality_score: Mapped[float | None] = mapped_column(
        Numeric(5, 2), default=0.0, nullable=True
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    expires_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, index=True
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            "total_projects BETWEEN 1 AND 20",
            name="check_total_projects_range",
        ),
        CheckConstraint(
            "average_quality_score BETWEEN 0 AND 100",
            name="check_quality_score_range",
        ),
        CheckConstraint(
            "status IN ('uploading', 'validating', 'validation_failed', "
            "'queued', 'processing', 'completed', 'partially_completed', 'archived')",
            name="check_valid_status",
        ),
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="batches")  # noqa: F821
    projects: Mapped[list["Project"]] = relationship(  # noqa: F821
        back_populates="batch", cascade="all, delete-orphan"
    )

    def __init__(self, **kwargs: object):
        """Initialize batch with automatic expiration date."""
        super().__init__(**kwargs)
        if not hasattr(self, "expires_at") or not self.expires_at:
            self.expires_at = utcnow() + timedelta(days=90)

    def __repr__(self) -> str:
        """String representation of Batch."""
        return (
            f"<Batch(id={self.id}, name='{self.name}', "
            f"status='{self.status}', total_projects={self.total_projects})>"
        )
