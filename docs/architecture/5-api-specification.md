# 5. API Specification

REST API with OpenAPI 3.0, automatic documentation at `/docs`

**Base URL:** `https://api.rnd-cards.example.com/v1`
**Authentication:** Bearer JWT tokens (AWS Cognito)
**WebSocket:** `wss://api.rnd-cards.example.com/ws`

## Core Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login (returns JWT)
- `GET /auth/me` - Get current user profile
- `POST /auth/refresh` - Refresh JWT token

### Templates
- `GET /templates/excel` - Download Excel template (.xlsx)

### Batches
- `GET /batches` - List user's batches (paginated)
- `POST /batches` - Create batch (upload Excel, multipart/form-data)
- `GET /batches/{batchId}` - Get batch with all projects
- `DELETE /batches/{batchId}` - Archive batch
- `POST /batches/{batchId}/generate` - Start AI generation (202 Accepted)

### Projects
- `GET /projects/{projectId}` - Get project with content
- `PATCH /projects/{projectId}` - Update section content
- `POST /projects/{projectId}/regenerate-section` - Regenerate specific section
- `POST /projects/{projectId}/retry` - Retry failed generation

### Export
- `GET /export/project/{projectId}` - Download single .docx
- `GET /export/batch/{batchId}` - Download batch as .zip

### Health
- `GET /health` - Health check with service status

## WebSocket Events

Connect to `wss://api.example.com/ws/{batchId}?token={jwt}`

**Events:**
- `project.status_changed` - Project status update
- `project.progress` - Generation progress %
- `batch.completed` - All projects finished
- `project.error` - Generation error

## Rate Limiting
- **100 requests/minute per user**
- **5 concurrent AI generations**
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`

---
