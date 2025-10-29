"""Project model for individual R&D project cards."""

from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from .batch import Batch
    from .generation_metadata import GenerationMetadata
    from .project_content import ProjectContent


class Project(Base, UUIDMixin, TimestampMixin):
    """Project model representing an individual R&D project card.

    Attributes:
        id: UUID primary key
        batch_id: Foreign key to batches table
        row_number: Row number from Excel (1-20)
        status: Project processing status
        quality_score: Quality score (0-100)
        input_data: Project input data from Excel (JSONB)
        ai_model: AI model used for generation
        created_at: Timestamp of project creation
        generated_at: Timestamp when generation completed
        edited_at: Timestamp of last edit
        batch: Relationship to batch
        content: Relationship to project content (1:1)
        metadata: Relationship to generation metadata (1:1)
    """

    __tablename__ = "projects"

    # Fields
    batch_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("batches.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    row_number: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(
        String(50), nullable=False, default="pending", index=True
    )
    quality_score: Mapped[float] = mapped_column(
        Numeric(5, 2), default=0.0, nullable=False
    )
    input_data: Mapped[dict[str, str]] = mapped_column(JSONB, nullable=False)
    ai_model: Mapped[str] = mapped_column(
        String(50), nullable=False, default="claude-3.5-sonnet"
    )
    generated_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
    edited_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            "row_number BETWEEN 1 AND 20",
            name="check_row_number_range",
        ),
        CheckConstraint(
            "quality_score BETWEEN 0 AND 100",
            name="check_project_quality_score_range",
        ),
        CheckConstraint(
            "status IN ('pending', 'generating', 'completed', 'failed', 'reviewed', 'exported')",
            name="check_valid_project_status",
        ),
        UniqueConstraint("batch_id", "row_number", name="uq_batch_row_number"),
    )

    # Relationships
    batch: Mapped["Batch"] = relationship(back_populates="projects")
    content: Mapped[Optional["ProjectContent"]] = relationship(
        back_populates="project", cascade="all, delete-orphan", uselist=False
    )
    generation_metadata: Mapped[Optional["GenerationMetadata"]] = relationship(
        back_populates="project", cascade="all, delete-orphan", uselist=False
    )

    def __repr__(self) -> str:
        """String representation of Project."""
        return (
            f"<Project(id={self.id}, batch_id={self.batch_id}, "
            f"row_number={self.row_number}, status='{self.status}')>"
        )
