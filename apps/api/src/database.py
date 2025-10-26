"""Database configuration and session management."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .config import settings

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # Set to True for SQL query logging in development
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,  # Verify connections before using them
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Get database session for FastAPI dependency injection.

    Yields:
        AsyncSession: Database session

    Example:
        ```python
        @app.get("/users/{user_id}")
        async def get_user(
            user_id: UUID,
            db: AsyncSession = Depends(get_db)
        ):
            user = await db.get(User, user_id)
            return user
        ```
    """
    async with AsyncSessionLocal() as session:
        yield session
