"""ProjectContent model for generated content sections."""

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .project import Project


class ProjectContent(Base):
    """ProjectContent model for 8 Ulga B+R sections (1:1 with projects).

    Attributes:
        project_id: Foreign key to projects table (primary key)
        sections: JSONB containing all 8 sections
        version: Content version number
        last_edited_section: Key of last edited section
        project: Relationship to project
    """

    __tablename__ = "project_contents"

    # Fields
    project_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        primary_key=True,
    )
    sections: Mapped[dict[str, str]] = mapped_column(JSONB, nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    last_edited_section: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )

    # Relationships
    project: Mapped["Project"] = relationship(back_populates="content")  # noqa: F821

    def __repr__(self) -> str:
        """String representation of ProjectContent."""
        return f"<ProjectContent(project_id={self.project_id}, version={self.version})>"
