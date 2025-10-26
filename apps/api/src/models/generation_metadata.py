"""GenerationMetadata model for AI usage tracking."""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .project import Project


class GenerationMetadata(Base):
    """GenerationMetadata model for tracking AI usage and costs (1:1 with projects).

    Attributes:
        project_id: Foreign key to projects table (primary key)
        attempts: Number of generation attempts (1-3)
        total_input_tokens: Total input tokens used
        total_output_tokens: Total output tokens generated
        total_cost_eur: Total cost in EUR
        average_latency_ms: Average latency in milliseconds
        model_used: AI model used for generation
        errors: JSONB array of API errors
        completed_at: Timestamp when generation completed
        project: Relationship to project
    """

    __tablename__ = "generation_metadata"

    # Fields
    project_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        primary_key=True,
    )
    attempts: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    total_input_tokens: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    total_output_tokens: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0
    )
    total_cost_eur: Mapped[float] = mapped_column(
        Numeric(10, 4), nullable=False, default=0.0
    )
    average_latency_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    model_used: Mapped[str] = mapped_column(String(50), nullable=False)
    errors: Mapped[list[dict[str, str]]] = mapped_column(JSONB, nullable=False, default=[])
    completed_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            "attempts BETWEEN 1 AND 3",
            name="check_attempts_range",
        ),
    )

    # Relationships
    project: Mapped["Project"] = relationship(
        back_populates="generation_metadata"
    )

    def __repr__(self) -> str:
        """String representation of GenerationMetadata."""
        return (
            f"<GenerationMetadata(project_id={self.project_id}, "
            f"model='{self.model_used}', attempts={self.attempts})>"
        )
