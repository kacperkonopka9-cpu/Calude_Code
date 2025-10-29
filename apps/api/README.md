# R&D Tax Relief API

FastAPI backend for the R&D Tax Relief Project Card Generator.

## Prerequisites

- Python 3.11+
- pip 23+
- PostgreSQL 15+ (for database)

## Installation

### 1. Install PostgreSQL

**Windows:**
```bash
# Using winget (Windows Package Manager)
winget install PostgreSQL.PostgreSQL

# Or download from: https://www.postgresql.org/download/windows/
```

**macOS:**
```bash
brew install postgresql@15
```

**Linux:**
```bash
sudo apt-get install postgresql-15
```

### 2. Create Databases

```bash
# Connect to PostgreSQL
psql -U postgres

# Create development database
CREATE DATABASE rnd_cards;

# Create test database
CREATE DATABASE rnd_cards_test;

# Exit psql
\q
```

### 3. Create Virtual Environment

```bash
cd apps/api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
# On Windows, use: py -m pip install -r requirements.txt
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` with your database configuration:
```bash
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/rnd_cards
```

### 6. Initialize Database

Run Alembic migrations to create all tables:

```bash
# Using Alembic directly
alembic upgrade head

# Or using the initialization script
py scripts/init_db.py
```

## Development

### Start Development Server

```bash
uvicorn src.main:app --reload --port 8000
```

The API will be available at:
- API: http://localhost:8000
- Interactive API docs (Swagger): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc
- Health check: http://localhost:8000/health

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run with HTML coverage report
pytest tests/ --cov=src --cov-report=html
```

### Code Quality

#### Linting

```bash
# Check code
ruff check src/

# Auto-fix issues
ruff check src/ --fix

# Format code
ruff format src/
```

#### Type Checking

```bash
mypy src/
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `API_HOST` | API server host | `0.0.0.0` |
| `API_PORT` | API server port | `8000` |
| `FRONTEND_URL` | Frontend URL for CORS | `http://localhost:5173` |
| `DATABASE_URL` | PostgreSQL connection URL | `postgresql+asyncpg://postgres:postgres@localhost:5432/rnd_cards` |
| `REDIS_URL` | Redis connection URL | `redis://localhost:6379/0` |
| `AWS_REGION` | AWS region | `eu-central-1` |
| `AWS_ACCESS_KEY_ID` | AWS access key | - |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key | - |
| `COGNITO_USER_POOL_ID` | AWS Cognito user pool ID | - |
| `COGNITO_CLIENT_ID` | AWS Cognito client ID | - |
| `S3_BUCKET` | S3 bucket name | `rnd-cards-storage` |

## Database

### Database Migrations

This project uses Alembic for database migrations:

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history

# View current migration
alembic current
```

### Repository Pattern

The codebase uses the Repository pattern for data access:

```python
from src.database import get_db
from src.repositories.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession

# In FastAPI route
@app.get("/users/{user_id}")
async def get_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    user = await repo.get_by_id(user_id)
    return user
```

**Available Repositories:**
- `UserRepository`: User CRUD operations
- `BatchRepository`: Batch CRUD operations and queries

### Database Schema

The database includes the following core tables:
- `users`: Polish tax consultants
- `batches`: Groups of 1-20 project cards
- `projects`: Individual R&D project cards
- `project_contents`: Generated content for 8 Ulga B+R sections
- `generation_metadata`: AI usage tracking for cost monitoring

See `docs/architecture/9-database-schema.md` for complete schema documentation.

## Project Structure

```
apps/api/
├── src/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment configuration
│   ├── database.py          # Database connection and session
│   ├── routes/              # API route handlers
│   ├── services/            # Business logic
│   ├── repositories/        # Data access layer
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic schemas (validation)
│   ├── workers/             # Celery tasks
│   ├── middleware/          # Custom middleware
│   └── utils/               # Utilities
├── alembic/                 # Database migrations
│   ├── versions/            # Migration scripts
│   └── env.py               # Alembic configuration
├── scripts/                 # Utility scripts
│   └── init_db.py           # Database initialization
├── tests/                   # Backend tests
│   ├── conftest.py          # pytest fixtures
│   ├── test_main.py         # Health check tests
│   ├── test_config.py       # Config tests
│   ├── test_database.py     # Database connection tests
│   ├── test_user_repository.py  # User repository tests
│   └── test_batch_repository.py # Batch repository tests
├── pyproject.toml           # Python project config
├── requirements.txt         # Python dependencies
├── pytest.ini               # pytest configuration
├── ruff.toml                # Ruff linter config
├── mypy.ini                 # mypy type checker config
└── README.md                # This file
```

## Architecture

This backend follows a **layered architecture**:

- **Routes**: Handle HTTP requests and responses
- **Services**: Contain business logic
- **Repositories**: Manage data access (database queries)
- **Models**: Define database schema (SQLAlchemy ORM)
- **Schemas**: Define request/response validation (Pydantic)
- **Workers**: Handle background tasks (Celery)
- **Middleware**: Handle cross-cutting concerns (auth, logging, etc.)
- **Utils**: Shared utility functions

## Development Commands (from root)

When running from the project root, use these npm scripts:

```bash
npm run dev:api         # Start backend dev server
npm run test:api        # Run backend tests
npm run lint:api        # Run backend linting
npm run type-check:api  # Run backend type checking
```
