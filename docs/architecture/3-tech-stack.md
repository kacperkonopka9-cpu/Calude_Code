# 3. Tech Stack

## Technology Stack Table

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
