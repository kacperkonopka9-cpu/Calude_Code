"""Tests for database connection and session management."""

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_database_connection(async_session: AsyncSession):
    """Test that database connection works."""
    result = await async_session.execute(text("SELECT 1"))
    value = result.scalar()
    assert value == 1


@pytest.mark.asyncio
async def test_database_tables_created(async_session: AsyncSession):
    """Test that all tables are created."""
    # Query for all table names
    result = await async_session.execute(
        text(
            """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name
        """
        )
    )
    tables = [row[0] for row in result.fetchall()]

    # Check that all expected tables exist
    expected_tables = {
        "users",
        "batches",
        "projects",
        "project_contents",
        "generation_metadata",
    }

    assert expected_tables.issubset(set(tables))
