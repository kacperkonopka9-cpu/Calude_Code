"""FastAPI application entry point."""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .config import settings
from .database import get_db

app = FastAPI(
    title="R&D Tax Relief API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    """Health check endpoint with database connectivity verification.

    Returns:
        dict: Status, version, and database connection status

    Example response:
        {
            "status": "healthy",
            "version": "1.0.0",
            "database": "connected"
        }
    """
    # Verify database connectivity
    try:
        await db.execute(text("SELECT 1"))
        database_status = "connected"
    except Exception:
        database_status = "disconnected"

    return {
        "status": "healthy" if database_status == "connected" else "degraded",
        "version": "1.0.0",
        "database": database_status,
    }
