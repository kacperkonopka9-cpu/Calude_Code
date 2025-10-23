# 14. Deployment Architecture

## 14.1 Deployment Strategy

**Frontend Deployment:**
- **Platform:** AWS S3 + CloudFront
- **Build Command:** `npm run build --workspace=apps/web`
- **Output Directory:** `apps/web/dist`
- **CDN/Edge:** CloudFront with gzip/brotli compression
- **Cache Strategy:**
  - HTML: No cache (must-revalidate)
  - JS/CSS: 1 year cache with content hash in filename
  - Assets: 1 year cache

**Backend Deployment:**
- **Platform:** AWS ECS Fargate (2 vCPU, 4GB RAM)
- **Build Method:** Docker container
- **Deployment Method:** Blue-green deployment (zero downtime)
- **Auto-scaling:** 1-3 tasks based on CPU (>70% triggers scale-up)
- **Health Check:** `/health` endpoint

**Celery Workers:**
- **Platform:** AWS ECS Fargate (2 vCPU, 4GB RAM)
- **Deployment:** Rolling update
- **Concurrency:** 3 workers per task (AI generation)
- **Queue:** Redis (ElastiCache)

---

## 14.2 CI/CD Pipeline

**GitHub Actions Workflow:**

```yaml
# .github/workflows/ci.yaml
name: CI

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint --workspace=apps/web
      - run: npm run type-check --workspace=apps/web
      - run: npm test --workspace=apps/web

  test-backend:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r apps/api/requirements.txt
      - run: pytest apps/api/tests
      - run: ruff check apps/api/src
      - run: mypy apps/api/src

  e2e-tests:
    runs-on: ubuntu-latest
    needs: [test-frontend, test-backend]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npx playwright install
      - run: npm run test:e2e
```

```yaml
# .github/workflows/deploy.yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build --workspace=apps/web
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-central-1
      - run: aws s3 sync apps/web/dist s3://rnd-cards-prod --delete
      - run: aws cloudfront create-invalidation --distribution-id E1234567890ABC --paths "/*"

  deploy-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
      - run: |
          docker build -t rnd-cards-api apps/api
          aws ecr get-login-password | docker login --username AWS --password-stdin 123456789012.dkr.ecr.eu-central-1.amazonaws.com
          docker tag rnd-cards-api:latest 123456789012.dkr.ecr.eu-central-1.amazonaws.com/rnd-cards-api:latest
          docker push 123456789012.dkr.ecr.eu-central-1.amazonaws.com/rnd-cards-api:latest
      - run: aws ecs update-service --cluster rnd-cards --service api --force-new-deployment
```

---

## 14.3 Environments

| Environment | Frontend URL | Backend URL | Purpose |
|-------------|-------------|-------------|---------|
| **Development** | http://localhost:5173 | http://localhost:8000 | Local development |
| **Staging** | https://staging.rnd-cards.example.com | https://staging-api.rnd-cards.example.com | Pre-production testing |
| **Production** | https://rnd-cards.example.com | https://api.rnd-cards.example.com | Live environment |

---
