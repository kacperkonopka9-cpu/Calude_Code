# R&D Tax Relief Project Card Generator - Fullstack Architecture Document

**Version:** 1.0
**Date:** October 22, 2025
**Architect:** Winston (BMad Architect Agent)
**Status:** Ready for Development

---

## Change Log

| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2025-10-22 | 1.0 | Initial architecture document | Winston |

---

## 1. Introduction

This document outlines the complete fullstack architecture for **R&D Tax Relief Project Card Generator**, including backend systems, frontend implementation, and their integration. It serves as the single source of truth for AI-driven development, ensuring consistency across the entire technology stack.

This unified approach combines what would traditionally be separate backend and frontend architecture documents, streamlining the development process for this modern fullstack application where these concerns are tightly integrated through AI services and real-time batch processing.

### 1.1 Starter Template

**Decision:** N/A - Greenfield project

This is a greenfield project with a well-defined technology stack from the PRD and technology research report. No starter template will be used, allowing maximum flexibility for the specific requirements (AWS Bedrock integration, Celery batch processing, custom MUI theme, GDPR compliance).

---

## 2. High Level Architecture

### 2.1 Technical Summary

The R&D Tax Relief Project Card Generator employs a **modern serverless-hybrid fullstack architecture** deployed primarily on AWS infrastructure within the EU-Central-1 region. The system features a **React 18 TypeScript SPA frontend** with Material-UI components, communicating with a **Python FastAPI backend** that orchestrates batch processing through Celery workers and Redis queue management. The architecture integrates **AWS Bedrock (Claude 3.5 Sonnet)** as the primary AI engine with **Azure OpenAI (GPT-4)** as a failover, ensuring resilient Polish-language project card generation. **PostgreSQL** stores metadata and session data, while **AWS S3** handles file storage with automated lifecycle policies for GDPR compliance. The system achieves real-time batch status updates through WebSocket connections, processes up to 5 concurrent AI requests, and exports government-compliant Word documents using python-docx, delivering a complete end-to-end workflow from Excel upload to downloadable .docx files in under 30 minutes for 20-project batches.

### 2.2 Platform and Infrastructure Choice

**Platform:** AWS (EU-Central-1 Frankfurt, Germany)

**Key Services:**
- **Compute:** ECS Fargate (backend API + Celery workers)
- **AI:** AWS Bedrock (Claude 3.5 Sonnet primary), Azure OpenAI Service (GPT-4 fallback)
- **Database:** RDS PostgreSQL 15+
- **Cache/Queue:** ElastiCache Redis 7+
- **Storage:** S3 (with lifecycle policies for GDPR compliance)
- **CDN:** CloudFront (frontend static assets)
- **Auth:** AWS Cognito User Pools
- **Monitoring:** CloudWatch (logs, metrics, dashboards, alerts)
- **Email:** Amazon SES (password reset, notifications)

**Deployment Host and Regions:**
- **Primary Region:** AWS EU-Central-1 (Frankfurt, Germany) - All data processing
- **Failover AI:** Azure West Europe (Netherlands) - GPT-4 fallback only
- **CDN Edge Locations:** CloudFront (Warsaw, Berlin, Amsterdam for low latency to Poland)

**Rationale:** AWS-centric approach chosen because AWS Bedrock is a hard requirement for Claude 3.5 Sonnet with EU data residency. Keeping all infrastructure on one cloud simplifies networking, IAM, monitoring, and GDPR compliance.

### 2.3 Repository Structure

**Structure:** Monorepo (single repository)

**Monorepo Tool:** npm workspaces (lightweight, no additional tooling)

**Package Organization:**
```
apps/
  web/          # React frontend application
  api/          # FastAPI backend application
packages/
  shared/       # Shared TypeScript types and constants
  config/       # Shared ESLint, TypeScript, Jest config
```

**Rationale:** Monorepo enables sharing TypeScript types between frontend and backend, simplified versioning, and coordinated deployment. npm workspaces sufficient for this project size (vs Nx/Turborepo overhead).

### 2.4 High Level Architecture Diagram

```mermaid
graph TB
    subgraph "Client Layer"
        USER[Polish Tax Consultant]
        BROWSER[Web Browser<br/>Chrome/Firefox/Edge]
    end

    subgraph "AWS CloudFront CDN"
        CDN[CloudFront Edge<br/>Warsaw/Berlin]
    end

    subgraph "Frontend - S3 + CloudFront"
        SPA[React 18 SPA<br/>Material-UI<br/>TypeScript]
    end

    subgraph "API Layer - AWS ECS Fargate"
        API[FastAPI REST API<br/>JWT Auth<br/>WebSocket]
        CELERY_WORKER[Celery Workers x3<br/>AI Generation<br/>Word Export]
    end

    subgraph "Data Layer - AWS"
        RDS[(PostgreSQL 15<br/>Metadata/Sessions)]
        REDIS[(ElastiCache Redis<br/>Queue/Cache)]
        S3[S3 Buckets<br/>Excel/Word Files<br/>Lifecycle Policies]
    end

    subgraph "AI Services"
        BEDROCK[AWS Bedrock<br/>Claude 3.5 Sonnet<br/>EU-Central-1]
        AZURE_AI[Azure OpenAI<br/>GPT-4 Fallback<br/>West Europe]
    end

    subgraph "Supporting Services"
        COGNITO[AWS Cognito<br/>User Auth]
        SES[Amazon SES<br/>Email]
        CLOUDWATCH[CloudWatch<br/>Monitoring]
    end

    USER -->|HTTPS| BROWSER
    BROWSER -->|Static Assets| CDN
    CDN --> SPA
    BROWSER -->|API Calls| API
    BROWSER -->|WebSocket| API

    API -->|Authenticate| COGNITO
    API -->|Queue Jobs| REDIS
    API -->|CRUD| RDS
    API -->|Upload/Download| S3
    API -->|Send Email| SES
    API -->|Logs/Metrics| CLOUDWATCH

    CELERY_WORKER -->|Poll Queue| REDIS
    CELERY_WORKER -->|Update Status| RDS
    CELERY_WORKER -->|Store Files| S3
    CELERY_WORKER -->|Generate Cards| BEDROCK
    CELERY_WORKER -->|Failover| AZURE_AI
    CELERY_WORKER -->|Logs| CLOUDWATCH

    style BEDROCK fill:#f9d71c
    style AZURE_AI fill:#0078d4
    style USER fill:#e1f5ff
```

### 2.5 Architectural Patterns

**Overall Architecture:**
- **Jamstack + Async Processing:** Static frontend with serverless API and background workers - _Rationale:_ Optimal performance for Polish users (CDN edge caching) while handling long-running AI generation asynchronously

**Frontend Patterns:**
- **Component-Based UI:** React components with TypeScript and Atomic Design - _Rationale:_ Maintainability and reusability across 5 core screens
- **Container/Presenter Pattern:** Smart containers handle logic, presentational components handle UI - _Rationale:_ Clear separation of concerns, easier testing
- **React Query for Server State:** Manage API state, caching, real-time updates - _Rationale:_ Eliminates Redux boilerplate, built-in cache invalidation

**Backend Patterns:**
- **Repository Pattern:** Abstract data access logic - _Rationale:_ Testability and future database migration flexibility
- **Task Queue Pattern:** Celery + Redis for async batch processing - _Rationale:_ Essential for 5 concurrent AI requests without blocking
- **Circuit Breaker Pattern:** Failover from Bedrock → Azure OpenAI on failures - _Rationale:_ Resilience against AI service outages
- **Retry with Exponential Backoff:** 3 retry attempts for failed AI calls - _Rationale:_ Handle transient API failures

**Integration Patterns:**
- **Backend for Frontend (BFF):** FastAPI orchestrates between React and AI services - _Rationale:_ Simplifies frontend complexity
- **API Gateway Pattern:** Single entry point with centralized auth, rate limiting, CORS - _Rationale:_ Security and monitoring chokepoint

---

## 3. Tech Stack

### Technology Stack Table

| Category | Technology | Version | Purpose | Rationale |
|----------|-----------|---------|---------|-----------|
| **Frontend Language** | TypeScript | 5.3+ | Type-safe frontend development | Prevents runtime errors, excellent IDE support, PRD requirement |
| **Frontend Framework** | React | 18.2+ | UI component framework | Industry standard, strong ecosystem, PRD requirement |
| **UI Component Library** | Material-UI (MUI) | 5.14+ | Pre-built accessible components | PRD custom iNOV theme, WCAG 2.1 AA built-in |
| **State Management** | React Query (TanStack Query) | 5.0+ | Server state management | Eliminates Redux boilerplate, WebSocket integration |
| **Backend Language** | Python | 3.11+ | Backend API and AI integration | Excellent AI library support, PRD requirement |
| **Backend Framework** | FastAPI | 0.104+ | REST API with OpenAPI docs | Async support, Pydantic validation, PRD requirement |
| **API Style** | REST + WebSocket | OpenAPI 3.0 | API communication | REST for CRUD, WebSocket for real-time updates |
| **Database** | PostgreSQL | 15+ | Relational data and metadata | JSONB for flexible content, ACID guarantees |
| **Cache** | Redis | 7+ | Celery broker + session cache | Required for Celery, sub-ms caching |
| **File Storage** | AWS S3 | - | Excel uploads and Word exports | Lifecycle policies for GDPR (90-day delete) |
| **Authentication** | AWS Cognito | - | User authentication | Managed service, JWT tokens, password reset |
| **Frontend Testing** | Vitest + React Testing Library | Vitest 1.0+, RTL 14+ | Component tests | Fast Vite-native testing |
| **Backend Testing** | pytest + pytest-asyncio | pytest 7.4+ | API and worker tests | Python standard, async FastAPI support |
| **E2E Testing** | Playwright | 1.40+ | End-to-end workflow testing | Cross-browser, file upload/download support |
| **Build Tool** | Vite | 5.0+ | Frontend build and dev server | 10-100x faster than Webpack, HMR |
| **Bundler** | Vite (esbuild) | 5.0+ | JS/TS bundling | Built into Vite, extremely fast |
| **IaC Tool** | AWS CDK | 2.100+ | Infrastructure as Code | TypeScript-based, higher-level than Terraform |
| **CI/CD** | GitHub Actions | - | Automated testing and deployment | Free, tight GitHub integration |
| **Monitoring** | AWS CloudWatch | - | Logs, metrics, alerts | Native AWS integration, cost tracking |
| **Logging** | Python logging + CloudWatch | - | Structured application logging | Standard library, JSON structured logs |
| **CSS Framework** | Tailwind CSS | 3.3+ | Utility-first styling | Complements MUI, rapid custom styling |
| **Excel Parsing** | SheetJS (xlsx) | 0.18+ | Client-side Excel parsing | Parse in browser before upload |
| **Excel Generation** | openpyxl | 3.1+ | Server Excel template generation | Python library for .xlsx templates |
| **Word Generation** | python-docx | 1.1+ | Generate .docx files | PRD requirement, validated in tech POC |
| **Task Queue** | Celery | 5.3+ | Async batch processing | Industry standard for Python |
| **AI SDK (AWS)** | boto3 (Bedrock) | 1.34+ | Claude 3.5 Sonnet integration | AWS SDK, Bedrock client |
| **AI SDK (Azure)** | openai (Azure) | 1.3+ | GPT-4 fallback | Official OpenAI SDK with Azure support |
| **Form Validation** | Zod | 3.22+ | Runtime type validation | TypeScript-first schema validation |
| **API Client** | Axios | 1.6+ | HTTP client | Request/response interceptors |
| **WebSocket Client** | Socket.IO Client | 4.6+ | Real-time batch updates | Auto-reconnection, fallback to polling |
| **WebSocket Server** | Socket.IO (Python) | 5.10+ | WebSocket server in FastAPI | Redis adapter for multi-worker |
| **Rich Text Editor** | TipTap | 2.1+ | Inline content editing | Headless editor, Polish support |
| **Date Handling** | date-fns | 3.0+ | Date parsing and formatting | Lightweight, tree-shakable, Polish locale |
| **Polish Grammar** | LanguageTool API | - | Automated grammar validation | Polish language support |

---

## 4. Data Models

Core business entities with shared TypeScript interfaces (in `packages/shared/src/types/`).

### User Model

**Purpose:** Polish tax consultant using the system

```typescript
interface User {
  id: string; // UUID v4
  email: string;
  name: string;
  company?: string;
  createdAt: Date;
  lastLoginAt?: Date;
  preferences: UserPreferences;
}

interface UserPreferences {
  defaultAiModel: 'claude' | 'gpt4';
  language: 'pl';
  notificationsEnabled: boolean;
}
```

**Relationships:** One User has many Batches (1:N)

---

### Batch Model

**Purpose:** Group of 1-20 project cards processed together

```typescript
interface Batch {
  id: string; // UUID v4
  userId: string;
  name: string;
  status: BatchStatus;
  totalProjects: number; // 1-20
  completedProjects: number;
  averageQualityScore: number; // 0-100
  createdAt: Date;
  completedAt?: Date;
  expiresAt: Date; // createdAt + 90 days
}

enum BatchStatus {
  UPLOADING = 'uploading',
  VALIDATING = 'validating',
  VALIDATION_FAILED = 'validation_failed',
  QUEUED = 'queued',
  PROCESSING = 'processing',
  COMPLETED = 'completed',
  PARTIALLY_COMPLETED = 'partially_completed',
  ARCHIVED = 'archived'
}
```

**Relationships:** Batch belongs to User (N:1), has many Projects (1:N)

---

### Project Model

**Purpose:** Individual R&D project card

```typescript
interface Project {
  id: string;
  batchId: string;
  rowNumber: number; // 1-20 from Excel
  status: ProjectStatus;
  qualityScore: number; // 0-100
  inputData: ProjectInputData;
  generatedContent?: ProjectContent;
  aiModel: 'claude-3.5-sonnet' | 'gpt-4';
  generationMetadata: GenerationMetadata;
  createdAt: Date;
  generatedAt?: Date;
  editedAt?: Date;
}

enum ProjectStatus {
  PENDING = 'pending',
  GENERATING = 'generating',
  COMPLETED = 'completed',
  FAILED = 'failed',
  REVIEWED = 'reviewed',
  EXPORTED = 'exported'
}

interface ProjectInputData {
  nazwaProjektu: string;
  opis: string; // ≥100 chars
  dataRozpoczecia: Date;
  dataZakonczenia: Date;
  celProjektu: string; // ≥50 chars
  osobaOdpowiedzialna: string;
}
```

---

### ProjectContent Model

**Purpose:** Generated content for 8 Ulga B+R sections

```typescript
interface ProjectContent {
  projectId: string;
  sections: Record<SectionKey, SectionContent>;
  version: number;
  lastEditedSection?: SectionKey;
}

enum SectionKey {
  NAZWA_PROJEKTU = 'nazwa_projektu',
  CEL_PROJEKTU = 'cel_projektu',
  OPIS_PROJEKTU = 'opis_projektu',
  NOWATORSTWO = 'nowatorstwo',
  METODOLOGIA = 'metodologia',
  REZULTATY = 'rezultaty',
  KOSZTY = 'koszty',
  HARMONOGRAM = 'harmonogram'
}

interface SectionContent {
  key: SectionKey;
  text: string; // Polish markdown
  isAiGenerated: boolean; // true = yellow, false = white
  qualityScore: number; // 0-100
  characterCount: number;
  generatedAt?: Date;
  editedAt?: Date;
  editedBy?: 'consultant' | 'ai-regeneration';
}
```

---

### GenerationMetadata Model

**Purpose:** Track AI usage for cost monitoring (FR20)

```typescript
interface GenerationMetadata {
  projectId: string;
  attempts: number; // 1-3
  totalInputTokens: number;
  totalOutputTokens: number;
  totalCostEur: number;
  averageLatencyMs: number;
  modelUsed: 'claude-3.5-sonnet' | 'gpt-4';
  errors: ApiError[];
  completedAt?: Date;
}

interface ApiError {
  timestamp: Date;
  errorCode: string;
  errorMessage: string;
  retryable: boolean;
}
```

---

### ValidationError Model

**Purpose:** Excel validation errors (FR3)

```typescript
interface ValidationError {
  batchId: string;
  rowNumber: number;
  columnName: string;
  errorType: ValidationErrorType;
  errorMessage: string; // Polish
}

enum ValidationErrorType {
  MISSING_REQUIRED = 'missing_required',
  INVALID_TYPE = 'invalid_type',
  MIN_LENGTH = 'min_length',
  INVALID_DATE = 'invalid_date',
  DATE_LOGIC_ERROR = 'date_logic_error'
}
```

---

### ExportHistory Model

**Purpose:** Track Word exports for audit

```typescript
interface ExportHistory {
  id: string;
  projectId: string;
  userId: string;
  fileName: string; // "Projekt-{Name}-{Date}.docx"
  s3Key: string;
  fileSizeBytes: number;
  exportedAt: Date;
  expiresAt: Date; // exportedAt + 30 days
}
```

---

## 5. API Specification

REST API with OpenAPI 3.0, automatic documentation at `/docs`

**Base URL:** `https://api.rnd-cards.example.com/v1`
**Authentication:** Bearer JWT tokens (AWS Cognito)
**WebSocket:** `wss://api.rnd-cards.example.com/ws`

### Core Endpoints

#### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login (returns JWT)
- `GET /auth/me` - Get current user profile
- `POST /auth/refresh` - Refresh JWT token

#### Templates
- `GET /templates/excel` - Download Excel template (.xlsx)

#### Batches
- `GET /batches` - List user's batches (paginated)
- `POST /batches` - Create batch (upload Excel, multipart/form-data)
- `GET /batches/{batchId}` - Get batch with all projects
- `DELETE /batches/{batchId}` - Archive batch
- `POST /batches/{batchId}/generate` - Start AI generation (202 Accepted)

#### Projects
- `GET /projects/{projectId}` - Get project with content
- `PATCH /projects/{projectId}` - Update section content
- `POST /projects/{projectId}/regenerate-section` - Regenerate specific section
- `POST /projects/{projectId}/retry` - Retry failed generation

#### Export
- `GET /export/project/{projectId}` - Download single .docx
- `GET /export/batch/{batchId}` - Download batch as .zip

#### Health
- `GET /health` - Health check with service status

### WebSocket Events

Connect to `wss://api.example.com/ws/{batchId}?token={jwt}`

**Events:**
- `project.status_changed` - Project status update
- `project.progress` - Generation progress %
- `batch.completed` - All projects finished
- `project.error` - Generation error

### Rate Limiting
- **100 requests/minute per user**
- **5 concurrent AI generations**
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`

---

## 6. Components

### Frontend Components

**Core UI Components:**

1. **Dashboard Component**
   - Responsibility: Display recent batches, initiate new batch
   - Key Interfaces: BatchList, BatchCard, NewBatchButton
   - Dependencies: React Query (batch fetching), React Router
   - Tech: React 18, MUI DataGrid, Axios

2. **Upload Component**
   - Responsibility: Excel upload with drag-and-drop, validation display
   - Key Interfaces: FileDropzone, ValidationErrorList
   - Dependencies: react-dropzone, SheetJS, Zod validator
   - Tech: React, MUI, Tailwind

3. **Processing Grid Component**
   - Responsibility: Real-time batch processing visualization
   - Key Interfaces: ProjectStatusCard, ProgressIndicator, WebSocketManager
   - Dependencies: Socket.IO client, React Query
   - Tech: React, MUI Grid, Socket.IO

4. **Review & Edit Component**
   - Responsibility: Section-by-section content review and editing
   - Key Interfaces: SectionEditor (TipTap), QualityScoreBadge, RegenerateButton
   - Dependencies: TipTap editor, React Query mutations
   - Tech: React, TipTap, MUI

5. **Export Component**
   - Responsibility: Single/batch Word export with download
   - Key Interfaces: ExportButton, DownloadProgress
   - Dependencies: Axios (file download)
   - Tech: React, MUI

---

### Backend Components

**Core Backend Services:**

1. **API Server (FastAPI)**
   - Responsibility: REST endpoints, WebSocket server, authentication
   - Key Interfaces: RESTful routes, WebSocket handlers
   - Dependencies: PostgreSQL (SQLAlchemy), Redis, Cognito
   - Tech: FastAPI, Uvicorn, Socket.IO

2. **Celery Worker - AI Generation**
   - Responsibility: Execute AI generation tasks (5 concurrent)
   - Key Interfaces: GenerateProjectTask, AWS Bedrock client, Azure OpenAI client
   - Dependencies: Redis queue, PostgreSQL, S3
   - Tech: Celery, boto3, openai SDK

3. **Celery Worker - Word Export**
   - Responsibility: Generate .docx files from ProjectContent
   - Key Interfaces: ExportProjectTask, python-docx
   - Dependencies: PostgreSQL, S3
   - Tech: Celery, python-docx

4. **Repository Layer**
   - Responsibility: Abstract database access
   - Key Interfaces: UserRepository, BatchRepository, ProjectRepository
   - Dependencies: PostgreSQL
   - Tech: SQLAlchemy ORM, async sessions

5. **AI Service Layer**
   - Responsibility: Orchestrate multi-stage AI generation with circuit breaker
   - Key Interfaces: AIGenerationService, PromptBuilder, QualityScorer
   - Dependencies: AWS Bedrock, Azure OpenAI
   - Tech: boto3, openai SDK, retry logic

6. **Validation Service**
   - Responsibility: Excel validation, Polish grammar checking
   - Key Interfaces: ExcelValidator, LanguageToolClient
   - Dependencies: openpyxl, LanguageTool API
   - Tech: Python, Pydantic, LanguageTool

---

### Component Diagram

```mermaid
graph TB
    subgraph "Frontend Components"
        DASHBOARD[Dashboard]
        UPLOAD[Upload]
        PROCESSING[Processing Grid]
        REVIEW[Review & Edit]
        EXPORT[Export]
    end

    subgraph "API Layer"
        FASTAPI[FastAPI Server<br/>REST + WebSocket]
    end

    subgraph "Worker Layer"
        CELERY_AI[Celery Worker<br/>AI Generation]
        CELERY_EXPORT[Celery Worker<br/>Word Export]
    end

    subgraph "Service Layer"
        AI_SERVICE[AI Service<br/>Bedrock/Azure]
        VALIDATION[Validation Service]
        REPO[Repository Layer]
    end

    subgraph "Data Layer"
        POSTGRES[(PostgreSQL)]
        REDIS[(Redis)]
        S3[(S3)]
    end

    DASHBOARD -->|API Calls| FASTAPI
    UPLOAD -->|Upload Excel| FASTAPI
    PROCESSING -->|WebSocket| FASTAPI
    REVIEW -->|Edit Content| FASTAPI
    EXPORT -->|Download| FASTAPI

    FASTAPI -->|Queue Tasks| REDIS
    FASTAPI -->|CRUD| REPO
    FASTAPI -->|Validate| VALIDATION

    CELERY_AI -->|Poll| REDIS
    CELERY_AI -->|Generate| AI_SERVICE
    CELERY_AI -->|Update| REPO

    CELERY_EXPORT -->|Poll| REDIS
    CELERY_EXPORT -->|Create .docx| S3

    REPO -->|Query| POSTGRES
    AI_SERVICE -->|Store| S3
```

---

## 7. External APIs

### AWS Bedrock (Claude 3.5 Sonnet)

- **Purpose:** Primary AI engine for Polish project card generation
- **Documentation:** https://docs.aws.amazon.com/bedrock/
- **Base URL:** `bedrock-runtime.eu-central-1.amazonaws.com`
- **Authentication:** AWS IAM credentials (via boto3)
- **Rate Limits:** 5 concurrent requests (application-enforced)

**Key Endpoints:**
- `POST /model/anthropic.claude-3-5-sonnet-20241022-v2:0/invoke` - Generate text

**Integration Notes:**
- Use boto3 SDK with exponential backoff retry
- Context window: 200K tokens
- Temperature: 0.5 for balanced creativity/consistency
- Cost: ~€0.10-0.14 per project card

---

### Azure OpenAI Service (GPT-4)

- **Purpose:** Failover AI engine when Bedrock unavailable
- **Documentation:** https://learn.microsoft.com/azure/ai-services/openai/
- **Base URL:** `https://westeurope.api.cognitive.microsoft.com/openai/deployments/`
- **Authentication:** API key
- **Rate Limits:** 10 requests/minute

**Key Endpoints:**
- `POST /{deployment-id}/chat/completions` - Generate chat completion

**Integration Notes:**
- Only used when Bedrock fails 3 consecutive times (circuit breaker)
- Automatic fallback, transparent to user
- Cost: ~€0.12-0.16 per project card (slightly higher than Claude)

---

### LanguageTool API

- **Purpose:** Polish grammar checking for quality scoring
- **Documentation:** https://languagetool.org/http-api/
- **Base URL:** `https://api.languagetool.org/v2/`
- **Authentication:** API key (or self-hosted)
- **Rate Limits:** 20 requests/minute (free tier)

**Key Endpoints:**
- `POST /check` - Check text for grammar/style errors

**Integration Notes:**
- Language: `pl-PL`
- Used asynchronously during quality scoring
- Consider self-hosted instance for production (no rate limits)

---

### Amazon SES

- **Purpose:** Transactional emails (password reset, notifications)
- **Documentation:** https://docs.aws.amazon.com/ses/
- **Authentication:** AWS IAM
- **Rate Limits:** 14 emails/second (verified account)

**Key Operations:**
- Send password reset emails
- Send batch completion notifications (optional future feature)

**Integration Notes:**
- Requires email verification for sender address
- Use templates for consistent branding

---

## 8. Core Workflows

### Workflow 1: Complete Batch Processing Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant API
    participant Redis
    participant Worker
    participant Bedrock
    participant S3
    participant DB

    User->>Frontend: Upload Excel file
    Frontend->>Frontend: Parse Excel (SheetJS)
    Frontend->>API: POST /batches (multipart)
    API->>API: Validate Excel data
    alt Validation Failed
        API->>Frontend: 400 + ValidationErrors
        Frontend->>User: Display errors + template link
    else Validation Success
        API->>DB: Create Batch + Projects
        API->>Frontend: 201 Batch Created
        Frontend->>User: Show validation success

        User->>Frontend: Click "Start Generation"
        Frontend->>API: POST /batches/{id}/generate
        API->>Redis: Queue 5 projects (parallel)
        API->>Frontend: 202 Accepted

        Frontend->>API: Connect WebSocket

        loop For each project (5 concurrent)
            Worker->>Redis: Poll task
            Worker->>DB: Update status=GENERATING
            Worker->>API: Emit project.status_changed
            API->>Frontend: WebSocket event
            Frontend->>User: Show "Generowanie..."

            Worker->>Bedrock: Generate sections (multi-stage)
            Bedrock->>Worker: Polish content
            Worker->>DB: Store content, calculate quality
            Worker->>DB: Update status=COMPLETED
            Worker->>API: Emit project.completed
            API->>Frontend: WebSocket event
            Frontend->>User: Show "Gotowe" + quality score
        end

        User->>Frontend: Click project to review
        Frontend->>API: GET /projects/{id}
        API->>DB: Fetch project + content
        API->>Frontend: Project data
        Frontend->>User: Display 8 sections with editor

        User->>Frontend: Edit section text
        Frontend->>API: PATCH /projects/{id}
        API->>DB: Update section, recalc quality
        API->>Frontend: Updated project
        Frontend->>User: Yellow → White, new score

        User->>Frontend: Click "Pobierz"
        Frontend->>API: GET /export/project/{id}
        API->>Worker: Queue export task
        Worker->>Worker: Generate .docx (python-docx)
        Worker->>S3: Upload file
        Worker->>DB: Create ExportHistory
        API->>Frontend: Stream .docx file
        Frontend->>User: Browser download
    end
```

---

### Workflow 2: AI Generation with Failover

```mermaid
sequenceDiagram
    participant Worker
    participant AIService
    participant Bedrock
    participant Azure
    participant DB

    Worker->>AIService: generate_project_card(project)
    AIService->>AIService: Build multi-stage prompt

    loop Attempt 1-3
        AIService->>Bedrock: Invoke Claude 3.5 Sonnet
        alt Bedrock Success
            Bedrock->>AIService: Generated content
            AIService->>AIService: Validate output
            AIService->>DB: Log tokens, cost
            AIService->>Worker: Return content
        else Bedrock Fails (timeout/rate limit)
            Bedrock->>AIService: Error
            AIService->>AIService: Increment failure count

            alt Failure count < 3
                AIService->>AIService: Wait (exponential backoff)
            else Failure count >= 3 (Circuit Open)
                AIService->>Azure: Fallback to GPT-4
                Azure->>AIService: Generated content
                AIService->>DB: Log fallback, tokens
                AIService->>Worker: Return content
            end
        end
    end

    alt All attempts failed
        AIService->>DB: Log error
        AIService->>Worker: Raise exception
        Worker->>DB: Update project status=FAILED
    end
```

---

### Workflow 3: Real-Time Status Updates

```mermaid
sequenceDiagram
    participant Frontend
    participant API
    participant Redis
    participant Worker
    participant DB

    Frontend->>API: Connect WebSocket /ws/{batchId}?token=jwt
    API->>API: Validate JWT
    API->>API: Join room: batch_{batchId}
    API->>Frontend: Connection established

    loop Every 2 seconds
        Worker->>DB: Update project status/progress
        Worker->>Redis: Publish event (pub/sub)
        Redis->>API: Broadcast to room
        API->>Frontend: Emit project.status_changed
        Frontend->>Frontend: Update UI (Oczekuje→Generowanie→Gotowe)
    end

    Worker->>DB: Mark batch completed
    Worker->>Redis: Publish batch.completed
    Redis->>API: Broadcast
    API->>Frontend: Emit batch.completed
    Frontend->>Frontend: Show success notification
```

---

## 9. Database Schema

PostgreSQL 15+ with JSONB for semi-structured data.

### SQL Schema (DDL)

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    cognito_sub VARCHAR(255) UNIQUE NOT NULL, -- AWS Cognito user ID
    preferences JSONB NOT NULL DEFAULT '{"defaultAiModel": "claude", "language": "pl", "notificationsEnabled": true}',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_cognito_sub ON users(cognito_sub);

-- Batches table
CREATE TABLE batches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'uploading',
    total_projects INTEGER NOT NULL CHECK (total_projects BETWEEN 1 AND 20),
    completed_projects INTEGER NOT NULL DEFAULT 0,
    average_quality_score DECIMAL(5,2) DEFAULT 0 CHECK (average_quality_score BETWEEN 0 AND 100),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL, -- created_at + 90 days
    CONSTRAINT valid_status CHECK (status IN ('uploading', 'validating', 'validation_failed', 'queued', 'processing', 'completed', 'partially_completed', 'archived'))
);

CREATE INDEX idx_batches_user_id ON batches(user_id);
CREATE INDEX idx_batches_status ON batches(status);
CREATE INDEX idx_batches_created_at ON batches(created_at DESC);
CREATE INDEX idx_batches_expires_at ON batches(expires_at);

-- Projects table
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    batch_id UUID NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL CHECK (row_number BETWEEN 1 AND 20),
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    quality_score DECIMAL(5,2) DEFAULT 0 CHECK (quality_score BETWEEN 0 AND 100),
    input_data JSONB NOT NULL, -- ProjectInputData
    ai_model VARCHAR(50) DEFAULT 'claude-3.5-sonnet',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    generated_at TIMESTAMP WITH TIME ZONE,
    edited_at TIMESTAMP WITH TIME ZONE,
    CONSTRAINT valid_project_status CHECK (status IN ('pending', 'generating', 'completed', 'failed', 'reviewed', 'exported')),
    UNIQUE(batch_id, row_number)
);

CREATE INDEX idx_projects_batch_id ON projects(batch_id);
CREATE INDEX idx_projects_status ON projects(status);

-- Project content table (1:1 with projects)
CREATE TABLE project_contents (
    project_id UUID PRIMARY KEY REFERENCES projects(id) ON DELETE CASCADE,
    sections JSONB NOT NULL, -- Record<SectionKey, SectionContent>
    version INTEGER NOT NULL DEFAULT 1,
    last_edited_section VARCHAR(50)
);

-- Generation metadata table (1:1 with projects)
CREATE TABLE generation_metadata (
    project_id UUID PRIMARY KEY REFERENCES projects(id) ON DELETE CASCADE,
    attempts INTEGER NOT NULL DEFAULT 1 CHECK (attempts BETWEEN 1 AND 3),
    total_input_tokens INTEGER NOT NULL DEFAULT 0,
    total_output_tokens INTEGER NOT NULL DEFAULT 0,
    total_cost_eur DECIMAL(10,4) NOT NULL DEFAULT 0,
    average_latency_ms INTEGER,
    model_used VARCHAR(50) NOT NULL,
    errors JSONB DEFAULT '[]', -- Array of ApiError
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Validation errors table
CREATE TABLE validation_errors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    batch_id UUID NOT NULL REFERENCES batches(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL,
    column_name VARCHAR(100) NOT NULL,
    error_type VARCHAR(50) NOT NULL,
    error_message TEXT NOT NULL,
    CONSTRAINT valid_error_type CHECK (error_type IN ('missing_required', 'invalid_type', 'min_length', 'max_length', 'invalid_date', 'date_logic_error'))
);

CREATE INDEX idx_validation_errors_batch_id ON validation_errors(batch_id);

-- Export history table
CREATE TABLE export_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    s3_key VARCHAR(500) NOT NULL,
    file_size_bytes INTEGER NOT NULL,
    exported_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL -- exported_at + 30 days
);

CREATE INDEX idx_export_history_project_id ON export_history(project_id);
CREATE INDEX idx_export_history_user_id ON export_history(user_id);
CREATE INDEX idx_export_history_expires_at ON export_history(expires_at);

-- Trigger to update batch average quality score
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

CREATE TRIGGER trigger_update_batch_quality
AFTER UPDATE OF quality_score, status ON projects
FOR EACH ROW
EXECUTE FUNCTION update_batch_quality_score();
```

---

### Data Access Patterns

**Optimized Queries:**

1. **Dashboard - Recent Batches:**
```sql
SELECT id, name, status, total_projects, completed_projects, average_quality_score, created_at
FROM batches
WHERE user_id = $1 AND status != 'archived'
ORDER BY created_at DESC
LIMIT 10;
```

2. **Batch Detail - All Projects:**
```sql
SELECT p.*, pc.sections, gm.total_cost_eur
FROM projects p
LEFT JOIN project_contents pc ON p.id = pc.project_id
LEFT JOIN generation_metadata gm ON p.id = gm.project_id
WHERE p.batch_id = $1
ORDER BY p.row_number ASC;
```

3. **Cost Tracking - Monthly Spend:**
```sql
SELECT
    DATE_TRUNC('day', created_at) as date,
    COUNT(*) as projects_generated,
    SUM(total_cost_eur) as total_cost
FROM generation_metadata
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY date DESC;
```

---

## 10. Frontend Architecture

### 10.1 Component Architecture

**Organization:** Atomic Design pattern

```
apps/web/src/
├── components/
│   ├── atoms/              # Basic building blocks
│   │   ├── Button/
│   │   ├── Input/
│   │   ├── Badge/
│   │   └── Spinner/
│   ├── molecules/          # Simple component groups
│   │   ├── ProjectCard/
│   │   ├── QualityScoreBadge/
│   │   ├── FileUploadZone/
│   │   └── SectionEditor/
│   ├── organisms/          # Complex components
│   │   ├── BatchGrid/
│   │   ├── ProjectList/
│   │   ├── ReviewPanel/
│   │   └── NavigationBar/
│   └── templates/          # Page layouts
│       ├── DashboardLayout/
│       └── AuthLayout/
├── pages/                  # Route components
│   ├── Dashboard/
│   ├── Upload/
│   ├── Processing/
│   ├── Review/
│   └── Login/
├── hooks/                  # Custom React hooks
│   ├── useAuth.ts
│   ├── useBatch.ts
│   ├── useWebSocket.ts
│   └── useProjects.ts
├── services/               # API client
│   ├── api.ts             # Axios instance
│   ├── batches.ts
│   ├── projects.ts
│   └── auth.ts
├── stores/                 # Global state (minimal)
│   └── authStore.ts       # Auth context only
├── styles/                 # Global styles
│   ├── theme.ts           # MUI iNOV theme
│   └── globals.css
└── utils/                  # Utilities
    ├── formatters.ts
    └── validators.ts
```

**Component Template Example:**

```typescript
// apps/web/src/components/molecules/QualityScoreBadge/QualityScoreBadge.tsx
import { Badge } from '@mui/material';
import { FC } from 'react';

interface QualityScoreBadgeProps {
  score: number; // 0-100
  size?: 'small' | 'medium' | 'large';
}

export const QualityScoreBadge: FC<QualityScoreBadgeProps> = ({
  score,
  size = 'medium'
}) => {
  const getColor = (score: number) => {
    if (score < 50) return 'error';
    if (score < 70) return 'warning';
    return 'success';
  };

  return (
    <Badge
      badgeContent={`${Math.round(score)}%`}
      color={getColor(score)}
      sx={{
        fontSize: size === 'large' ? '1.2rem' : '0.875rem',
        fontWeight: 600
      }}
    />
  );
};
```

---

### 10.2 State Management Architecture

**State Structure:**

```typescript
// Global State (React Context)
interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

// Server State (React Query)
// Managed automatically by React Query hooks

// Local Component State
// Managed by useState/useReducer within components
```

**State Management Patterns:**

1. **Authentication:** React Context (`AuthProvider`)
2. **Server Data:** React Query (batches, projects, API calls)
3. **WebSocket State:** Custom `useWebSocket` hook with React Query integration
4. **Form State:** React Hook Form with Zod validation
5. **UI State:** Local component state (modals, drawers, etc.)

---

### 10.3 Routing Architecture

**Route Organization:**

```typescript
// apps/web/src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public routes */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />

        {/* Protected routes */}
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/batches/new" element={<UploadPage />} />
          <Route path="/batches/:batchId/processing" element={<ProcessingPage />} />
          <Route path="/batches/:batchId/review" element={<ReviewPage />} />
          <Route path="/batches/:batchId/review/:projectId" element={<ProjectReviewPage />} />
        </Route>

        {/* 404 */}
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  );
}
```

**Protected Route Pattern:**

```typescript
// apps/web/src/components/ProtectedRoute.tsx
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';

export const ProtectedRoute = () => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
};
```

---

### 10.4 Frontend Services Layer

**API Client Setup:**

```typescript
// apps/web/src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/v1',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor (add JWT token)
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor (handle errors)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired, redirect to login
      localStorage.removeItem('auth_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

**Service Example:**

```typescript
// apps/web/src/services/batches.ts
import api from './api';
import { Batch, Project } from '@shared/types';

export const batchesService = {
  async list(limit = 10, offset = 0): Promise<{ batches: Batch[]; total: number }> {
    const { data } = await api.get('/batches', { params: { limit, offset } });
    return data;
  },

  async create(file: File, name: string): Promise<Batch> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('name', name);

    const { data } = await api.post('/batches', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return data;
  },

  async get(batchId: string): Promise<Batch & { projects: Project[] }> {
    const { data } = await api.get(`/batches/${batchId}`);
    return data;
  },

  async startGeneration(batchId: string): Promise<void> {
    await api.post(`/batches/${batchId}/generate`);
  },

  async delete(batchId: string): Promise<void> {
    await api.delete(`/batches/${batchId}`);
  }
};
```

---

## 11. Backend Architecture

### 11.1 Service Architecture (FastAPI)

**Project Structure:**

```
apps/api/src/
├── main.py                 # FastAPI app entry point
├── config.py               # Environment configuration
├── routes/                 # API route handlers
│   ├── __init__.py
│   ├── auth.py
│   ├── batches.py
│   ├── projects.py
│   ├── templates.py
│   └── export.py
├── services/               # Business logic
│   ├── ai_service.py       # AI generation orchestration
│   ├── validation_service.py
│   ├── export_service.py
│   └── quality_service.py
├── repositories/           # Data access layer
│   ├── user_repository.py
│   ├── batch_repository.py
│   └── project_repository.py
├── models/                 # SQLAlchemy ORM models
│   ├── user.py
│   ├── batch.py
│   └── project.py
├── schemas/                # Pydantic schemas (validation)
│   ├── user.py
│   ├── batch.py
│   └── project.py
├── workers/                # Celery tasks
│   ├── celery_app.py
│   ├── ai_generation_task.py
│   └── export_task.py
├── middleware/             # Custom middleware
│   ├── auth.py
│   ├── rate_limit.py
│   └── error_handler.py
└── utils/                  # Utilities
    ├── logger.py
    ├── s3_client.py
    └── websocket_manager.py
```

---

**FastAPI Entry Point:**

```python
# apps/api/src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socketio import ASGIApp, AsyncServer

from .routes import auth, batches, projects, templates, export
from .middleware import error_handler, rate_limit
from .config import settings

app = FastAPI(
    title="R&D Tax Relief API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Custom middleware
app.add_middleware(error_handler.ErrorHandlerMiddleware)
app.add_middleware(rate_limit.RateLimitMiddleware)

# Register routes
app.include_router(auth.router, prefix="/v1/auth", tags=["auth"])
app.include_router(batches.router, prefix="/v1/batches", tags=["batches"])
app.include_router(projects.router, prefix="/v1/projects", tags=["projects"])
app.include_router(templates.router, prefix="/v1/templates", tags=["templates"])
app.include_router(export.router, prefix="/v1/export", tags=["export"])

# WebSocket server
sio = AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = ASGIApp(sio, app)

@sio.event
async def connect(sid, environ, auth):
    # Validate JWT token from query params
    token = auth.get('token')
    # ... validate token, join batch room
    pass

@sio.event
async def disconnect(sid):
    pass

# Health check
@app.get("/health")
async def health():
    return {"status": "healthy", "version": "1.0.0"}
```

---

### 11.2 Database Architecture

**Repository Pattern:**

```python
# apps/api/src/repositories/batch_repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from typing import List, Optional
from uuid import UUID

from ..models.batch import Batch

class BatchRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_id: UUID, name: str, total_projects: int) -> Batch:
        batch = Batch(
            user_id=user_id,
            name=name,
            total_projects=total_projects
        )
        self.session.add(batch)
        await self.session.commit()
        await self.session.refresh(batch)
        return batch

    async def get_by_id(self, batch_id: UUID) -> Optional[Batch]:
        result = await self.session.execute(
            select(Batch).where(Batch.id == batch_id)
        )
        return result.scalar_one_or_none()

    async def list_by_user(
        self,
        user_id: UUID,
        limit: int = 10,
        offset: int = 0
    ) -> List[Batch]:
        result = await self.session.execute(
            select(Batch)
            .where(Batch.user_id == user_id, Batch.status != 'archived')
            .order_by(Batch.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return result.scalars().all()

    async def update_status(self, batch_id: UUID, status: str) -> None:
        await self.session.execute(
            update(Batch)
            .where(Batch.id == batch_id)
            .values(status=status)
        )
        await self.session.commit()
```

---

### 11.3 Authentication and Authorization

**AWS Cognito Integration:**

```python
# apps/api/src/middleware/auth.py
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import requests

from ..config import settings

security = HTTPBearer()

async def verify_jwt_token(credentials: HTTPAuthCredentials = Depends(security)) -> dict:
    token = credentials.credentials

    # Get Cognito public keys
    jwks_url = f"https://cognito-idp.{settings.AWS_REGION}.amazonaws.com/{settings.COGNITO_USER_POOL_ID}/.well-known/jwks.json"
    jwks = requests.get(jwks_url).json()

    try:
        # Decode and verify token
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                audience=settings.COGNITO_CLIENT_ID,
                issuer=f"https://cognito-idp.{settings.AWS_REGION}.amazonaws.com/{settings.COGNITO_USER_POOL_ID}"
            )
            return payload
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail="Invalid claims")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

async def get_current_user(token_payload: dict = Depends(verify_jwt_token)) -> str:
    return token_payload["sub"]  # Cognito user ID
```

**Auth Flow Diagram:**

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant API
    participant Cognito

    User->>Frontend: Enter email/password
    Frontend->>Cognito: Authenticate (SDK)
    Cognito->>Frontend: JWT token
    Frontend->>Frontend: Store token (localStorage)

    Frontend->>API: Request with Bearer token
    API->>API: Extract token from header
    API->>Cognito: Fetch JWKS (public keys)
    Cognito->>API: Public keys
    API->>API: Verify signature + claims

    alt Token Valid
        API->>API: Extract user ID
        API->>Frontend: Process request
    else Token Invalid/Expired
        API->>Frontend: 401 Unauthorized
        Frontend->>User: Redirect to /login
    end
```

---

## 12. Unified Project Structure

Full monorepo structure with all packages:

```
rnd-tax-relief-generator/
├── .github/
│   └── workflows/
│       ├── ci.yaml                 # Run tests on PR
│       └── deploy.yaml             # Deploy to AWS
├── apps/
│   ├── web/                        # React frontend
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── atoms/
│   │   │   │   ├── molecules/
│   │   │   │   ├── organisms/
│   │   │   │   └── templates/
│   │   │   ├── pages/
│   │   │   │   ├── Dashboard/
│   │   │   │   ├── Upload/
│   │   │   │   ├── Processing/
│   │   │   │   ├── Review/
│   │   │   │   └── Login/
│   │   │   ├── hooks/
│   │   │   ├── services/
│   │   │   ├── stores/
│   │   │   ├── styles/
│   │   │   ├── utils/
│   │   │   ├── App.tsx
│   │   │   └── main.tsx
│   │   ├── public/
│   │   ├── tests/
│   │   ├── index.html
│   │   ├── vite.config.ts
│   │   ├── tsconfig.json
│   │   └── package.json
│   └── api/                        # FastAPI backend
│       ├── src/
│       │   ├── routes/
│       │   ├── services/
│       │   ├── repositories/
│       │   ├── models/
│       │   ├── schemas/
│       │   ├── workers/
│       │   │   ├── celery_app.py
│       │   │   ├── ai_generation_task.py
│       │   │   └── export_task.py
│       │   ├── middleware/
│       │   ├── utils/
│       │   ├── main.py
│       │   └── config.py
│       ├── tests/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── pyproject.toml
├── packages/
│   ├── shared/                     # Shared TypeScript types
│   │   ├── src/
│   │   │   ├── types/
│   │   │   │   ├── user.ts
│   │   │   │   ├── batch.ts
│   │   │   │   ├── project.ts
│   │   │   │   └── index.ts
│   │   │   └── constants/
│   │   ├── tsconfig.json
│   │   └── package.json
│   └── config/                     # Shared configs
│       ├── eslint/
│       ├── typescript/
│       └── jest/
├── infrastructure/                 # AWS CDK
│   ├── lib/
│   │   ├── database-stack.ts
│   │   ├── api-stack.ts
│   │   ├── frontend-stack.ts
│   │   └── monitoring-stack.ts
│   ├── bin/
│   │   └── app.ts
│   ├── cdk.json
│   └── tsconfig.json
├── scripts/                        # Build/deploy scripts
│   ├── deploy.sh
│   └── local-dev.sh
├── docs/                          # Documentation
│   ├── prd.md
│   ├── architecture.md
│   ├── front-end-spec.md
│   └── api-docs.md
├── .env.example
├── .gitignore
├── package.json                   # Root package.json
├── tsconfig.json                  # Root TypeScript config
└── README.md
```

---

## 13. Development Workflow

### 13.1 Local Development Setup

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

### 13.2 Environment Configuration

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

## 14. Deployment Architecture

### 14.1 Deployment Strategy

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

### 14.2 CI/CD Pipeline

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

### 14.3 Environments

| Environment | Frontend URL | Backend URL | Purpose |
|-------------|-------------|-------------|---------|
| **Development** | http://localhost:5173 | http://localhost:8000 | Local development |
| **Staging** | https://staging.rnd-cards.example.com | https://staging-api.rnd-cards.example.com | Pre-production testing |
| **Production** | https://rnd-cards.example.com | https://api.rnd-cards.example.com | Live environment |

---

## 15. Security and Performance

### 15.1 Security Requirements

**Frontend Security:**
- **CSP Headers:** `default-src 'self'; script-src 'self' 'unsafe-inline'; connect-src 'self' https://api.rnd-cards.example.com wss://api.rnd-cards.example.com`
- **XSS Prevention:** React auto-escaping, DOMPurify for rich text editor
- **Secure Storage:** JWT in httpOnly cookies (not localStorage for production)

**Backend Security:**
- **Input Validation:** Pydantic schemas for all API inputs, SQL injection prevention via ORM
- **Rate Limiting:** 100 requests/minute per user, 5 concurrent AI generations
- **CORS Policy:** Allow only frontend domain

**Authentication Security:**
- **Token Storage:** JWT tokens with 24-hour expiry, refresh tokens with 7-day expiry
- **Session Management:** Cognito-managed sessions
- **Password Policy:** Min 8 chars, 1 uppercase, 1 number (enforced by Cognito)

---

### 15.2 Rate Limiting Implementation

**Architecture:** Redis-based sliding window algorithm

**Implementation:**

```python
# apps/api/src/middleware/rate_limit.py
from fastapi import Request, HTTPException
from redis.asyncio import Redis
import time

class RateLimiter:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def check_rate_limit(
        self,
        user_id: str,
        limit: int = 100,
        window: int = 60  # seconds
    ) -> bool:
        """Sliding window rate limiter"""
        key = f"rate_limit:{user_id}"
        now = time.time()

        # Remove requests older than window
        await self.redis.zremrangebyscore(key, 0, now - window)

        # Count requests in current window
        current_count = await self.redis.zcard(key)

        if current_count >= limit:
            # Get oldest request timestamp
            oldest = await self.redis.zrange(key, 0, 0, withscores=True)
            if oldest:
                reset_time = int(oldest[0][1] + window)
                raise HTTPException(
                    status_code=429,
                    detail={
                        "error": "Rate limit exceeded",
                        "retryAfter": reset_time,
                        "limit": limit,
                        "window": window
                    },
                    headers={
                        "X-RateLimit-Limit": str(limit),
                        "X-RateLimit-Remaining": "0",
                        "X-RateLimit-Reset": str(reset_time),
                        "Retry-After": str(int(reset_time - now))
                    }
                )

        # Add current request
        await self.redis.zadd(key, {str(now): now})
        await self.redis.expire(key, window)

        return True

# Middleware implementation
from fastapi import Depends

async def rate_limit_middleware(
    request: Request,
    user_id: str = Depends(get_current_user)
):
    limiter = RateLimiter(request.app.state.redis)
    await limiter.check_rate_limit(user_id, limit=100, window=60)
```

**AI Generation Rate Limiting:**

```python
# apps/api/src/middleware/ai_rate_limit.py
async def ai_generation_limiter(user_id: str, redis: Redis) -> bool:
    """Limit concurrent AI generations to 5 per user"""
    key = f"ai_concurrent:{user_id}"
    current = await redis.get(key)

    if current and int(current) >= 5:
        raise HTTPException(
            status_code=429,
            detail={
                "error": "Maximum 5 concurrent AI generations exceeded",
                "message": "Poczekaj na zakończenie bieżących generacji"
            }
        )

    await redis.incr(key)
    await redis.expire(key, 3600)  # 1 hour max
    return True

# Decrement when generation completes
async def release_ai_slot(user_id: str, redis: Redis):
    key = f"ai_concurrent:{user_id}"
    await redis.decr(key)
```

**Rate Limit Headers (FastAPI Middleware):**

```python
# apps/api/src/middleware/rate_limit.py
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if hasattr(request.state, 'user_id'):
            user_id = request.state.user_id
            redis = request.app.state.redis

            # Get current usage
            key = f"rate_limit:{user_id}"
            count = await redis.zcard(key)

            response.headers["X-RateLimit-Limit"] = "100"
            response.headers["X-RateLimit-Remaining"] = str(max(0, 100 - count))
            response.headers["X-RateLimit-Reset"] = str(int(time.time() + 60))

        return response
```

---

### 15.3 Input Validation Architecture

**Pydantic Schema Examples:**

```python
# apps/api/src/schemas/batch.py
from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class ProjectInputDataSchema(BaseModel):
    """Validation for Excel row data"""
    nazwaProjektu: str = Field(..., min_length=1, max_length=255)
    opis: str = Field(..., min_length=100, max_length=5000)
    dataRozpoczecia: date
    dataZakonczenia: date
    celProjektu: str = Field(..., min_length=50, max_length=2000)
    osobaOdpowiedzialna: str = Field(..., min_length=1, max_length=255)

    @validator('dataZakonczenia')
    def validate_end_date(cls, v, values):
        if 'dataRozpoczecia' in values and v < values['dataRozpoczecia']:
            raise ValueError('Data zakończenia musi być późniejsza niż data rozpoczęcia')
        return v

    @validator('nazwaProjektu', 'opis', 'celProjektu')
    def sanitize_text(cls, v):
        """Remove potentially dangerous characters"""
        # Strip HTML tags
        import re
        v = re.sub(r'<[^>]+>', '', v)
        # Remove null bytes
        v = v.replace('\x00', '')
        return v.strip()

class BatchCreateSchema(BaseModel):
    """Validation for batch creation"""
    name: str = Field(..., min_length=1, max_length=255)
    # File validation happens in route handler

    @validator('name')
    def sanitize_name(cls, v):
        import re
        # Remove special characters that could cause filesystem issues
        v = re.sub(r'[<>:"/\\|?*]', '', v)
        return v.strip()

class ProjectRegenerateSchema(BaseModel):
    """Validation for section regeneration"""
    sectionKey: str = Field(..., regex=r'^(nazwa_projektu|cel_projektu|opis_projektu|nowatorstwo|metodologia|rezultaty|koszty|harmonogram)$')
    hints: Optional[str] = Field(None, max_length=1000)
    aiModel: str = Field(default='claude', regex=r'^(claude|gpt4)$')

    @validator('hints')
    def sanitize_hints(cls, v):
        if v:
            # Remove potential prompt injection attempts
            forbidden = ['ignore previous', 'disregard', 'system:', 'assistant:']
            v_lower = v.lower()
            for phrase in forbidden:
                if phrase in v_lower:
                    raise ValueError('Niedozwolone frazy w hints')
        return v
```

**Excel Upload Validation:**

```python
# apps/api/src/services/validation_service.py
import openpyxl
from typing import List
from ..schemas.batch import ProjectInputDataSchema, ValidationError

class ExcelValidationService:
    REQUIRED_COLUMNS = [
        'Nazwa projektu',
        'Opis',
        'Data rozpoczęcia',
        'Data zakończenia',
        'Cel projektu',
        'Osoba odpowiedzialna'
    ]

    async def validate_excel(self, file_path: str) -> List[ValidationError]:
        errors = []

        try:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active

            # Validate headers
            headers = [cell.value for cell in ws[1]]
            missing_cols = set(self.REQUIRED_COLUMNS) - set(headers)
            if missing_cols:
                errors.append(ValidationError(
                    rowNumber=0,
                    columnName=', '.join(missing_cols),
                    errorType='missing_required',
                    errorMessage=f'Brakujące kolumny: {", ".join(missing_cols)}'
                ))
                return errors

            # Validate rows (max 20)
            row_count = ws.max_row - 1  # Exclude header
            if row_count > 20:
                errors.append(ValidationError(
                    rowNumber=0,
                    columnName='',
                    errorType='max_length',
                    errorMessage=f'Maksymalnie 20 projektów na plik (znaleziono {row_count})'
                ))
                return errors

            # Validate each row
            for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
                row_data = dict(zip(headers, row))

                try:
                    ProjectInputDataSchema(
                        nazwaProjektu=row_data.get('Nazwa projektu'),
                        opis=row_data.get('Opis'),
                        dataRozpoczecia=row_data.get('Data rozpoczęcia'),
                        dataZakonczenia=row_data.get('Data zakończenia'),
                        celProjektu=row_data.get('Cel projektu'),
                        osobaOdpowiedzialna=row_data.get('Osoba odpowiedzialna')
                    )
                except ValueError as e:
                    errors.append(ValidationError(
                        rowNumber=idx,
                        columnName=str(e.__cause__) if e.__cause__ else '',
                        errorType='invalid_type',
                        errorMessage=str(e)
                    ))

        except Exception as e:
            errors.append(ValidationError(
                rowNumber=0,
                columnName='',
                errorType='invalid_type',
                errorMessage=f'Nie można odczytać pliku Excel: {str(e)}'
            ))

        return errors
```

**SQL Injection Prevention (SQLAlchemy ORM):**

```python
# apps/api/src/repositories/batch_repository.py
# CORRECT - Using ORM (safe)
async def get_batches_by_status(self, user_id: str, status: str):
    result = await self.session.execute(
        select(Batch)
        .where(Batch.user_id == user_id)
        .where(Batch.status == status)  # Parameterized
    )
    return result.scalars().all()

# NEVER DO THIS - Raw SQL with string interpolation (vulnerable)
# query = f"SELECT * FROM batches WHERE user_id = '{user_id}' AND status = '{status}'"
```

---

### 15.4 Network Security Architecture

**AWS VPC Design:**

```
AWS VPC (10.0.0.0/16) - EU-Central-1
│
├── Public Subnets (10.0.1.0/24, 10.0.2.0/24)
│   ├── Application Load Balancer (ALB)
│   │   └── Security Group: sg-alb
│   │       - Inbound: 443 (0.0.0.0/0), 80 (0.0.0.0/0)
│   │       - Outbound: All to ECS security group
│   └── NAT Gateway (for private subnet internet access)
│
├── Private Subnets - App Tier (10.0.10.0/24, 10.0.11.0/24)
│   ├── ECS Fargate Tasks (API + Workers)
│   │   └── Security Group: sg-ecs-tasks
│   │       - Inbound: 8000 from ALB security group
│   │       - Outbound: 443 (AWS APIs), 5432 (RDS), 6379 (Redis)
│   │
│   └── Network ACL (Stateless firewall)
│       - Inbound: 8000, 1024-65535 (ephemeral)
│       - Outbound: All
│
└── Private Subnets - Data Tier (10.0.20.0/24, 10.0.21.0/24)
    ├── RDS PostgreSQL
    │   └── Security Group: sg-rds
    │       - Inbound: 5432 from ECS security group
    │       - Outbound: None
    │
    └── ElastiCache Redis
        └── Security Group: sg-redis
            - Inbound: 6379 from ECS security group
            - Outbound: None
```

**Security Group Rules (AWS CDK):**

```typescript
// infrastructure/lib/network-stack.ts
import * as ec2 from 'aws-cdk-lib/aws-ec2';

// ALB Security Group
const albSg = new ec2.SecurityGroup(this, 'AlbSecurityGroup', {
  vpc,
  description: 'ALB security group',
  allowAllOutbound: false
});
albSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(443), 'HTTPS from internet');
albSg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'HTTP from internet (redirect to HTTPS)');

// ECS Tasks Security Group
const ecsSg = new ec2.SecurityGroup(this, 'EcsSecurityGroup', {
  vpc,
  description: 'ECS Fargate tasks security group',
  allowAllOutbound: false
});
ecsSg.addIngressRule(albSg, ec2.Port.tcp(8000), 'HTTP from ALB');
ecsSg.addEgressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(443), 'HTTPS to AWS APIs (Bedrock, S3)');
ecsSg.addEgressRule(rdsSg, ec2.Port.tcp(5432), 'PostgreSQL');
ecsSg.addEgressRule(redisSg, ec2.Port.tcp(6379), 'Redis');

// RDS Security Group
const rdsSg = new ec2.SecurityGroup(this, 'RdsSecurityGroup', {
  vpc,
  description: 'RDS PostgreSQL security group',
  allowAllOutbound: false
});
rdsSg.addIngressRule(ecsSg, ec2.Port.tcp(5432), 'PostgreSQL from ECS');

// Redis Security Group
const redisSg = new ec2.SecurityGroup(this, 'RedisSecurityGroup', {
  vpc,
  description: 'ElastiCache Redis security group',
  allowAllOutbound: false
});
redisSg.addIngressRule(ecsSg, ec2.Port.tcp(6379), 'Redis from ECS');
```

**IAM Policies (Least Privilege):**

```typescript
// infrastructure/lib/iam-stack.ts
import * as iam from 'aws-cdk-lib/aws-iam';

// ECS Task Execution Role (pulls images, writes logs)
const taskExecutionRole = new iam.Role(this, 'EcsTaskExecutionRole', {
  assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com'),
  managedPolicies: [
    iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonECSTaskExecutionRolePolicy')
  ]
});

// ECS Task Role (application permissions)
const taskRole = new iam.Role(this, 'EcsTaskRole', {
  assumedBy: new iam.ServicePrincipal('ecs-tasks.amazonaws.com')
});

// S3 access (read/write to specific bucket only)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: [
    's3:GetObject',
    's3:PutObject',
    's3:DeleteObject'
  ],
  resources: [`arn:aws:s3:::rnd-cards-${env}/*`]
}));

// Bedrock access (specific model only)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['bedrock:InvokeModel'],
  resources: [`arn:aws:bedrock:eu-central-1::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0`]
}));

// Secrets Manager (read database credentials)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['secretsmanager:GetSecretValue'],
  resources: [`arn:aws:secretsmanager:eu-central-1:${account}:secret:rnd-cards-db-*`]
}));

// SES (send emails)
taskRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ['ses:SendEmail', 'ses:SendRawEmail'],
  resources: [`arn:aws:ses:eu-central-1:${account}:identity/*`],
  conditions: {
    StringEquals: {
      'ses:FromAddress': 'noreply@rnd-cards.example.com'
    }
  }
}));
```

**WAF Configuration:**

```typescript
// infrastructure/lib/waf-stack.ts
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';

const webAcl = new wafv2.CfnWebACL(this, 'WebAcl', {
  defaultAction: { allow: {} },
  scope: 'REGIONAL',
  visibilityConfig: {
    cloudWatchMetricsEnabled: true,
    metricName: 'rnd-cards-waf',
    sampledRequestsEnabled: true
  },
  rules: [
    // AWS Managed Rules - Core Rule Set (OWASP Top 10)
    {
      name: 'AWSManagedRulesCommonRuleSet',
      priority: 1,
      statement: {
        managedRuleGroupStatement: {
          vendorName: 'AWS',
          name: 'AWSManagedRulesCommonRuleSet'
        }
      },
      overrideAction: { none: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AWSManagedRulesCommonRuleSetMetric',
        sampledRequestsEnabled: true
      }
    },
    // SQL Injection protection
    {
      name: 'AWSManagedRulesSQLiRuleSet',
      priority: 2,
      statement: {
        managedRuleGroupStatement: {
          vendorName: 'AWS',
          name: 'AWSManagedRulesSQLiRuleSet'
        }
      },
      overrideAction: { none: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AWSManagedRulesSQLiRuleSetMetric',
        sampledRequestsEnabled: true
      }
    },
    // Rate limiting (1000 requests per 5 minutes per IP)
    {
      name: 'RateLimitRule',
      priority: 3,
      statement: {
        rateBasedStatement: {
          limit: 1000,
          aggregateKeyType: 'IP'
        }
      },
      action: { block: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'RateLimitRuleMetric',
        sampledRequestsEnabled: true
      }
    }
  ]
});
```

---

### 15.5 Error Handling & Resilience Patterns

#### Retry Policy Configuration

**Exponential Backoff Strategy:**

```python
# apps/api/src/services/resilience/retry_policy.py
from typing import Callable, TypeVar, Any
import asyncio
import logging

T = TypeVar('T')

class RetryConfig:
    """Retry configuration for external services"""

    # Base delays (seconds) for exponential backoff
    BASE_DELAY = 1.0
    MAX_RETRIES = 3
    MAX_TOTAL_DELAY = 30.0  # Maximum total retry time
    BACKOFF_MULTIPLIER = 4  # Delay multiplies by 4x each retry (1s, 4s, 16s)

    # Service-specific retry configurations
    RETRY_CONFIGS = {
        'bedrock': {
            'max_retries': 3,
            'base_delay': 1.0,
            'retryable_errors': ['ThrottlingException', 'ServiceUnavailableException'],
            'timeout': 180  # 3 minutes per request
        },
        'azure_openai': {
            'max_retries': 3,
            'base_delay': 2.0,
            'retryable_errors': ['RateLimitError', 'APIConnectionError'],
            'timeout': 180
        },
        'database': {
            'max_retries': 3,
            'base_delay': 0.5,
            'retryable_errors': ['OperationalError', 'TimeoutError'],
            'timeout': 10
        },
        's3': {
            'max_retries': 5,
            'base_delay': 0.5,
            'retryable_errors': ['RequestTimeout', 'ServiceUnavailable'],
            'timeout': 60
        }
    }

async def retry_with_backoff(
    func: Callable[..., T],
    service_name: str,
    *args,
    **kwargs
) -> T:
    """
    Execute function with exponential backoff retry logic.

    Args:
        func: Async function to retry
        service_name: Service identifier ('bedrock', 'azure_openai', 'database', 's3')
        *args, **kwargs: Arguments to pass to func

    Returns:
        Result from successful function execution

    Raises:
        Exception: After all retries exhausted
    """
    config = RetryConfig.RETRY_CONFIGS[service_name]
    max_retries = config['max_retries']
    base_delay = config['base_delay']
    retryable_errors = config['retryable_errors']

    logger = logging.getLogger(__name__)

    for attempt in range(max_retries):
        try:
            # Execute with timeout
            return await asyncio.wait_for(
                func(*args, **kwargs),
                timeout=config['timeout']
            )
        except asyncio.TimeoutError as e:
            logger.warning(
                f"{service_name} timeout on attempt {attempt + 1}/{max_retries}",
                extra={'service': service_name, 'attempt': attempt}
            )
            if attempt == max_retries - 1:
                raise Exception(f"Max retries exceeded for {service_name} (timeout)") from e
        except Exception as e:
            error_name = e.__class__.__name__
            is_retryable = any(err in str(e) or err == error_name for err in retryable_errors)

            if not is_retryable or attempt == max_retries - 1:
                logger.error(
                    f"{service_name} non-retryable error or max retries: {error_name}",
                    exc_info=True
                )
                raise

            # Calculate exponential backoff delay
            delay = min(
                base_delay * (RetryConfig.BACKOFF_MULTIPLIER ** attempt),
                RetryConfig.MAX_TOTAL_DELAY
            )

            logger.warning(
                f"{service_name} retryable error on attempt {attempt + 1}/{max_retries}. "
                f"Retrying in {delay}s... Error: {error_name}",
                extra={
                    'service': service_name,
                    'attempt': attempt,
                    'delay': delay,
                    'error': error_name
                }
            )

            await asyncio.sleep(delay)

    raise Exception(f"Retry logic failed for {service_name}")
```

**Usage Example:**

```python
# apps/api/src/services/ai/bedrock_service.py
from services.resilience.retry_policy import retry_with_backoff

class BedrockService:
    async def generate_card(self, prompt: str) -> str:
        """Generate project card with automatic retry"""

        async def _generate():
            response = await self.bedrock_client.invoke_model(
                modelId='anthropic.claude-3-5-sonnet-20241022-v2:0',
                body=json.dumps({
                    'anthropic_version': 'bedrock-2023-05-31',
                    'max_tokens': 4000,
                    'messages': [{'role': 'user', 'content': prompt}]
                })
            )
            return json.loads(response['body'].read())['content'][0]['text']

        # Automatically retries with exponential backoff (1s, 4s, 16s)
        return await retry_with_backoff(_generate, 'bedrock')
```

---

#### Circuit Breaker Implementation

**Circuit Breaker Pattern:**

```python
# apps/api/src/services/resilience/circuit_breaker.py
from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, TypeVar
import asyncio
import logging

T = TypeVar('T')

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, reject requests immediately
    HALF_OPEN = "half_open"  # Testing if service recovered

class CircuitBreaker:
    """
    Circuit breaker for AI services to prevent cascading failures.

    States:
    - CLOSED: Normal operation, requests pass through
    - OPEN: Too many failures, reject requests immediately (return fallback)
    - HALF_OPEN: After reset timeout, allow 1 test request

    Configuration:
    - Failure threshold: 3 consecutive failures → OPEN
    - Reset timeout: 60 seconds in OPEN before → HALF_OPEN
    - Success threshold in HALF_OPEN: 1 success → CLOSED
    """

    def __init__(
        self,
        service_name: str,
        failure_threshold: int = 3,
        reset_timeout: int = 60,  # seconds
        success_threshold: int = 1
    ):
        self.service_name = service_name
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: datetime | None = None

        self.logger = logging.getLogger(__name__)

    async def call(
        self,
        func: Callable[..., T],
        fallback: Callable[..., T] | None = None,
        *args,
        **kwargs
    ) -> T:
        """
        Execute function with circuit breaker protection.

        Args:
            func: Function to execute
            fallback: Optional fallback function when circuit is OPEN
            *args, **kwargs: Arguments for func

        Returns:
            Result from func or fallback

        Raises:
            Exception: If circuit is OPEN and no fallback provided
        """
        # Check if we should transition from OPEN → HALF_OPEN
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.logger.info(
                    f"Circuit breaker for {self.service_name}: OPEN → HALF_OPEN (testing recovery)"
                )
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
            else:
                # Circuit still open, use fallback
                self.logger.warning(
                    f"Circuit breaker for {self.service_name} is OPEN. Using fallback."
                )
                if fallback:
                    return await fallback(*args, **kwargs)
                else:
                    raise Exception(
                        f"Service {self.service_name} is unavailable (circuit breaker OPEN)"
                    )

        # Attempt the call
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()

            # If circuit just opened, use fallback
            if self.state == CircuitState.OPEN and fallback:
                self.logger.warning(
                    f"Circuit breaker OPENED for {self.service_name}. Using fallback."
                )
                return await fallback(*args, **kwargs)

            raise

    def _on_success(self):
        """Handle successful call"""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.logger.info(
                    f"Circuit breaker for {self.service_name}: HALF_OPEN → CLOSED (service recovered)"
                )
                self.state = CircuitState.CLOSED
                self.failure_count = 0
        elif self.state == CircuitState.CLOSED:
            # Reset failure count on success
            self.failure_count = 0

    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()

        if self.state == CircuitState.HALF_OPEN:
            # Failure during test → back to OPEN
            self.logger.warning(
                f"Circuit breaker for {self.service_name}: HALF_OPEN → OPEN (test failed)"
            )
            self.state = CircuitState.OPEN
        elif self.state == CircuitState.CLOSED:
            if self.failure_count >= self.failure_threshold:
                self.logger.error(
                    f"Circuit breaker for {self.service_name}: CLOSED → OPEN "
                    f"({self.failure_count} consecutive failures)"
                )
                self.state = CircuitState.OPEN

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset"""
        if self.last_failure_time is None:
            return False

        elapsed = (datetime.now() - self.last_failure_time).total_seconds()
        return elapsed >= self.reset_timeout

# Global circuit breakers for AI services
bedrock_breaker = CircuitBreaker('bedrock', failure_threshold=3, reset_timeout=60)
azure_openai_breaker = CircuitBreaker('azure_openai', failure_threshold=3, reset_timeout=60)
```

**Usage with Fallback:**

```python
# apps/api/src/services/ai/ai_orchestrator.py
from services.resilience.circuit_breaker import bedrock_breaker, azure_openai_breaker

class AIOrchestrator:
    """Orchestrates AI generation with circuit breaker and failover"""

    async def generate_with_failover(self, prompt: str, project_data: dict) -> str:
        """
        Generate card with primary (Bedrock) and fallback (Azure OpenAI).
        Circuit breaker prevents cascading failures.
        """

        # Try Bedrock (primary) with circuit breaker
        try:
            async def _bedrock_call():
                return await self.bedrock_service.generate_card(prompt)

            async def _azure_fallback():
                self.logger.info("Using Azure OpenAI fallback (Bedrock circuit OPEN)")
                return await self.azure_service.generate_card(prompt)

            result = await bedrock_breaker.call(
                _bedrock_call,
                fallback=_azure_fallback
            )

            return result

        except Exception as e:
            # Both services failed, return degraded response
            self.logger.error(f"All AI services failed: {e}", exc_info=True)
            return self._generate_degraded_response(project_data)

    def _generate_degraded_response(self, project_data: dict) -> str:
        """
        Generate basic template when AI unavailable.
        Allows consultant to save draft and retry later.
        """
        return f"""
# {project_data['nazwaProjektu']}

**Status:** Wersja robocza - AI tymczasowo niedostępne

## Opis projektu
{project_data['opis']}

## Cel projektu
{project_data['celProjektu']}

## Harmonogram
- Data rozpoczęcia: {project_data['dataRozpoczecia']}
- Data zakończenia: {project_data['dataZakonczenia']}

---
*Ta karta wymaga uzupełnienia. AI jest tymczasowo niedostępne. Możesz zapisać jako wersję roboczą i wygenerować ponownie później.*
"""
```

---

#### Timeout Handling

**Global Timeout Middleware:**

```python
# apps/api/src/middleware/timeout_middleware.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio
import logging

class TimeoutMiddleware(BaseHTTPMiddleware):
    """
    Global timeout middleware for API requests.

    Timeouts:
    - AI generation endpoints: 15 minutes (900s)
    - Standard API endpoints: 30 seconds
    - Health checks: 5 seconds
    """

    TIMEOUT_CONFIG = {
        '/api/batches/generate': 900,  # 15 minutes for AI generation
        '/api/projects/regenerate': 900,
        '/api/batches': 30,
        '/api/projects': 30,
        '/health': 5,
        'default': 30
    }

    async def dispatch(self, request: Request, call_next):
        # Determine timeout based on path
        timeout = self._get_timeout(request.url.path)

        logger = logging.getLogger(__name__)
        logger.debug(f"Request to {request.url.path} with {timeout}s timeout")

        try:
            response = await asyncio.wait_for(
                call_next(request),
                timeout=timeout
            )
            return response

        except asyncio.TimeoutError:
            logger.error(
                f"Request timeout after {timeout}s: {request.method} {request.url.path}",
                extra={
                    'method': request.method,
                    'path': request.url.path,
                    'timeout': timeout
                }
            )

            # Return 504 Gateway Timeout with Polish message
            raise HTTPException(
                status_code=504,
                detail={
                    'error': 'timeout',
                    'message': f'Żądanie przekroczyło limit czasu ({timeout}s). Spróbuj ponownie później.',
                    'timeout_seconds': timeout
                }
            )

    def _get_timeout(self, path: str) -> int:
        """Get timeout for specific path"""
        for pattern, timeout in self.TIMEOUT_CONFIG.items():
            if pattern in path:
                return timeout
        return self.TIMEOUT_CONFIG['default']
```

**Celery Task Timeouts:**

```python
# apps/worker/src/tasks/ai_generation.py
from celery import Task
from celery.exceptions import SoftTimeLimitExceeded

@celery_app.task(
    bind=True,
    soft_time_limit=900,  # 15 minutes soft limit (allows cleanup)
    time_limit=960,  # 16 minutes hard limit (force kill)
    max_retries=1,
    retry_backoff=True
)
def generate_project_card_task(self, project_id: str, prompt: str) -> dict:
    """
    Generate project card with timeout protection.

    Soft limit (900s): Raises SoftTimeLimitExceeded, allows cleanup
    Hard limit (960s): Force kills task
    """
    try:
        # Generate card
        result = ai_orchestrator.generate_with_failover(prompt, project_data)

        return {
            'status': 'success',
            'content': result,
            'project_id': project_id
        }

    except SoftTimeLimitExceeded:
        logger.warning(f"Task soft timeout for project {project_id}")

        # Mark project as failed in database
        project_repo.update_status(project_id, 'generation_timeout')

        return {
            'status': 'timeout',
            'message': 'Generowanie przekroczyło limit 15 minut',
            'project_id': project_id
        }

    except Exception as e:
        logger.error(f"Task failed for project {project_id}: {e}", exc_info=True)
        raise self.retry(exc=e, countdown=60)  # Retry after 60s
```

---

#### Degraded Mode Strategy

**Service Availability Matrix:**

| Component | Status | Available Features | Unavailable Features |
|-----------|--------|-------------------|---------------------|
| **AI Services DOWN** | Degraded | - Upload Excel<br>- View past batches<br>- Edit saved projects<br>- Export saved projects<br>- Save drafts | - AI generation<br>- Quality scoring<br>- Auto-validation |
| **Database DOWN** | Critical | - None (system offline) | - All features |
| **S3 DOWN** | Degraded | - AI generation (with temp storage)<br>- View metadata<br>- Edit projects | - Excel uploads<br>- Word exports<br>- File downloads |
| **Redis DOWN** | Degraded | - All core features (slower)<br>- Auth via Cognito directly | - Real-time status updates<br>- Rate limiting<br>- Session caching |

**Degraded Mode Implementation:**

```python
# apps/api/src/services/degraded_mode.py
from enum import Enum

class ServiceHealth(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

class DegradedModeService:
    """Manages system behavior during service outages"""

    def __init__(self):
        self.service_health = {
            'bedrock': ServiceHealth.HEALTHY,
            'azure_openai': ServiceHealth.HEALTHY,
            'database': ServiceHealth.HEALTHY,
            's3': ServiceHealth.HEALTHY,
            'redis': ServiceHealth.HEALTHY
        }

    def get_system_status(self) -> dict:
        """Return overall system health"""
        critical_services = ['database']
        degraded_services = [
            name for name, health in self.service_health.items()
            if health == ServiceHealth.DEGRADED
        ]
        unavailable_services = [
            name for name, health in self.service_health.items()
            if health == ServiceHealth.UNAVAILABLE
        ]

        # System is CRITICAL if database is down
        if 'database' in unavailable_services:
            return {
                'status': 'critical',
                'message': 'System tymczasowo niedostępny',
                'available_features': []
            }

        # System is DEGRADED if AI or storage unavailable
        if unavailable_services or degraded_services:
            available_features = self._get_available_features(unavailable_services)
            return {
                'status': 'degraded',
                'message': 'Niektóre funkcje mogą być niedostępne',
                'available_features': available_features,
                'unavailable_services': unavailable_services + degraded_services
            }

        return {
            'status': 'healthy',
            'message': 'System działa prawidłowo',
            'available_features': ['all']
        }

    def _get_available_features(self, unavailable_services: list) -> list:
        """Determine which features work with current service availability"""
        all_features = [
            'excel_upload', 'ai_generation', 'edit_projects',
            'export_word', 'view_batches', 'quality_scoring'
        ]

        # Remove features based on unavailable services
        available = all_features.copy()

        if 'bedrock' in unavailable_services and 'azure_openai' in unavailable_services:
            available.remove('ai_generation')
            available.remove('quality_scoring')

        if 's3' in unavailable_services:
            available.remove('excel_upload')
            available.remove('export_word')

        return available

# Endpoint to expose health status
@router.get('/health/detailed')
async def get_detailed_health(
    degraded_service: DegradedModeService = Depends()
) -> dict:
    """
    Returns detailed system health status.
    Frontend uses this to show degraded mode warnings.
    """
    return degraded_service.get_system_status()
```

**Frontend Degraded Mode UI:**

```typescript
// apps/web/src/components/DegradedModeWarning.tsx
import { Alert, AlertTitle } from '@mui/material';
import { useQuery } from '@tanstack/react-query';

export function DegradedModeWarning() {
  const { data: health } = useQuery({
    queryKey: ['health'],
    queryFn: () => api.get('/health/detailed'),
    refetchInterval: 30000  // Check every 30s
  });

  if (!health || health.status === 'healthy') {
    return null;
  }

  if (health.status === 'critical') {
    return (
      <Alert severity="error">
        <AlertTitle>System tymczasowo niedostępny</AlertTitle>
        {health.message}. Spróbuj ponownie za kilka minut.
      </Alert>
    );
  }

  // Degraded mode
  return (
    <Alert severity="warning">
      <AlertTitle>Tryb ograniczony</AlertTitle>
      {health.message}. Funkcje AI mogą być tymczasowo niedostępne.
      Możesz kontynuować pracę z zapisanymi projektami.
    </Alert>
  );
}
```

---

### 15.6 Deployment & Rollback Procedures

#### Blue-Green Deployment Strategy

**Deployment Architecture:**

```
Production Traffic Flow:

┌─────────────┐
│   Route 53  │  (DNS: rnd-cards.example.com)
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────────┐
│  Application Load Balancer (ALB)         │
│  - Target Group: Blue (100% traffic)     │
│  - Target Group: Green (0% traffic)      │
└────┬─────────────────────────────┬───────┘
     │                             │
     ▼                             ▼
┌─────────────┐              ┌─────────────┐
│  ECS Service│              │  ECS Service│
│  (Blue)     │              │  (Green)    │
│  Version    │              │  Version    │
│  v1.2.3     │              │  v1.2.4     │
└─────────────┘              └─────────────┘
 ACTIVE                       STANDBY
```

**Deployment Steps:**

```yaml
# .github/workflows/deploy-production.yml
name: Deploy to Production (Blue-Green)

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to deploy (e.g., v1.2.4)'
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # 1. Build and push Docker images
      - name: Build Docker images
        run: |
          docker build -t rnd-cards-api:${{ inputs.version }} -f apps/api/Dockerfile .
          docker build -t rnd-cards-web:${{ inputs.version }} -f apps/web/Dockerfile .
          docker push rnd-cards-api:${{ inputs.version }}
          docker push rnd-cards-web:${{ inputs.version }}

      # 2. Run database migrations (safe, backward-compatible only)
      - name: Run database migrations
        run: |
          # Migrations must be backward-compatible with current version
          alembic upgrade head

      # 3. Deploy to GREEN environment (standby)
      - name: Deploy to Green (standby)
        run: |
          aws ecs update-service \
            --cluster rnd-cards-prod \
            --service rnd-cards-green \
            --task-definition rnd-cards:${{ inputs.version }} \
            --force-new-deployment

          # Wait for GREEN to be healthy
          aws ecs wait services-stable \
            --cluster rnd-cards-prod \
            --services rnd-cards-green

      # 4. Run smoke tests against GREEN
      - name: Smoke tests (Green environment)
        run: |
          npm run test:smoke -- --base-url https://green.rnd-cards-internal.example.com

      # 5. Switch traffic: Blue (100%) → Green (10%)
      - name: Gradual traffic shift (10%)
        run: |
          aws elbv2 modify-listener \
            --listener-arn $ALB_LISTENER_ARN \
            --default-actions \
              Type=forward,ForwardConfig='{
                "TargetGroups": [
                  {"TargetGroupArn": "$GREEN_TG_ARN", "Weight": 10},
                  {"TargetGroupArn": "$BLUE_TG_ARN", "Weight": 90}
                ]
              }'

          # Monitor for 5 minutes
          sleep 300

      # 6. Check metrics (error rate, latency)
      - name: Validate metrics
        run: |
          python scripts/check_deployment_metrics.py \
            --threshold-error-rate 1.0 \
            --threshold-p99-latency 2000

      # 7. Switch traffic: Blue (0%) → Green (100%)
      - name: Complete traffic shift (100%)
        run: |
          aws elbv2 modify-listener \
            --listener-arn $ALB_LISTENER_ARN \
            --default-actions \
              Type=forward,ForwardConfig='{
                "TargetGroups": [
                  {"TargetGroupArn": "$GREEN_TG_ARN", "Weight": 100}
                ]
              }'

      # 8. Monitor for 10 minutes
      - name: Final monitoring
        run: |
          sleep 600
          python scripts/check_deployment_metrics.py

      # 9. Mark BLUE as standby (keep running for fast rollback)
      - name: Success - Keep Blue as standby
        run: |
          echo "Deployment successful. Blue environment remains as standby for 24h."
          # Blue will be terminated after 24h if no rollback needed
```

---

#### Rollback Procedures

**Automated Rollback Triggers:**

```python
# scripts/check_deployment_metrics.py
import boto3
import sys
from datetime import datetime, timedelta

class DeploymentValidator:
    """
    Validates deployment health and triggers rollback if needed.

    Rollback triggers:
    - Error rate > 1% (from <0.1% baseline)
    - P99 latency > 2000ms (from ~500ms baseline)
    - 5xx errors > 10 in 5 minutes
    - Health check failures > 3 consecutive
    """

    THRESHOLDS = {
        'error_rate_percent': 1.0,
        'p99_latency_ms': 2000,
        'error_5xx_count': 10,
        'failed_health_checks': 3
    }

    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.ecs = boto3.client('ecs')
        self.elb = boto3.client('elbv2')

    def validate_deployment(self) -> bool:
        """
        Check all metrics. Return False if rollback needed.
        """
        metrics_ok = True

        # 1. Check error rate
        error_rate = self._get_error_rate()
        if error_rate > self.THRESHOLDS['error_rate_percent']:
            print(f"❌ Error rate {error_rate}% exceeds threshold {self.THRESHOLDS['error_rate_percent']}%")
            metrics_ok = False
        else:
            print(f"✅ Error rate: {error_rate}%")

        # 2. Check P99 latency
        p99_latency = self._get_p99_latency()
        if p99_latency > self.THRESHOLDS['p99_latency_ms']:
            print(f"❌ P99 latency {p99_latency}ms exceeds threshold {self.THRESHOLDS['p99_latency_ms']}ms")
            metrics_ok = False
        else:
            print(f"✅ P99 latency: {p99_latency}ms")

        # 3. Check 5xx errors
        error_5xx_count = self._get_5xx_count()
        if error_5xx_count > self.THRESHOLDS['error_5xx_count']:
            print(f"❌ 5xx errors {error_5xx_count} exceeds threshold {self.THRESHOLDS['error_5xx_count']}")
            metrics_ok = False
        else:
            print(f"✅ 5xx errors: {error_5xx_count}")

        # 4. Check health checks
        failed_health_checks = self._get_failed_health_checks()
        if failed_health_checks > self.THRESHOLDS['failed_health_checks']:
            print(f"❌ Failed health checks {failed_health_checks} exceeds threshold {self.THRESHOLDS['failed_health_checks']}")
            metrics_ok = False
        else:
            print(f"✅ Failed health checks: {failed_health_checks}")

        return metrics_ok

    def _get_error_rate(self) -> float:
        """Calculate error rate from CloudWatch"""
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=5)

        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='HTTPCode_Target_5XX_Count',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )

        error_count = response['Datapoints'][0]['Sum'] if response['Datapoints'] else 0

        # Get total request count
        response_total = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='RequestCount',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )

        total_count = response_total['Datapoints'][0]['Sum'] if response_total['Datapoints'] else 1

        return (error_count / total_count) * 100 if total_count > 0 else 0.0

    def _get_p99_latency(self) -> float:
        """Get P99 latency from CloudWatch"""
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=5)

        response = self.cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='TargetResponseTime',
            Dimensions=[{'Name': 'LoadBalancer', 'Value': 'rnd-cards-prod-alb'}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            ExtendedStatistics=['p99']
        )

        return response['Datapoints'][0]['ExtendedStatistics']['p99'] * 1000 if response['Datapoints'] else 0.0

    # ... (similar methods for 5xx count and health checks)

if __name__ == '__main__':
    validator = DeploymentValidator()

    if not validator.validate_deployment():
        print("\n🚨 DEPLOYMENT VALIDATION FAILED - INITIATING ROLLBACK")
        sys.exit(1)  # Non-zero exit triggers rollback in CI/CD

    print("\n✅ Deployment validation passed")
    sys.exit(0)
```

**Manual Rollback Procedure:**

```bash
#!/bin/bash
# scripts/rollback.sh - Manual rollback to previous version

set -e

CLUSTER="rnd-cards-prod"
BLUE_SERVICE="rnd-cards-blue"
GREEN_SERVICE="rnd-cards-green"
ALB_LISTENER_ARN="arn:aws:elasticloadbalancing:..."
BLUE_TG_ARN="arn:aws:elasticloadbalancing:..."
GREEN_TG_ARN="arn:aws:elasticloadbalancing:..."

echo "🔄 Starting rollback procedure..."

# 1. Immediately switch traffic back to BLUE (previous version)
echo "Step 1: Switching 100% traffic to Blue (previous version)"
aws elbv2 modify-listener \
  --listener-arn $ALB_LISTENER_ARN \
  --default-actions \
    Type=forward,ForwardConfig="{
      \"TargetGroups\": [
        {\"TargetGroupArn\": \"$BLUE_TG_ARN\", \"Weight\": 100}
      ]
    }"

echo "✅ Traffic switched to Blue"

# 2. Verify Blue is healthy
echo "Step 2: Verifying Blue environment health"
aws elbv2 describe-target-health \
  --target-group-arn $BLUE_TG_ARN

# 3. Stop Green service
echo "Step 3: Scaling down Green service"
aws ecs update-service \
  --cluster $CLUSTER \
  --service $GREEN_SERVICE \
  --desired-count 0

echo "✅ Rollback complete. Blue (previous version) is now serving 100% traffic."
echo "📊 Monitor metrics: https://console.aws.amazon.com/cloudwatch/..."
```

**Rollback Decision Matrix:**

| Metric | Threshold | Action | Severity |
|--------|-----------|--------|----------|
| Error rate > 1% | 5 minutes sustained | **Automatic rollback** | Critical |
| P99 latency > 2000ms | 5 minutes sustained | **Automatic rollback** | Critical |
| 5xx errors > 10 | In 5-minute window | **Automatic rollback** | Critical |
| Health checks failing | 3 consecutive | **Automatic rollback** | Critical |
| User reports | >5 critical bugs | **Manual rollback** | High |
| Database migration error | Any failure | **Manual rollback + DB rollback** | Critical |

---

#### Database Migration Safety

**Backward-Compatible Migration Guidelines:**

```python
# apps/api/migrations/versions/20250122_add_quality_metrics.py
"""
Add quality metrics columns to projects table.

IMPORTANT: This migration is backward-compatible.
- Columns added with DEFAULT values (no data loss)
- Old code (Blue) can still run during deployment
- New code (Green) uses new columns

Revision ID: a1b2c3d4e5f6
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    """
    Add quality metrics columns (backward-compatible).
    Blue environment (old code) ignores these columns.
    """
    # Add columns with DEFAULT to avoid breaking old code
    op.add_column('projects',
        sa.Column('quality_score', sa.Integer(), nullable=True, server_default='0')
    )
    op.add_column('projects',
        sa.Column('validation_errors', sa.JSON(), nullable=True, server_default='[]')
    )

    # Backfill existing rows (optional, can be done in background)
    # op.execute("UPDATE projects SET quality_score = 0 WHERE quality_score IS NULL")

def downgrade():
    """
    Rollback: Remove quality metrics columns.
    Only run this if rollback is needed within 24h of deployment.
    """
    op.drop_column('projects', 'quality_score')
    op.drop_column('projects', 'validation_errors')
```

**Migration Rollback Procedure:**

```bash
#!/bin/bash
# scripts/rollback-migration.sh

set -e

echo "🔄 Rolling back database migration..."

# 1. Identify current migration version
CURRENT_VERSION=$(alembic current)
echo "Current version: $CURRENT_VERSION"

# 2. Rollback to previous version
PREVIOUS_VERSION="$1"  # Pass as argument

if [ -z "$PREVIOUS_VERSION" ]; then
  echo "❌ Error: Must specify previous version"
  echo "Usage: ./rollback-migration.sh <previous_version_id>"
  exit 1
fi

# 3. Confirm rollback
echo "⚠️  WARNING: Rolling back from $CURRENT_VERSION to $PREVIOUS_VERSION"
read -p "Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
  echo "Rollback cancelled"
  exit 0
fi

# 4. Execute rollback
echo "Rolling back migration..."
alembic downgrade $PREVIOUS_VERSION

echo "✅ Migration rollback complete"
echo "📊 Verify database state manually"
```

**Migration Safety Checklist:**

- [ ] Migration is backward-compatible (Blue can run with new schema)
- [ ] No columns dropped (use deprecation instead)
- [ ] No NOT NULL columns without DEFAULT
- [ ] Tested rollback procedure in staging
- [ ] Database backup taken before migration
- [ ] Monitoring alerts configured for migration errors

---

#### Smoke Test Definitions

**Critical User Paths (5 tests):**

```typescript
// apps/api/tests/smoke/smoke-tests.spec.ts
import { test, expect } from '@playwright/test';

/**
 * Smoke tests run after deployment to validate critical paths.
 * Must complete in <2 minutes total.
 */

test.describe('Smoke Tests - Critical Paths', () => {

  // 1. Authentication flow
  test('Path 1: User can authenticate', async ({ page }) => {
    await page.goto('/login');

    await page.fill('input[name="email"]', 'smoke-test@example.com');
    await page.fill('input[name="password"]', process.env.SMOKE_TEST_PASSWORD);
    await page.click('button[type="submit"]');

    // Should redirect to dashboard
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('text=Witaj')).toBeVisible();
  });

  // 2. Excel upload + batch creation
  test('Path 2: User can upload Excel and create batch', async ({ page }) => {
    await page.goto('/dashboard');

    // Upload Excel file
    await page.setInputFiles('input[type="file"]', 'tests/fixtures/test-batch-5-projects.xlsx');
    await page.fill('input[name="batchName"]', `Smoke Test ${Date.now()}`);
    await page.click('button:has-text("Prześlij")');

    // Should see batch in list
    await expect(page.locator('text=Smoke Test')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('text=5 projektów')).toBeVisible();
  });

  // 3. AI generation (single project)
  test('Path 3: User can generate project card with AI', async ({ page }) => {
    await page.goto('/dashboard');

    // Find test batch (created by previous test or setup)
    await page.click('text=Smoke Test Batch');

    // Click generate for first project
    await page.click('button:has-text("Generuj"):first');

    // Wait for generation (max 180s)
    await expect(page.locator('text=Generowanie zakończone')).toBeVisible({ timeout: 180000 });

    // Verify content exists
    const content = await page.locator('.project-card-content').textContent();
    expect(content.length).toBeGreaterThan(500);  // Should have substantial content
  });

  // 4. Project review + edit
  test('Path 4: User can review and edit generated card', async ({ page }) => {
    await page.goto('/dashboard');

    await page.click('text=Smoke Test Batch');
    await page.click('button:has-text("Przejrzyj"):first');

    // Should see editor
    await expect(page.locator('.project-editor')).toBeVisible();

    // Make an edit
    await page.fill('textarea[name="opis"]', 'Edytowany opis projektu (smoke test)');
    await page.click('button:has-text("Zapisz")');

    // Should see success message
    await expect(page.locator('text=Zapisano zmiany')).toBeVisible();
  });

  // 5. Word export
  test('Path 5: User can export batch to Word', async ({ page }) => {
    await page.goto('/dashboard');

    await page.click('text=Smoke Test Batch');

    // Start download
    const downloadPromise = page.waitForEvent('download');
    await page.click('button:has-text("Eksportuj do Word")');
    const download = await downloadPromise;

    // Verify download
    expect(download.suggestedFilename()).toContain('Smoke_Test');
    expect(download.suggestedFilename()).toContain('.docx');

    // Verify file size (should be >50KB for 5 projects)
    const path = await download.path();
    const fs = require('fs');
    const stats = fs.statSync(path);
    expect(stats.size).toBeGreaterThan(50000);
  });
});

/**
 * API Health Checks
 */
test.describe('Smoke Tests - API Health', () => {

  test('API /health returns 200', async ({ request }) => {
    const response = await request.get('/api/health');
    expect(response.status()).toBe(200);

    const body = await response.json();
    expect(body.status).toBe('healthy');
  });

  test('API /health/detailed shows all services healthy', async ({ request }) => {
    const response = await request.get('/api/health/detailed');
    expect(response.status()).toBe(200);

    const body = await response.json();
    expect(body.database).toBe('healthy');
    expect(body.redis).toBe('healthy');
    expect(body.s3).toBe('healthy');
  });
});
```

**Running Smoke Tests:**

```bash
# Run smoke tests against specific environment
npm run test:smoke -- --base-url https://green.rnd-cards-internal.example.com

# Expected output:
# ✅ Path 1: User can authenticate (2.1s)
# ✅ Path 2: User can upload Excel and create batch (5.3s)
# ✅ Path 3: User can generate project card with AI (45.2s)
# ✅ Path 4: User can review and edit generated card (3.8s)
# ✅ Path 5: User can export batch to Word (4.1s)
# ✅ API /health returns 200 (0.2s)
# ✅ API /health/detailed shows all services healthy (0.3s)
#
# Total: 7 passed (60.0s)
```

---

### 15.2 Performance Optimization

**Frontend Performance:**
- **Bundle Size Target:** <500KB initial JS (gzipped)
- **Loading Strategy:** Code splitting by route, lazy loading components
- **Caching Strategy:** React Query with 5-minute stale time for batches, 1-minute for projects

**Backend Performance:**
- **Response Time Target:** <200ms for API endpoints (except AI generation)
- **Database Optimization:** Indexed queries, connection pooling (max 20 connections)
- **Caching Strategy:** Redis cache for user sessions (24-hour TTL), batch metadata (5-minute TTL)

---

## 16. Testing Strategy

### 16.1 Testing Pyramid

```
        E2E Tests (Playwright)
       /                      \
  Integration Tests
 /            |             \
Frontend Unit  Backend Unit  Worker Unit
```

---

### 16.2 Test Organization

**Frontend Tests:**

```
apps/web/tests/
├── unit/
│   ├── components/
│   │   ├── QualityScoreBadge.test.tsx
│   │   └── ProjectCard.test.tsx
│   └── hooks/
│       └── useAuth.test.ts
├── integration/
│   ├── BatchUpload.test.tsx
│   └── ProjectReview.test.tsx
└── e2e/
    ├── complete-workflow.spec.ts
    └── batch-processing.spec.ts
```

**Backend Tests:**

```
apps/api/tests/
├── unit/
│   ├── services/
│   │   ├── test_ai_service.py
│   │   └── test_validation_service.py
│   └── repositories/
│       └── test_batch_repository.py
├── integration/
│   ├── test_batches_api.py
│   ├── test_projects_api.py
│   └── test_auth_api.py
└── e2e/
    └── test_complete_workflow.py
```

---

### 16.3 Test Examples

**Frontend Component Test:**

```typescript
// apps/web/tests/unit/components/QualityScoreBadge.test.tsx
import { render, screen } from '@testing-library/react';
import { QualityScoreBadge } from '@/components/molecules/QualityScoreBadge';

describe('QualityScoreBadge', () => {
  it('displays score with correct color for high quality', () => {
    render(<QualityScoreBadge score={85} />);
    const badge = screen.getByText('85%');
    expect(badge).toBeInTheDocument();
    expect(badge).toHaveClass('MuiBadge-colorSuccess');
  });

  it('displays warning color for medium quality', () => {
    render(<QualityScoreBadge score={65} />);
    const badge = screen.getByText('65%');
    expect(badge).toHaveClass('MuiBadge-colorWarning');
  });

  it('displays error color for low quality', () => {
    render(<QualityScoreBadge score={40} />);
    const badge = screen.getByText('40%');
    expect(badge).toHaveClass('MuiBadge-colorError');
  });
});
```

**Backend API Test:**

```python
# apps/api/tests/integration/test_batches_api.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_create_batch_with_valid_excel(client: AsyncClient, auth_token: str):
    files = {'file': ('test.xlsx', open('tests/fixtures/valid.xlsx', 'rb'))}
    data = {'name': 'Test Batch'}

    response = await client.post(
        '/v1/batches',
        files=files,
        data=data,
        headers={'Authorization': f'Bearer {auth_token}'}
    )

    assert response.status_code == 201
    batch = response.json()
    assert batch['name'] == 'Test Batch'
    assert batch['status'] == 'queued'
    assert batch['totalProjects'] == 5

@pytest.mark.asyncio
async def test_create_batch_with_invalid_excel_returns_validation_errors(
    client: AsyncClient,
    auth_token: str
):
    files = {'file': ('invalid.xlsx', open('tests/fixtures/invalid.xlsx', 'rb'))}
    data = {'name': 'Invalid Batch'}

    response = await client.post(
        '/v1/batches',
        files=files,
        data=data,
        headers={'Authorization': f'Bearer {auth_token}'}
    )

    assert response.status_code == 400
    errors = response.json()['errors']
    assert len(errors) > 0
    assert errors[0]['rowNumber'] == 2
    assert errors[0]['errorType'] == 'missing_required'
```

**E2E Test:**

```typescript
// apps/web/tests/e2e/complete-workflow.spec.ts
import { test, expect } from '@playwright/test';

test('complete batch processing workflow', async ({ page }) => {
  // Login
  await page.goto('http://localhost:5173/login');
  await page.fill('input[name="email"]', 'test@example.com');
  await page.fill('input[name="password"]', 'TestPass123');
  await page.click('button[type="submit"]');

  // Wait for dashboard
  await expect(page).toHaveURL(/.*dashboard/);

  // Upload Excel file
  await page.click('text=Nowa partia');
  const fileInput = await page.locator('input[type="file"]');
  await fileInput.setInputFiles('tests/fixtures/valid.xlsx');
  await page.fill('input[name="batchName"]', 'E2E Test Batch');
  await page.click('button:has-text("Rozpocznij generowanie")');

  // Wait for processing screen
  await expect(page).toHaveURL(/.*processing/);

  // Wait for first project to complete (max 2 minutes)
  await expect(page.locator('text=Gotowe').first()).toBeVisible({ timeout: 120000 });

  // Navigate to review
  await page.click('.project-card >> nth=0');
  await expect(page).toHaveURL(/.*review/);

  // Verify sections loaded
  await expect(page.locator('text=Nazwa projektu')).toBeVisible();
  await expect(page.locator('text=Cel projektu')).toBeVisible();

  // Edit section
  const editor = page.locator('.tiptap-editor').first();
  await editor.click();
  await editor.type(' - edycja testowa');

  // Wait for quality score update
  await page.waitForTimeout(1000);

  // Export project
  await page.click('button:has-text("Pobierz projekt")');

  // Verify download started
  const download = await page.waitForEvent('download');
  expect(download.suggestedFilename()).toMatch(/Projekt-.*\.docx/);
});
```

---

## 17. Coding Standards

### 17.1 Critical Fullstack Rules

**Type Sharing:** Always define types in `packages/shared` and import from there. Never duplicate type definitions between frontend and backend.

**API Calls:** Never make direct HTTP calls in components - use the service layer (`apps/web/src/services/`).

**Environment Variables:** Access only through config objects, never `process.env` or `import.meta.env` directly.

**Error Handling:** All API routes must use the standard error handler middleware.

**State Updates:** Never mutate state directly - use proper state management patterns (React Query mutations, setState).

**Database Access:** Never write raw SQL - use SQLAlchemy ORM and repository pattern.

**AI Prompts:** Store all prompts as constants in `apps/api/src/services/prompts/`, never inline.

**S3 Keys:** Use consistent naming: `{userId}/{batchId}/uploads/{filename}` for uploads, `{userId}/{batchId}/exports/{projectId}.docx` for exports.

---

### 17.2 Naming Conventions

| Element | Frontend | Backend | Example |
|---------|----------|---------|---------|
| **Components** | PascalCase | - | `UserProfile.tsx` |
| **Hooks** | camelCase with 'use' | - | `useAuth.ts` |
| **API Routes** | - | snake_case | `/api/user-profile` |
| **Database Tables** | - | snake_case | `user_profiles` |
| **Functions** | camelCase | snake_case | `handleSubmit()`, `validate_excel()` |
| **Constants** | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE | `MAX_BATCH_SIZE` |
| **Interfaces/Types** | PascalCase | PascalCase | `UserProfile` |

---

### 17.3 Code Quality Gates

**Pre-commit Requirements:**
- ESLint passes (frontend)
- Ruff/mypy passes (backend)
- Unit tests pass
- Type checking passes

**Pre-merge Requirements:**
- All tests pass (unit + integration)
- Code coverage ≥80% for new code
- No TypeScript/mypy errors
- PR reviewed by at least 1 developer

---

## 18. Error Handling Strategy

### 18.1 Error Flow

```mermaid
sequenceDiagram
    participant Frontend
    participant API
    participant Service
    participant DB

    Frontend->>API: POST /projects/{id}
    API->>Service: update_project_content()
    Service->>DB: Update query

    alt Database Error
        DB->>Service: IntegrityError
        Service->>Service: Log error
        Service->>API: Raise HTTPException(500)
        API->>API: ErrorHandler middleware
        API->>Frontend: {error: "Internal error", requestId: "xxx"}
        Frontend->>Frontend: Display error toast
        Frontend->>Frontend: Log to console
    else Validation Error
        Service->>API: Raise HTTPException(400)
        API->>Frontend: {error: "Invalid input", details: {...}}
        Frontend->>Frontend: Display inline error
    else Success
        DB->>Service: Updated record
        Service->>API: Return data
        API->>Frontend: 200 OK
        Frontend->>Frontend: Update UI
    end
```

---

### 18.2 Error Response Format

**Standard Error Response:**

```typescript
interface ApiError {
  error: {
    code: string;           // 'validation_error' | 'internal_error' | 'not_found'
    message: string;        // Polish user-facing message
    details?: Record<string, any>; // Field-level errors for forms
    timestamp: string;
    requestId: string;      // For support/debugging
  };
}
```

**Example:**

```json
{
  "error": {
    "code": "validation_error",
    "message": "Błędy walidacji w pliku Excel",
    "details": {
      "row2": {
        "opis": "Opis musi mieć co najmniej 100 znaków"
      },
      "row5": {
        "dataZakonczenia": "Data zakończenia musi być późniejsza niż data rozpoczęcia"
      }
    },
    "timestamp": "2025-10-22T14:30:00Z",
    "requestId": "req_abc123"
  }
}
```

---

### 18.3 Frontend Error Handling

```typescript
// apps/web/src/services/api.ts (interceptor)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const apiError = error.response?.data?.error;

    // Log to console for debugging
    console.error('[API Error]', {
      code: apiError?.code,
      message: apiError?.message,
      requestId: apiError?.requestId,
      url: error.config?.url
    });

    // Show user-friendly toast notification
    if (apiError?.message) {
      toast.error(apiError.message);
    } else {
      toast.error('Wystąpił nieoczekiwany błąd. Spróbuj ponownie.');
    }

    return Promise.reject(error);
  }
);
```

---

### 18.4 Backend Error Handling

```python
# apps/api/src/middleware/error_handler.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging
import uuid

logger = logging.getLogger(__name__)

async def error_handler_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())

    try:
        response = await call_next(request)
        return response
    except HTTPException as exc:
        # Expected errors
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.detail.get("code", "http_error"),
                    "message": exc.detail.get("message", str(exc.detail)),
                    "details": exc.detail.get("details"),
                    "timestamp": datetime.utcnow().isoformat(),
                    "requestId": request_id
                }
            }
        )
    except Exception as exc:
        # Unexpected errors
        logger.exception(f"Unhandled exception: {exc}", extra={"requestId": request_id})
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "internal_error",
                    "message": "Wystąpił błąd serwera. Skontaktuj się z pomocą techniczną.",
                    "timestamp": datetime.utcnow().isoformat(),
                    "requestId": request_id
                }
            }
        )
```

---

## 19. Monitoring and Observability

### 19.1 Monitoring Stack

- **Frontend Monitoring:** CloudWatch RUM (Real User Monitoring)
- **Backend Monitoring:** CloudWatch Logs + Metrics
- **Error Tracking:** CloudWatch Insights
- **Performance Monitoring:** CloudWatch Application Insights

---

### 19.2 Key Metrics

**Frontend Metrics:**
- Core Web Vitals (LCP, FID, CLS)
- JavaScript errors (count, stack traces)
- API response times (P50, P95, P99)
- User interactions (button clicks, page views)

**Backend Metrics:**
- Request rate (requests/minute)
- Error rate (errors/total requests %)
- Response time (P50, P95, P99)
- Database query performance (slow query log)
- AI generation time (per project)
- AI cost (EUR per project, daily total)
- Celery queue depth (pending tasks)
- Worker utilization (active/idle workers)

**Alerts:**
- Error rate >5% for 5 minutes
- API response time P95 >1 second
- AI generation failures >10% in 10 minutes
- Daily AI cost >€100 (budget warning)
- Database connection pool exhausted
- Celery queue depth >50 tasks

---

### 19.3 CloudWatch Dashboard

**Widgets:**

1. **API Health**
   - Request rate (line chart)
   - Error rate % (line chart)
   - P50/P95/P99 latency (line chart)

2. **AI Generation**
   - Projects generated/hour (bar chart)
   - Average generation time (line chart)
   - Failure rate % (line chart)
   - Cost per project (line chart)

3. **Infrastructure**
   - ECS CPU utilization (line chart)
   - ECS memory utilization (line chart)
   - Database connections (line chart)
   - Redis memory usage (line chart)

4. **User Activity**
   - Active users (gauge)
   - Batches created/hour (bar chart)
   - Projects exported/hour (bar chart)

---

## 20. Summary

This architecture provides a robust, scalable, and maintainable foundation for the R&D Tax Relief Project Card Generator. Key highlights:

**Strengths:**
- ✅ Modern tech stack (React 18, FastAPI, AWS)
- ✅ EU-compliant (GDPR, data residency)
- ✅ Resilient AI integration (primary + failover)
- ✅ Real-time batch processing (WebSocket)
- ✅ Comprehensive testing strategy
- ✅ Production-ready deployment pipeline

**Technology Decisions:**
- AWS-centric for simplicity (Bedrock requirement)
- Monorepo for type sharing (TypeScript across stack)
- Celery for async batch processing (proven pattern)
- React Query for server state (eliminates Redux)
- PostgreSQL JSONB for flexible content storage

**Next Steps:**
1. Run architecture validation checklist
2. Set up development environment
3. Execute AI generation POC (2 weeks)
4. Begin Sprint 0 (infrastructure setup)
5. Start Epic 1 development (Excel upload)

**Architecture Owner:** Winston (BMad Architect)
**Review Date:** 2025-10-22
**Status:** ✅ Ready for Development

---

**End of Architecture Document**
