# 13. Development Workflow

## 13.1 Local Development Setup

**Prerequisites:**

```bash
# Install required tools
node --version   # v20+
python --version # 3.11+
docker --version # 20+
```

**Initial Setup:**

```bash
# Clone repository
git clone https://github.com/your-org/rnd-tax-relief.git
cd rnd-tax-relief

# Install dependencies (all workspaces)
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with local credentials

# Start local services (PostgreSQL, Redis) via Docker
docker-compose up -d

# Run database migrations
cd apps/api
alembic upgrade head

# Generate sample data (optional)
python scripts/seed_db.py
```

**Development Commands:**

```bash
# Start all services (frontend + backend + workers)
npm run dev

# Start frontend only
npm run dev --workspace=apps/web

# Start backend only
npm run dev --workspace=apps/api

# Start Celery workers
cd apps/api
celery -A src.workers.celery_app worker -l info -c 3

# Run tests (all workspaces)
npm test

# Run tests (specific workspace)
npm test --workspace=apps/web

# Lint code
npm run lint

# Type check
npm run type-check
```

---

## 13.2 Environment Configuration

**Frontend (.env.local):**

```bash
VITE_API_BASE_URL=http://localhost:8000/v1
VITE_WS_URL=ws://localhost:8000/ws
VITE_COGNITO_USER_POOL_ID=eu-central-1_XXXXXXXXX
VITE_COGNITO_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXX
VITE_AWS_REGION=eu-central-1
```

**Backend (.env):**

```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/rnd_cards
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=user
POSTGRES_PASSWORD=pass
POSTGRES_DB=rnd_cards

# Redis
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# AWS
AWS_REGION=eu-central-1
AWS_ACCESS_KEY_ID=AKIAXXXXXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
S3_BUCKET_NAME=rnd-cards-dev
BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20241022-v2:0

# Azure (fallback)
AZURE_OPENAI_ENDPOINT=https://westeurope.api.cognitive.microsoft.com
AZURE_OPENAI_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4

# Cognito
COGNITO_USER_POOL_ID=eu-central-1_XXXXXXXXX
COGNITO_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXXXXXX

# LanguageTool
LANGUAGE_TOOL_API_URL=https://api.languagetool.org/v2
LANGUAGE_TOOL_API_KEY=XXXXXXXXXXXXXXXX

# App Config
ENVIRONMENT=development
LOG_LEVEL=DEBUG
FRONTEND_URL=http://localhost:5173
```

**Shared (.env at root):**

```bash
# Shared between frontend and backend
NODE_ENV=development
```

---
