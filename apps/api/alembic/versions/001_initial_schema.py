"""Initial schema: users, batches, projects, project_contents, generation_metadata

Revision ID: 001
Revises:
Create Date: 2025-10-26
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create initial database schema."""
    # Enable UUID extension
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    # Create users table
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False, server_default=sa.text("uuid_generate_v4()")),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("company", sa.String(length=255), nullable=True),
        sa.Column("cognito_sub", sa.String(length=255), nullable=False),
        sa.Column(
            "preferences",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default=sa.text("'{\"defaultAiModel\": \"claude\", \"language\": \"pl\", \"notificationsEnabled\": true}'::jsonb"),
        ),
        sa.Column("last_login_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("cognito_sub"),
    )
    op.create_index(op.f("ix_users_created_at"), "users", ["created_at"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_cognito_sub"), "users", ["cognito_sub"], unique=True)

    # Create batches table
    op.create_table(
        "batches",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False, server_default=sa.text("uuid_generate_v4()")),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False, server_default="uploading"),
        sa.Column("total_projects", sa.Integer(), nullable=False),
        sa.Column("completed_projects", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.Column("average_quality_score", sa.Numeric(precision=5, scale=2), nullable=True, server_default=sa.text("0.0")),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("completed_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("expires_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.CheckConstraint("total_projects BETWEEN 1 AND 20", name="check_total_projects_range"),
        sa.CheckConstraint("average_quality_score BETWEEN 0 AND 100", name="check_quality_score_range"),
        sa.CheckConstraint(
            "status IN ('uploading', 'validating', 'validation_failed', 'queued', 'processing', 'completed', 'partially_completed', 'archived')",
            name="check_valid_status",
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_batches_created_at"), "batches", ["created_at"], unique=False)
    op.create_index(op.f("ix_batches_expires_at"), "batches", ["expires_at"], unique=False)
    op.create_index(op.f("ix_batches_status"), "batches", ["status"], unique=False)
    op.create_index(op.f("ix_batches_user_id"), "batches", ["user_id"], unique=False)

    # Create projects table
    op.create_table(
        "projects",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False, server_default=sa.text("uuid_generate_v4()")),
        sa.Column("batch_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("row_number", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False, server_default="pending"),
        sa.Column("quality_score", sa.Numeric(precision=5, scale=2), nullable=False, server_default=sa.text("0.0")),
        sa.Column("input_data", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("ai_model", sa.String(length=50), nullable=False, server_default="claude-3.5-sonnet"),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("generated_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column("edited_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.CheckConstraint("row_number BETWEEN 1 AND 20", name="check_row_number_range"),
        sa.CheckConstraint("quality_score BETWEEN 0 AND 100", name="check_project_quality_score_range"),
        sa.CheckConstraint(
            "status IN ('pending', 'generating', 'completed', 'failed', 'reviewed', 'exported')",
            name="check_valid_project_status",
        ),
        sa.ForeignKeyConstraint(["batch_id"], ["batches.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("batch_id", "row_number", name="uq_batch_row_number"),
    )
    op.create_index(op.f("ix_projects_batch_id"), "projects", ["batch_id"], unique=False)
    op.create_index(op.f("ix_projects_created_at"), "projects", ["created_at"], unique=False)
    op.create_index(op.f("ix_projects_status"), "projects", ["status"], unique=False)

    # Create project_contents table
    op.create_table(
        "project_contents",
        sa.Column("project_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("sections", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False, server_default=sa.text("1")),
        sa.Column("last_edited_section", sa.String(length=50), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("project_id"),
    )

    # Create generation_metadata table
    op.create_table(
        "generation_metadata",
        sa.Column("project_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("attempts", sa.Integer(), nullable=False, server_default=sa.text("1")),
        sa.Column("total_input_tokens", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.Column("total_output_tokens", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.Column("total_cost_eur", sa.Numeric(precision=10, scale=4), nullable=False, server_default=sa.text("0.0")),
        sa.Column("average_latency_ms", sa.Integer(), nullable=True),
        sa.Column("model_used", sa.String(length=50), nullable=False),
        sa.Column("errors", postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default=sa.text("'[]'::jsonb")),
        sa.Column("completed_at", sa.TIMESTAMP(timezone=True), nullable=True),
        sa.CheckConstraint("attempts BETWEEN 1 AND 3", name="check_attempts_range"),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("project_id"),
    )

    # Create trigger function to update batch quality score
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_batch_quality_score()
        RETURNS TRIGGER AS $$
        BEGIN
            UPDATE batches
            SET average_quality_score = (
                SELECT AVG(quality_score)
                FROM projects
                WHERE batch_id = NEW.batch_id AND quality_score > 0
            ),
            completed_projects = (
                SELECT COUNT(*)
                FROM projects
                WHERE batch_id = NEW.batch_id AND status = 'completed'
            )
            WHERE id = NEW.batch_id;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """
    )

    # Create trigger on projects table
    op.execute(
        """
        CREATE TRIGGER trigger_update_batch_quality
        AFTER UPDATE OF quality_score, status ON projects
        FOR EACH ROW
        EXECUTE FUNCTION update_batch_quality_score();
        """
    )


def downgrade() -> None:
    """Drop all tables and extensions."""
    # Drop trigger first
    op.execute("DROP TRIGGER IF EXISTS trigger_update_batch_quality ON projects")
    op.execute("DROP FUNCTION IF EXISTS update_batch_quality_score()")

    # Drop tables in reverse order
    op.drop_table("generation_metadata")
    op.drop_table("project_contents")
    op.drop_table("projects")
    op.drop_table("batches")
    op.drop_table("users")

    # Drop extension
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp"')
