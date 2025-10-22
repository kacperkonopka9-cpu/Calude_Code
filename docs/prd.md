# Product Requirements Document (PRD)
## R&D Tax Relief Project Card Generator

**Version:** 1.0
**Date:** October 22, 2025
**Product Manager:** John (BMad PM Agent)
**Status:** Draft

---

## 1. Goals and Background Context

### 1.1 Product Goals

This product aims to deliver the following measurable outcomes:

1. **Reduce Manual Work Time**: Decrease project card generation time from 20-40 hours per batch to <5 hours total (including review/editing)
2. **Enable Batch Processing**: Support generation of 1-20 project cards from a single Excel file upload
3. **Achieve Quality Threshold**: Deliver ≥70% AI-generated content that requires ≤30% consultant editing to meet Ulga B+R standards
4. **Maintain Speed**: Generate individual project cards in ≤15 minutes (target: 1 minute average)
5. **Ensure Compliance**: Produce cards that comply with Polish R&D tax relief (Ulga B+R) requirements without legal risk
6. **Maximize Accessibility**: Achieve WCAG 2.1 Level AA compliance for all users including tax consultants with varying technical skills
7. **Provide Transparency**: Display clear quality scores (0-100%) and highlight AI-generated vs. manual sections for consultant confidence

### 1.2 Background Context

Polish R&D tax consultants currently spend 20-40 hours manually creating batches of 10-20 project cards for clients applying for Ulga B+R (Research & Development tax relief). Each card requires detailed Polish-language descriptions of project goals, methodology, innovation, and R&D activities across 8-12 sections following strict government templates.

This manual process creates a business bottleneck: consultants who could handle strategic client relationships instead spend most of their time on repetitive document generation. The quality is inconsistent, deadlines are tight, and scaling the business requires hiring more expensive specialists.

Our solution leverages AI (Claude 3.5 Sonnet or GPT-4) to automate 70%+ of the content generation while keeping consultants in control through a review/edit workflow. By providing structured Excel input templates and validating data upfront, we ensure AI receives the context needed to generate high-quality, compliant project cards that consultants can confidently submit after minimal editing.

---

## 2. Requirements

### 2.1 Functional Requirements

**FR1:** The system shall accept Excel file uploads (.xlsx format) with required columns: Nazwa projektu, Opis, Data rozpoczęcia, Data zakończenia, Cel projektu, Osoba odpowiedzialna

**FR2:** The system shall validate uploaded Excel files for:
- Required column presence
- Data type correctness (dates, text fields)
- Minimum content length (Opis ≥100 chars, Cel projektu ≥50 chars)
- Date logic (Data zakończenia ≥ Data rozpoczęcia)
- Row count limits (1-20 projects per batch)

**FR3:** The system shall display validation errors with Polish-language messages indicating specific row numbers and missing/incorrect fields before allowing generation to proceed

**FR4:** The system shall provide a downloadable Excel template (.xlsx) with:
- Pre-configured columns with Polish headers
- Example data rows demonstrating required format
- Cell validation rules (date formats, text length hints)
- Instructions sheet explaining each field

**FR5:** The system shall process uploaded Excel files row-by-row, treating each row as a separate project card generation task

**FR6:** The system shall generate Polish-language project cards using AI (Claude 3.5 Sonnet or GPT-4) following the Ulga B+R template structure with sections:
- Nazwa projektu
- Cel projektu
- Opis projektu
- Nowatorskość i innowacyjność
- Metodologia prac B+R
- Rezultaty projektu
- Koszty kwalifikowane
- Harmonogram

**FR7:** The system shall process up to 5 projects concurrently (parallel AI API calls) while queueing remaining projects in the batch

**FR8:** The system shall display real-time processing status for each project in the batch showing:
- Queue position (Oczekuje)
- Generating state with progress (Generowanie...)
- Completion state (Gotowe)
- Error state with retry option (Błąd - Spróbuj ponownie)

**FR9:** The system shall calculate and display a quality score (0-100%) for each generated project card based on:
- Section completeness (all 8 required sections present)
- Content length adequacy (minimum thresholds per section)
- Polish language quality (grammar, terminology)
- Ulga B+R keyword presence (B+R, innowacyjność, etc.)

**FR10:** The system shall provide an inline review interface for each generated project card allowing consultants to:
- View AI-generated content section-by-section
- Edit content directly in rich text editor
- See quality score updated in real-time as edits are made
- Mark sections as "Approved" or "Needs Work"

**FR11:** The system shall visually distinguish AI-generated content from manually edited content using:
- Yellow background highlight for AI-generated sections
- White background for consultant-edited sections
- Timestamp showing last edit time

**FR12:** The system shall allow consultants to regenerate individual sections using a "Regeneruj sekcję" button with options to:
- Keep current context
- Provide additional instructions/hints (optional text field)
- Select alternative AI model (Claude vs GPT-4)

**FR13:** The system shall export completed project cards to Word (.docx) format matching the official Ulga B+R template layout with:
- Government-compliant formatting (fonts, margins, headers)
- All 8 sections in required order
- Consultant and client company information in header/footer
- Date of generation

**FR14:** The system shall allow batch export of multiple completed project cards as:
- Single ZIP file containing individual .docx files (one per project)
- Naming convention: "Projekt-{Nazwa projektu}-{YYYY-MM-DD}.docx"

**FR15:** The system shall save all project card generation sessions (input data, AI outputs, consultant edits, quality scores) for 90 days enabling:
- Resume incomplete batches
- Access generation history
- Download previous exports

**FR16:** The system shall provide a Dashboard view displaying:
- Recent batches (last 10)
- Batch status (In Progress, Completed, Archived)
- Total projects per batch
- Average quality score per batch
- Completion date

**FR17:** The system shall allow consultants to delete/archive completed batches older than 30 days to manage storage

**FR18:** The system shall display estimated time remaining for batch processing based on:
- Number of projects in queue
- Average generation time (rolling average)
- Current API response times

**FR19:** The system shall handle AI API failures gracefully by:
- Retrying failed requests (max 3 attempts with exponential backoff)
- Displaying clear error messages in Polish
- Allowing manual retry for failed projects
- Continuing processing of remaining projects in batch

**FR20:** The system shall log all AI API calls (timestamps, tokens used, model, response time) for cost tracking and debugging

### 2.2 Non-Functional Requirements

**NFR1:** The system shall generate individual project cards in ≤1 minute average (target), ≤15 minutes maximum per card

**NFR2:** The system shall process batches of 20 projects in ≤30 minutes total generation time (excluding consultant review)

**NFR3:** The system shall achieve ≥70% usable AI-generated content quality requiring ≤30% consultant editing (measured by character count changes)

**NFR4:** The system shall maintain ≥99% uptime during Polish business hours (8:00-18:00 CET Monday-Friday)

**NFR5:** The system shall respond to user interactions (button clicks, navigation) in ≤200ms

**NFR6:** The system shall load the Dashboard view in ≤1 second

**NFR7:** The system shall display real-time processing status updates at ≤2 second intervals

**NFR8:** The system shall support concurrent access by ≤50 users without performance degradation

**NFR9:** The system shall support Excel files up to 5MB in size

**NFR10:** The system shall export Word documents ≤2MB per project card

**NFR11:** The system shall comply with WCAG 2.1 Level AA accessibility standards including:
- Keyboard navigation for all functions
- Screen reader compatibility
- Minimum 4.5:1 color contrast ratios
- Focus indicators on interactive elements

**NFR12:** The system shall display all UI text, messages, and instructions in Polish language

**NFR13:** The system shall be responsive and usable on desktop browsers (Chrome, Firefox, Edge, Safari) at screen resolutions ≥1366×768

**NFR14:** The system shall provide limited mobile browser support (view-only for Dashboard and Results; upload/edit requires desktop)

**NFR15:** The system shall encrypt all data in transit using TLS 1.3

**NFR16:** The system shall rate-limit AI API calls to prevent quota exhaustion (max 5 concurrent, queue remaining)

**NFR17:** The system shall store uploaded Excel files and generated content for 90 days, then automatically archive or delete per data retention policy

**NFR18:** The system shall implement authentication to prevent unauthorized access (specific auth method TBD by Architect)

**NFR19:** The system shall be maintainable by developers with React/TypeScript experience following documented coding standards

**NFR20:** The system shall be deployable to cloud hosting (Vercel recommended) with CI/CD pipeline for automated testing and deployment

### 2.3 Requirements Rationale

**Key Trade-offs:**
- **Quality vs. Speed**: We target 1-minute average generation but allow up to 15 minutes for complex projects. This reflects the reality that some projects require more AI reasoning time. The 70% quality threshold balances "good enough to save time" with "needs consultant expertise."
- **Batch Size Limits**: The 1-20 project limit per batch prevents overwhelming consultants with review work while supporting realistic client engagement sizes (most consultants handle 10-20 cards per deadline).
- **Parallel Processing**: 5 concurrent AI calls balances API cost/rate limits with user-perceived speed. Processing 20 cards sequentially would take 20 minutes; parallel processing reduces this to ~4 minutes.

**Assumptions:**
- Consultants have desktop computers (not tablets/phones) for primary work
- Excel is the universal format for client data handoff
- AI models (Claude 3.5 Sonnet/GPT-4) maintain current quality levels and pricing
- Polish government Ulga B+R template requirements remain stable for 12+ months

**Alignment with Brief:**
- FR1-FR5, FR18 address "Data Validation" pain point from brief (prevent garbage-in-garbage-out)
- FR6-FR8, NFR1-NFR3 address "Speed" goal (≤5 hours total vs. 20-40 hours manual)
- FR9-FR12 address "Quality Control" and "Transparency" principles from UX goals
- FR13-FR14 address "Output Format" requirement (government-compliant .docx)
- NFR11-NFR14 address "Accessibility" for persona 3 (inbound accountant with limited tech skills)

---

## 3. User Interface Design Goals

### 3.1 UX Vision

The user interface shall embody the **iNOV Research & Development** brand identity while delivering a streamlined, professional workflow for Polish R&D tax consultants. The design prioritizes **speed over polish** and **clarity over features**, reflecting the consultant's need to process batches efficiently under tight deadlines.

**Core Design Principles** (from front-end specification):
1. **Speed First** - Minimize clicks and cognitive load; default paths for common workflows
2. **Clarity of Understanding** - Transparent AI process with quality scores and edit tracking
3. **Transparency** - Clear status, progress indicators, and error messages
4. **Professional Polish** - Clean, uncluttered interface with iNOV branding

**Design Decision Protocol**: When principles conflict, resolve in priority order: **Speed > Clarity > Transparency > Polish**

### 3.2 Target Personas

The interface serves three primary user types (detailed in `docs/front-end-spec.md`):

1. **Agnieszka (Primary: Time-Pressed Consultant)** - 32, senior R&D tax consultant, processes 20+ cards per deadline, needs fastest possible workflow
2. **Marcin (Secondary: Quality Guardian)** - 28, junior consultant, focuses on compliance accuracy, needs confidence-building transparency
3. **Beata (Tertiary: Inbound Accountant)** - 45, limited R&D tax knowledge, needs clear guidance and error prevention

### 3.3 Key Interaction Paradigms

**Workflow Model**: **Linear Pipeline with Exit Ramps**
- Primary flow: Upload → Validate → Generate → Review → Download
- Exit ramps: Save draft, retry failed, regenerate sections, download template
- No complex navigation trees; Dashboard serves as home base

**Status Visibility**: **Glanceable Progress**
- Real-time batch processing grid showing all 20 projects simultaneously
- Color-coded states: Gray (queue), Yellow (generating), Green (complete), Red (error)
- Estimated time remaining updates every 2 seconds

**Quality Feedback**: **Numeric + Visual**
- Quality score (0-100%) displayed prominently per project
- Yellow highlight for AI-generated content, white for edited
- Score recalculates in real-time as consultant edits

**Error Handling**: **Inline + Actionable**
- Validation errors shown in-context (red border on upload, row-level messages)
- Failed generation shows "Spróbuj ponownie" button
- Excel template download link embedded in error messages

### 3.4 Core Screens and Views

Detailed wireframes and component specifications are available in `docs/front-end-spec.md` (Section 4) and visual design specifications in `docs/figma-design-specifications.md`. Summary:

#### 3.4.1 Dashboard (Home)
- **Purpose**: Entry point showing recent batches and status overview
- **Key Elements**:
  - "Nowa partia" (New Batch) prominent CTA button
  - Recent batches table (10 rows) with status, date, project count
  - "Pobierz szablon Excel" (Download Template) link in header
- **Interactions**: Click batch row to resume/view; click "Nowa partia" to start upload

#### 3.4.2 Upload Screen
- **Purpose**: Excel file upload with validation
- **Key Elements**:
  - Drag-and-drop upload zone (fallback: file picker)
  - Real-time validation with row-level error display
  - "Pobierz szablon" link if validation fails
  - "Rozpocznij generowanie" (Start Generation) button enabled only after successful validation
- **Interactions**: Upload → Validate → Proceed or Download Template → Fix → Re-upload

#### 3.4.3 Processing Screen
- **Purpose**: Real-time batch generation monitoring
- **Key Elements**:
  - Grid of project cards (1-20) showing status per project
  - Each card displays: Project name, status (Oczekuje/Generowanie/Gotowe/Błąd), progress bar
  - Overall batch progress: "12/20 gotowych, ~8 minut pozostało"
  - "Anuluj" (Cancel) button to stop remaining generations
- **Interactions**: Auto-refresh every 2s; click completed project to preview; retry failed projects

#### 3.4.4 Results & Review Screen
- **Purpose**: Review generated content and make edits
- **Key Elements**:
  - Left sidebar: List of all projects in batch with quality scores
  - Main panel: Selected project's 8 sections with inline editing
  - Quality score badge (0-100%) updates as edits are made
  - "Regeneruj sekcję" button per section
  - Yellow highlight for AI content, white for edited
  - "Pobierz projekt" (Download) and "Pobierz wszystko" (Download All) buttons
- **Interactions**: Click project in sidebar to switch; edit inline; regenerate sections; download individually or as ZIP

#### 3.4.5 Error Recovery Screen
- **Purpose**: Handle validation failures and generation errors
- **Key Elements**:
  - Clear error message in Polish explaining issue
  - Specific row numbers and field names for validation errors
  - "Pobierz szablon Excel" button
  - "Spróbuj ponownie" (Retry) button for generation failures
  - "Wróć do panelu" (Back to Dashboard) link
- **Interactions**: Download template → fix data → re-upload; or retry failed generation

### 3.5 Visual Design System

**Brand Identity**: iNOV Research & Development
- **Primary Color**: Yellow (#F5C344) - used for primary CTAs, highlights, accents
- **Secondary Color**: Navy (#2C3E50) - used for text, headers, navigation
- **Logo**: Light bulb icon with "iNOV" wordmark (3 variants: horizontal, stacked, icon-only)
- **Typography**: Inter (UI), Roboto Slab (headings) - see Figma specs for exact weights

**Component Library** (Material-UI v5 customization):
- **inovTheme**: Custom MUI theme with iNOV color palette
- **ProjectCardGrid**: Grid layout for batch processing display
- **QualityScoreBadge**: 0-100% score with color-coded background (red <50, yellow 50-69, green ≥70)
- **InlineEditor**: Rich text editor with AI highlight toggle
- **UploadZone**: Drag-and-drop with validation state

**Detailed specifications**: See `docs/figma-design-specifications.md` for:
- Complete color palette (primary, secondary, semantic colors)
- Typography scale (heading levels, body text, captions)
- Component anatomy (dimensions, spacing, states)
- Screen layouts with ASCII diagrams and measurements
- MUI theme configuration code snippet

### 3.6 Accessibility Requirements

**WCAG 2.1 Level AA Compliance**:
- **Keyboard Navigation**: All interactive elements (buttons, links, form fields) must be keyboard accessible with visible focus indicators (2px yellow outline)
- **Screen Reader Support**: All images have alt text, form fields have labels, status updates announced via ARIA live regions
- **Color Contrast**: Minimum 4.5:1 ratio for text (Navy #2C3E50 on white backgrounds meets this)
- **Focus Management**: Logical tab order, focus trapped in modals, focus restored after actions
- **Error Identification**: Validation errors announced to screen readers with `role="alert"`

**Testing**: Manual testing with NVDA/JAWS screen readers and keyboard-only navigation required before launch.

### 3.7 Responsive Design Strategy

**Primary Platform**: Desktop Web (1366×768 minimum, optimized for 1920×1080)
- Full feature set including upload, real-time processing, inline editing, export

**Secondary Platform**: Tablet (768px-1365px)
- View-only Dashboard and Results screens
- Upload and editing require desktop (show "Użyj komputera do edycji" message)

**Tertiary Platform**: Mobile (≤767px)
- Dashboard list view only
- No upload, processing, or editing functionality
- "Ta funkcja wymaga komputera" message for restricted features

**Rationale**: Consultants perform primary work on desktop computers. Mobile/tablet support enables checking status on-the-go but not full workflow (per user research in brief).

### 3.8 Platform and Browser Support

**Supported Browsers**:
- Chrome/Edge (Chromium) 90+
- Firefox 88+
- Safari 14+

**Operating Systems**:
- Windows 10+
- macOS 11+
- Linux (Ubuntu 20.04+ with supported browsers)

**Not Supported**:
- Internet Explorer (EOL)
- Mobile browsers for editing (view-only acceptable)

### 3.9 UI Goals Summary

The user interface design aims to:
1. **Reduce cognitive load** through linear workflow and glanceable status displays
2. **Build trust** through transparency (quality scores, AI highlights, clear errors)
3. **Enable speed** through keyboard shortcuts, default paths, and parallel processing visibility
4. **Ensure accessibility** for all consultant personas regardless of technical skill
5. **Reflect brand** through consistent iNOV visual identity (yellow/navy, light bulb motif)
6. **Support quality** through inline editing, section regeneration, and real-time score updates

**Success Metrics** (measurable post-launch):
- Average time from upload to first download: <10 minutes
- Consultant satisfaction with UI clarity: ≥4.5/5 (survey)
- Accessibility audit score: ≥95% WCAG 2.1 AA compliance
- Error recovery success rate: ≥90% (users who encounter errors successfully resolve them)

---

**References**:
- Detailed UX specification: `docs/front-end-spec.md`
- Visual design system: `docs/figma-design-specifications.md`
- User research and personas: `docs/brief.md` (Section 3)

---

## 4. Technical Assumptions

This section documents the technical assumptions and constraints that inform the architecture and implementation. These assumptions are based on the technology research report (`docs/technology-research-report.md`) and represent the foundational technical decisions for the MVP.

### 4.1 Technology Stack Assumptions

#### Frontend Technology
- **Framework**: React 18+ with TypeScript
- **UI Library**: Material-UI (MUI) v5 with custom iNOV theme
- **State Management**: React Context API + React Query for API state
- **File Handling**: react-dropzone (drag-and-drop) + SheetJS (xlsx parsing)
- **Build & Deployment**: Vite bundler, deployed to Vercel or AWS S3 + CloudFront

**Assumptions**:
- Modern browsers only (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- No IE11 support required
- Users have JavaScript enabled
- Desktop-first development approach (mobile is secondary)

#### Backend Technology
- **Runtime**: Python 3.11+
- **Framework**: FastAPI for REST API
- **Document Processing**: python-docx (Word generation), pandas + openpyxl (Excel parsing)
- **Task Queue**: Celery + Redis for asynchronous batch processing
- **Deployment**: Docker containers on AWS ECS Fargate or Azure Container Apps

**Assumptions**:
- python-docx library can replicate Ulga B+R template structure (validated in tech research POC)
- Celery provides sufficient reliability for batch job management
- FastAPI automatic OpenAPI documentation will serve as API contract

#### Database & Storage
- **Primary Database**: PostgreSQL 15+ for metadata and user sessions
- **File Storage**: AWS S3 (EU-Central-1 region) with lifecycle policies
- **Cache**: Redis 7+ for session cache and Celery message broker

**Assumptions**:
- 90-day data retention is sufficient (per NFR17)
- S3 eventual consistency acceptable for file operations
- PostgreSQL JSONB sufficient for storing generated content and quality metadata

#### AI Services
- **Primary LLM**: Claude 3.5 Sonnet via AWS Bedrock (EU-Central-1)
- **Fallback LLM**: GPT-4 via Azure OpenAI Service (West Europe region)
- **Context Window**: 200K tokens (Claude), 128K tokens (GPT-4)
- **Temperature**: 0.4-0.6 for balanced creativity and consistency

**Assumptions**:
- Claude 3.5 Sonnet maintains current Polish language quality levels
- AWS Bedrock and Azure OpenAI Service maintain ≥99.9% availability
- Token pricing remains stable (Claude: $3/$15 per 1M input/output tokens)
- Average generation requires 11,000-15,000 input tokens + 2,800-4,150 output tokens
- Cost per document: €0.80-1.50 including retries and infrastructure overhead

### 4.2 GDPR and Data Compliance Assumptions

**Geographic Constraints**:
- All data processing occurs within EU borders (AWS EU-Central-1 or Azure West Europe)
- No data transmitted to US-based AI APIs (use AWS Bedrock/Azure OpenAI only)
- Data Processing Agreements (DPAs) signed with AWS and Azure

**Data Retention**:
- Uploaded Excel files: 90 days auto-deletion
- Generated Word documents: 30 days auto-deletion (or immediate post-download)
- API logs: 6 months retention for debugging
- Database backups: 1 year encrypted retention in EU region

**Opt-Out Policies**:
- AWS Bedrock: Customer data NOT used for model training (per AWS policy)
- Azure OpenAI: Data retention disabled for EU deployments

**Assumptions**:
- AWS and Azure maintain GDPR compliance certifications
- Automated S3 lifecycle policies reliably delete expired data
- PostgreSQL contains no PII beyond hashed user identifiers
- No manual intervention required for data deletion compliance

### 4.3 AI Model Assumptions

#### Prompt Engineering Approach
**Architecture**: Multi-stage sequential generation (3 stages)
1. **Stage 1**: Project analysis and R&D identification (~2,000-3,000 tokens)
2. **Stage 2**: Section-by-section generation (7 sections × 500-800 tokens each)
3. **Stage 3**: Coherence review and compliance validation (~1,000-1,500 tokens)

**Few-Shot Learning**:
- 2-3 example project cards included in every prompt
- Examples selected based on domain similarity (construction → construction, IT → IT)
- Total example tokens: 8,000-10,000 per generation

**Grounding Strategy**:
- Strict prompt instructions emphasizing "use only provided data"
- Automated fact-checking against input Excel data
- Low-confidence sections flagged with `[WYMAGA WERYFIKACJI]` markers

**Assumptions**:
- 2-3 examples provide sufficient few-shot context (vs. 5-10 examples)
- Multi-stage approach reduces hallucination risk vs. single-prompt generation
- Temperature 0.4-0.6 balances quality and consistency
- Low-confidence flagging detectable via AI self-reflection prompts

#### Model Performance Expectations

**Polish Language Quality**:
- Grammar error rate: <2 errors per 1,000 words
- Technical terminology accuracy: ≥90% correct usage
- Professional tone consistency: ≥95% of outputs
- Consultant satisfaction: ≥4/5 rating

**Compliance Coverage**:
- 100% of outputs address "celowość" (purposefulness)
- 100% of outputs address "element twórczy" (creative element)
- 100% of outputs address "nowa wiedza" (new knowledge)
- Automated compliance checks validate keyword presence

**Output Consistency**:
- ±15-20% variance in phrasing across similar projects (acceptable)
- Structural consistency: 100% (all 8 sections present)
- Length variance: ±30% acceptable per section (based on input data richness)

**Assumptions**:
- Claude 3.5 Sonnet and GPT-4 maintain current capabilities through 2026
- Quality degrades gracefully with sparse input data (flagged for consultant attention)
- Native Polish speakers on QA team validate quality during pilot phase

### 4.4 Infrastructure and Deployment Assumptions

#### Cloud Provider
**Primary**: AWS (EU-Central-1 Frankfurt region)
**Secondary**: Azure (West Europe) for AI fallback only

**Services Used**:
- AWS Bedrock (Claude 3.5 Sonnet)
- AWS S3 (file storage with lifecycle policies)
- AWS RDS PostgreSQL (metadata database)
- AWS ECS Fargate (serverless containers for backend)
- AWS ElastiCache Redis (cache + Celery broker)
- AWS CloudFront (CDN for frontend assets)
- AWS CloudWatch (logging and monitoring)

**Assumptions**:
- AWS maintains EU data residency guarantees
- Fargate provides sufficient compute for 5 concurrent AI requests
- CloudFront CDN acceptable latency for Polish users (<100ms to Warsaw)
- CloudWatch logging sufficient for debugging (no third-party APM required for MVP)

#### Scalability Targets (MVP Phase)
- **Concurrent Users**: ≤50 consultants
- **Batch Processing**: 5 parallel AI requests (per FR7)
- **Monthly Volume**: 100-500 project cards generated
- **Storage**: 10GB Excel files + 20GB Word documents (with 90-day rotation)

**Assumptions**:
- Single ECS task (2 vCPU, 4GB RAM) sufficient for MVP scale
- Single PostgreSQL instance (db.t4g.medium) handles metadata load
- No horizontal scaling required until >1,000 cards/month
- Vertical scaling (larger instances) acceptable for growth

#### CI/CD and Development Workflow
- **Version Control**: Git + GitHub
- **CI/CD Pipeline**: GitHub Actions
- **Automated Testing**: pytest (backend), Jest + React Testing Library (frontend)
- **Infrastructure as Code**: Terraform or AWS CDK
- **Deployment Strategy**: Blue-green deployment for zero-downtime updates

**Assumptions**:
- GitHub Actions free tier sufficient for MVP CI/CD
- Automated tests cover ≥80% code coverage before production deployment
- Infrastructure can be torn down and recreated via IaC for disaster recovery

### 4.5 Security Assumptions

**Authentication & Authorization**:
- **MVP**: Simple email/password authentication (specific implementation TBD by Architect)
- **Future**: Consider OAuth2/SSO for enterprise clients
- **Session Management**: JWT tokens with 24-hour expiry
- **Access Control**: Per-user isolation (consultants see only their own batches)

**Data Security**:
- **Encryption in Transit**: TLS 1.3 for all HTTPS connections
- **Encryption at Rest**: AWS S3 SSE-S3, RDS encryption enabled
- **API Security**: Rate limiting (100 requests/min per user), CORS policies
- **Input Validation**: Server-side validation of all Excel uploads (prevent injection attacks)

**Assumptions**:
- No multi-tenancy required for MVP (each consultant is independent user)
- No need for role-based access control (RBAC) in MVP
- AWS managed security services sufficient (no WAF required initially)
- Excel file malware scanning handled by AWS S3 antivirus integration (optional, recommended)

### 4.6 Integration and Dependency Assumptions

**Third-Party Dependencies**:
- AWS Bedrock API availability: ≥99.9%
- Azure OpenAI API availability: ≥99.5% (fallback only)
- Material-UI library updates: No breaking changes in v5.x minor versions
- python-docx library stability: No breaking changes in 1.x versions

**Browser Compatibility**:
- Modern ES6+ JavaScript supported natively
- No polyfills required for target browsers (Chrome 90+, Firefox 88+, Safari 14+)
- WebAssembly not required
- Local storage available for session persistence

**Assumptions**:
- No on-premises deployment required (cloud-only acceptable for target users)
- Consultants have reliable internet connectivity (≥5 Mbps download, ≥1 Mbps upload)
- No offline mode required for MVP
- Desktop browsers primary target (mobile web view-only acceptable per NFR14)

### 4.7 Quality and Testing Assumptions

**Automated Quality Validation**:
- **Compliance Check**: Automated keyword validation for celowość, element twórczy, nowa wiedza
- **Section Completeness**: Verify all 8 required sections present
- **Polish Grammar**: Basic automated grammar checking using LanguageTool (pl-PL)
- **Fact-Checking**: Validate generated content against input Excel data (no date/name mismatches)

**Manual Review Workflow**:
- Consultant reviews 100% of generated content before download (per FR10-FR12)
- Quality score (0-100%) guides review prioritization (low-scoring cards reviewed first)
- Consultant edits tracked to measure "70% AI-generated" success metric (per NFR3)

**Testing Strategy**:
- **Unit Tests**: ≥80% code coverage for backend logic, ≥70% for frontend components
- **Integration Tests**: End-to-end Excel upload → AI generation → Word download
- **Quality Validation**: Use 60+ existing example cards as test dataset
- **Load Testing**: Simulate 50 concurrent users processing 20-card batches

**Assumptions**:
- 60+ example cards in brief.md sufficient for training prompt engineering
- Native Polish speaker available for quality validation during development
- Consultant pilot users provide feedback on AI quality (target: 10-15 pilot users)
- Quality scoring algorithm correlates with consultant satisfaction (validate during pilot)

### 4.8 Performance Assumptions

**Target Performance Metrics** (per NFR1-NFR7):
- Individual card generation: 1 minute average, 15 minutes maximum
- Batch of 20 cards: ≤30 minutes total (5 parallel × 6 minutes per wave)
- Dashboard load time: <1 second
- UI interaction response: <200ms
- Real-time status updates: Every 2 seconds

**Bottleneck Analysis**:
- **AI API Latency**: Assumed 30-90 seconds per Claude/GPT-4 call (largest bottleneck)
- **Word Generation**: Assumed <5 seconds per document (python-docx)
- **Excel Parsing**: Assumed <2 seconds for 20-row file
- **Database Queries**: Assumed <50ms per query (simple CRUD operations)

**Assumptions**:
- AI API latency dominates total generation time (other components negligible)
- 5 parallel requests sufficient to meet 30-minute batch target
- Network latency from Poland to AWS EU-Central-1: <50ms
- CloudFront CDN reduces frontend asset load time by 40-60%

### 4.9 Cost Assumptions

**AI Cost Model** (per document):
- Base AI cost: €0.08-0.11 (11,000-15,000 input tokens + 2,800-4,150 output tokens)
- Retry/refinement buffer (30%): €0.02-0.03
- **Total AI cost: €0.10-0.14 per document**

**Infrastructure Cost Model** (monthly, 100 docs/month):
- AWS Bedrock (AI): €80-150
- AWS ECS Fargate: €50-100
- AWS RDS PostgreSQL: €30-50
- AWS S3 + CloudFront: €15-30
- AWS ElastiCache Redis: €20-30
- Monitoring/Logs: €10-20
- **Total infrastructure: €205-380/month**

**Per-Document Total Cost** (infrastructure amortized):
- AI: €0.10-0.14
- Infrastructure: €2.05-3.80 (for 100 docs/month)
- **Total: €2.15-3.94 per document**

**Cost Scaling Assumptions**:
- Infrastructure costs grow sub-linearly (€1-2 per doc at 500 docs/month due to economies of scale)
- AI costs scale linearly with volume
- Break-even pricing: €5-8 per document (assuming 50% gross margin target)

**Assumptions**:
- Token pricing remains stable through 2026
- No significant prompt optimization beyond initial engineering (30% retry buffer holds)
- Prompt caching (if available) could reduce costs by 40-50% (not assumed for MVP)

### 4.10 Constraints and Limitations

**Known Limitations**:
1. **Batch Size**: Maximum 20 projects per batch (Excel row limit per FR2)
2. **Concurrent Processing**: Maximum 5 parallel AI requests (rate limit constraint per NFR16)
3. **File Size**: Excel files ≤5MB, Word exports ≤2MB (per NFR9-NFR10)
4. **Data Retention**: 90 days for inputs, 30 days for outputs (GDPR compliance per NFR17)
5. **Browser Support**: Desktop-only editing (mobile view-only per NFR14)
6. **Language**: Polish-only UI and content (no internationalization for MVP)

**Technical Debt Accepted for MVP**:
- No fine-tuning of AI models (use general-purpose Claude/GPT-4 with few-shot prompts)
- No advanced analytics dashboard (basic quality metrics only)
- No collaborative editing (single consultant per batch)
- No version history for project cards (single generation, download, done)
- No API for third-party integrations (web UI only)

**Assumptions**:
- MVP limitations acceptable to pilot users (validated during user research)
- Technical debt can be addressed in Phase 2 based on user feedback
- 20-project batch limit sufficient for 95% of use cases (per brief.md user research)

### 4.11 Risks and Dependencies

**Critical Technical Risks**:
1. **AI Hallucination** (HIGH): Mitigation via strict prompt grounding, automated fact-checking, mandatory consultant review
2. **Polish Language Quality Variance** (MEDIUM): Mitigation via multi-model approach, native speaker QA, quality scoring
3. **API Availability/Outages** (MEDIUM-HIGH): Mitigation via multi-provider architecture, automatic failover, queue-based processing
4. **Token Cost Escalation** (MEDIUM): Mitigation via real-time cost monitoring, budget alerts, prompt optimization

**External Dependencies**:
- AWS Bedrock service availability and pricing stability
- Azure OpenAI service availability (fallback)
- Python ecosystem stability (FastAPI, python-docx, Celery)
- React and Material-UI ecosystem stability
- Polish government Ulga B+R template requirements (assumed stable for 12+ months)

**Assumptions**:
- No dependency becomes unavailable or prohibitively expensive during MVP development
- Alternative solutions exist for each critical dependency (fallback models, alternative libraries)
- Polish tax law changes announced with ≥6 months notice (time to adapt templates)

---

**References**:
- Complete technology research: `docs/technology-research-report.md`
- Cost analysis: Section 2 and Appendix B of technology report
- Risk assessment: Section 8 of technology report
- Proof-of-concept validation: Section 4 of technology report

---

## 5. Epic List

This section organizes the product requirements into high-level epics that represent major functional areas. Each epic groups related user stories and represents a cohesive deliverable that provides value to users.

### Epic Prioritization Framework

**Priority Levels**:
- **P0 (Critical)**: Required for MVP launch, blocks core workflow
- **P1 (High)**: Essential for MVP, enhances core experience
- **P2 (Medium)**: Important but can be deferred post-MVP
- **P3 (Low)**: Nice-to-have, future enhancement

**Sequencing Strategy**: P0 epics must be completed first, P1 epics complete MVP, P2-P3 are post-MVP roadmap.

---

### Epic 1: Excel Template & Data Upload
**Priority**: P0 (Critical)
**Effort**: Medium (2-3 weeks)
**Dependencies**: None
**Risk**: Low

**Description**:
Enable consultants to upload Excel files containing project data for batch processing. This epic includes providing a downloadable Excel template with validation rules, drag-and-drop upload functionality, and comprehensive data validation to ensure quality inputs for AI generation.

**Key Capabilities**:
- Download Excel template with Polish headers, example data, and validation rules
- Drag-and-drop file upload with fallback file picker
- Client-side Excel parsing and initial validation
- Server-side comprehensive validation (column presence, data types, content length, date logic)
- Row-level error reporting with Polish error messages
- Support 1-20 projects per batch

**Requirements Addressed**:
- FR1: Excel file upload with required columns
- FR2: Validation (columns, data types, content length, date logic, row count)
- FR3: Validation error display with row numbers
- FR4: Downloadable Excel template
- FR5: Row-by-row processing

**Success Metrics**:
- Template download available on Dashboard and Upload screen
- Upload validation catches 95%+ of data quality issues before generation
- Clear error messages enable 90%+ self-service error resolution
- Upload flow completable in <2 minutes for valid files

**User Value**:
Consultants can quickly prepare batches using a structured template, preventing "garbage in, garbage out" and reducing generation errors.

---

### Epic 2: AI-Powered Project Card Generation
**Priority**: P0 (Critical)
**Effort**: High (4-6 weeks)
**Dependencies**: Epic 1 (data upload)
**Risk**: High (AI quality, hallucination risk)

**Description**:
Core AI generation engine that transforms Excel input data into Polish-language Ulga B+R project cards. This epic includes prompt engineering, multi-stage generation workflow, integration with Claude 3.5 Sonnet and GPT-4, quality scoring, and automated compliance validation.

**Key Capabilities**:
- Multi-stage AI generation (analysis → sections → review)
- Polish-language project card generation with 8 required sections
- Few-shot prompting with 2-3 example cards
- Automated compliance validation (celowość, element twórczy, nowa wiedza)
- Quality scoring algorithm (0-100%)
- Multi-model support (Claude primary, GPT-4 fallback)
- Hallucination prevention via grounding prompts
- Automated fact-checking against input data

**Requirements Addressed**:
- FR6: Polish-language generation following Ulga B+R template
- FR9: Quality score calculation (0-100%)
- FR12: Section regeneration with alternative models
- NFR3: ≥70% AI-generated content quality
- NFR16: Rate-limiting (max 5 concurrent API calls)

**Success Metrics**:
- ≥70% of generated content requires ≤30% consultant editing (per NFR3)
- Quality score ≥70 for 80%+ of generated cards
- Polish grammar error rate <2 per 1,000 words
- 100% compliance coverage (all 3 criteria addressed)
- Average generation time ≤1 minute (target), ≤15 minutes (max)

**User Value**:
Consultants save 15-30 hours per batch by automating content generation while maintaining professional quality and compliance.

---

### Epic 3: Batch Processing & Status Tracking
**Priority**: P0 (Critical)
**Effort**: Medium (2-3 weeks)
**Dependencies**: Epic 1, Epic 2
**Risk**: Medium (async processing complexity)

**Description**:
Asynchronous batch processing system that handles 1-20 projects concurrently with real-time status updates. This epic includes queue management, parallel AI request handling (5 concurrent), progress tracking, error recovery, and time estimation.

**Key Capabilities**:
- Queue-based batch processing (Celery + Redis)
- Parallel processing (5 concurrent AI requests)
- Real-time status updates (every 2 seconds)
- Per-project status display (Oczekuje → Generowanie → Gotowe → Błąd)
- Overall batch progress tracking
- Estimated time remaining calculation
- Automatic retry for failed generations (3 attempts with exponential backoff)
- Graceful handling of API failures
- Resume incomplete batches

**Requirements Addressed**:
- FR7: Process up to 5 projects concurrently
- FR8: Real-time processing status display
- FR18: Estimated time remaining
- FR19: Graceful AI API failure handling
- NFR1: ≤1 minute average generation time
- NFR2: 20 projects in ≤30 minutes
- NFR7: Status updates every ≤2 seconds

**Success Metrics**:
- Batch of 20 projects completes in ≤30 minutes (per NFR2)
- Status updates visible within 2 seconds of state changes
- Failed generations retry automatically with 90%+ eventual success
- Users can navigate away and resume batch processing

**User Value**:
Consultants can start batches and monitor progress transparently without blocking their workflow, with automatic recovery from transient failures.

---

### Epic 4: Review & Editing Interface
**Priority**: P0 (Critical)
**Effort**: Medium-High (3-4 weeks)
**Dependencies**: Epic 2, Epic 3
**Risk**: Medium (editing UX complexity)

**Description**:
Inline review and editing interface that allows consultants to review AI-generated content, make edits, track changes, regenerate sections, and approve project cards. This epic includes rich text editing, quality score updates, AI highlight tracking, and section-level regeneration.

**Key Capabilities**:
- Sidebar list of all projects in batch with quality scores
- Section-by-section content display (8 sections)
- Inline rich text editor (edit directly in interface)
- Real-time quality score recalculation as edits are made
- Visual distinction between AI-generated (yellow highlight) and edited (white) content
- Section-level regeneration with optional hints
- Alternative model selection (Claude vs GPT-4)
- Timestamp tracking for edits
- Section approval workflow ("Approved" vs "Needs Work")

**Requirements Addressed**:
- FR10: Inline review interface with editing
- FR11: Visual distinction (yellow = AI, white = edited)
- FR12: Section regeneration with hints and model selection
- FR9: Quality score display and updates

**Success Metrics**:
- Consultants can complete review/edit of 20 cards in ≤3 hours
- Quality score updates within 1 second of edit
- Section regeneration completes in ≤2 minutes
- User satisfaction with editing interface ≥4.5/5

**User Value**:
Consultants maintain full control over final content quality while benefiting from AI acceleration, with transparency into what AI generated vs. what they edited.

---

### Epic 5: Word Document Export
**Priority**: P0 (Critical)
**Effort**: Medium (2-3 weeks)
**Dependencies**: Epic 2, Epic 4
**Risk**: Medium (template formatting complexity)

**Description**:
Export completed project cards to Word (.docx) format matching the official Ulga B+R template layout. This epic includes python-docx integration, template structure replication, government-compliant formatting, and batch export (ZIP).

**Key Capabilities**:
- Generate Word documents using python-docx
- Match official Ulga B+R template structure (tables, sections, formatting)
- Apply government-compliant styling (fonts, margins, headers/footers)
- Include consultant and client company information
- Single project download (.docx)
- Batch download (ZIP with multiple .docx files)
- File naming convention: "Projekt-{Nazwa projektu}-{YYYY-MM-DD}.docx"

**Requirements Addressed**:
- FR13: Word export with Ulga B+R template formatting
- FR14: Batch export as ZIP
- NFR10: Word documents ≤2MB per card

**Success Metrics**:
- Generated .docx files visually match official template (validated by consultants)
- Export completes in ≤10 seconds per document
- File size ≤2MB per card (per NFR10)
- No formatting errors requiring manual Word fixes

**User Value**:
Consultants receive government-ready Word documents that can be directly submitted or shared with clients without additional formatting work.

---

### Epic 6: Dashboard & Batch Management
**Priority**: P1 (High)
**Effort**: Low-Medium (1-2 weeks)
**Dependencies**: Epic 3, Epic 5
**Risk**: Low

**Description**:
Central dashboard providing overview of recent batches, status tracking, and batch management capabilities. This epic includes batch history, session persistence, archive/delete functionality, and navigation to active batches.

**Key Capabilities**:
- Dashboard view as home screen
- Recent batches list (last 10) with status, date, project count
- Batch status indicators (In Progress, Completed, Archived)
- Average quality score per batch
- Click batch to resume or view results
- Save incomplete batches (90-day persistence)
- Archive/delete completed batches (>30 days)
- "Nowa partia" (New Batch) prominent CTA

**Requirements Addressed**:
- FR15: Save generation sessions for 90 days
- FR16: Dashboard with recent batches and status
- FR17: Delete/archive old batches
- NFR6: Dashboard loads in ≤1 second

**Success Metrics**:
- Dashboard loads in <1 second (per NFR6)
- Users can locate and resume batches in ≤3 clicks
- Batch persistence enables 95%+ completion rate (resume after interruption)

**User Value**:
Consultants have clear visibility into all their work, can easily resume interrupted batches, and maintain organized workspace.

---

### Epic 7: Quality Assurance & Validation
**Priority**: P1 (High)
**Effort**: Medium (2-3 weeks)
**Dependencies**: Epic 2
**Risk**: Medium (validation accuracy)

**Description**:
Automated quality validation system that checks generated content for compliance, completeness, Polish grammar, and fact accuracy. This epic includes quality scoring algorithm, automated checks, and flagging low-confidence sections.

**Key Capabilities**:
- Compliance validation (celowość, element twórczy, nowa wiedza keyword checks)
- Section completeness check (all 8 sections present)
- Polish grammar checking (LanguageTool integration)
- Fact-checking against input Excel data (dates, names, project titles)
- Quality scoring algorithm (0-100%)
- Low-confidence section flagging
- Quality report per project card

**Requirements Addressed**:
- FR9: Quality score calculation
- FR20: Logging AI API calls for debugging
- NFR3: ≥70% usable content quality

**Success Metrics**:
- Quality score correlates with consultant satisfaction (≥0.7 correlation)
- Automated checks catch 80%+ of major issues
- Grammar checks identify real errors with ≤10% false positive rate
- Fact-checking prevents 95%+ of data inconsistencies

**User Value**:
Consultants receive automated quality feedback that guides their review prioritization, focusing effort on low-quality cards.

---

### Epic 8: User Authentication & Security
**Priority**: P1 (High)
**Effort**: Low-Medium (1-2 weeks)
**Dependencies**: None (parallel to Epic 1)
**Risk**: Low

**Description**:
Basic authentication system to control access and ensure per-user data isolation. This epic includes email/password authentication, session management, and secure data access patterns.

**Key Capabilities**:
- Email/password user registration and login
- JWT token-based session management (24-hour expiry)
- Password reset flow
- Per-user data isolation (consultants see only their batches)
- Secure session storage
- Logout functionality

**Requirements Addressed**:
- NFR18: Authentication to prevent unauthorized access
- NFR15: TLS 1.3 encryption in transit

**Success Metrics**:
- Login flow completable in ≤30 seconds
- Zero cross-user data leakage (security testing)
- Session expiry handled gracefully (auto-redirect to login)

**User Value**:
Consultants can securely access their work from any device without risk of data exposure to other users.

---

### Epic 9: GDPR Compliance & Data Management
**Priority**: P1 (High)
**Effort**: Low-Medium (1-2 weeks)
**Dependencies**: All data storage epics
**Risk**: Medium (compliance risk)

**Description**:
GDPR-compliant data handling including EU-only processing, automated data retention policies, encryption, and audit logging. This epic ensures legal compliance for processing sensitive client data.

**Key Capabilities**:
- EU-only data processing (AWS EU-Central-1, Azure West Europe)
- Automated data lifecycle policies (90-day Excel, 30-day Word, 6-month logs)
- S3 lifecycle rules for auto-deletion
- Encryption at rest (S3 SSE-S3, RDS encryption)
- Encryption in transit (TLS 1.3)
- API call logging and audit trails
- Data Processing Agreements with AWS/Azure

**Requirements Addressed**:
- NFR15: TLS 1.3 encryption
- NFR17: 90-day data retention with auto-deletion
- Technical Assumptions 4.2: GDPR compliance

**Success Metrics**:
- 100% of data processed within EU borders
- Automated deletion policies tested and functioning
- GDPR compliance audit passes with zero critical findings
- Encryption verified for all data at rest and in transit

**User Value**:
Consultants can confidently use the system with sensitive client data knowing it meets Polish/EU data protection requirements.

---

### Epic 10: Error Recovery & Help System
**Priority**: P2 (Medium)
**Effort**: Low (1 week)
**Dependencies**: Epic 1, Epic 3
**Risk**: Low

**Description**:
Comprehensive error handling and user guidance to help consultants recover from failures and understand how to use the system effectively.

**Key Capabilities**:
- Clear Polish-language error messages
- Contextual help for validation errors (with template download link)
- Retry functionality for failed generations
- Error recovery screen with guidance
- In-app tooltips and hints
- Link to documentation/FAQ

**Requirements Addressed**:
- FR3: Clear validation error messages
- FR19: Graceful error handling with manual retry

**Success Metrics**:
- ≥90% of users who encounter errors successfully recover without support
- Error messages rated ≥4/5 for clarity
- Support tickets for "how to fix errors" <5% of users

**User Value**:
Consultants can self-service error resolution without frustration or need for technical support.

---

### Epic 11: Performance Optimization & Monitoring
**Priority**: P2 (Medium)
**Effort**: Low-Medium (1-2 weeks)
**Dependencies**: All P0/P1 epics
**Risk**: Low

**Description**:
Performance monitoring, optimization, and alerting to ensure system meets speed targets and remains healthy in production.

**Key Capabilities**:
- CloudWatch monitoring dashboards
- Real-time performance metrics (API latency, generation time, queue depth)
- Cost tracking (tokens used, AI spend per document)
- Budget alerts (80% of monthly threshold)
- Error rate monitoring
- Uptime monitoring
- Slow query identification

**Requirements Addressed**:
- FR20: Log AI API calls for cost tracking
- NFR4: ≥99% uptime during Polish business hours
- NFR5: UI interactions ≤200ms
- Technical Assumptions 4.9: Cost monitoring

**Success Metrics**:
- Dashboard provides visibility into all key metrics
- Alerts fire before budget overruns (≥80% threshold)
- Performance regressions detected within 24 hours
- System uptime ≥99% (per NFR4)

**User Value**:
System remains fast and reliable, with proactive issue detection before user impact.

---

### Epic 12: Accessibility & Internationalization
**Priority**: P2 (Medium)
**Effort**: Medium (2 weeks)
**Dependencies**: All frontend epics
**Risk**: Low

**Description**:
WCAG 2.1 Level AA accessibility compliance and Polish language localization to ensure the system is usable by all consultants including those with disabilities.

**Key Capabilities**:
- Keyboard navigation for all functions
- Screen reader compatibility (ARIA labels, roles, live regions)
- Focus indicators (2px yellow outline)
- 4.5:1 color contrast ratios
- Error announcements for screen readers
- Polish language for all UI text and messages
- Logical tab order
- Focus management (modals, dialogs)

**Requirements Addressed**:
- NFR11: WCAG 2.1 Level AA compliance
- NFR12: Polish-language UI
- UI Goals 3.6: Accessibility requirements

**Success Metrics**:
- WCAG 2.1 AA audit score ≥95%
- All functions keyboard-accessible (zero mouse-only actions)
- Screen reader testing passes with NVDA/JAWS
- Color contrast violations = 0

**User Value**:
All consultants, including those with visual or motor impairments, can use the system effectively without barriers.

---

### Epic 13: Mobile & Responsive Design
**Priority**: P3 (Low)
**Effort**: Low-Medium (1-2 weeks)
**Dependencies**: All frontend epics
**Risk**: Low

**Description**:
Responsive design implementation to provide limited functionality on tablets and mobile devices for on-the-go status checking.

**Key Capabilities**:
- Responsive breakpoints (desktop, tablet, mobile)
- Tablet view-only Dashboard and Results (768-1365px)
- Mobile Dashboard list view (≤767px)
- "Użyj komputera" messages for restricted features
- Touch-friendly tap targets on mobile/tablet

**Requirements Addressed**:
- NFR13: Desktop browser support (≥1366×768)
- NFR14: Limited mobile browser support (view-only)
- UI Goals 3.7: Responsive design strategy

**Success Metrics**:
- Desktop experience fully functional at 1366×768+
- Tablet users can view Dashboard and Results without horizontal scroll
- Mobile users can check batch status
- Zero critical features broken on mobile (graceful degradation)

**User Value**:
Consultants can check batch status and view results on-the-go from tablets or phones without needing desktop access.

---

### Epic 14: Advanced AI Features (Post-MVP)
**Priority**: P3 (Low)
**Effort**: High (4-6 weeks)
**Dependencies**: Epic 2
**Risk**: High

**Description**:
Advanced AI capabilities including fine-tuning, multi-year project support, and advanced prompt optimization for improved quality and cost efficiency.

**Key Capabilities**:
- Fine-tune Claude/GPT-4 on 60+ example cards
- Multi-year project handling
- Prompt caching for cost optimization
- A/B testing of prompt strategies
- Model performance analytics
- Custom quality scoring models

**Requirements Addressed**:
- Future enhancements beyond MVP scope
- Cost optimization (Technical Assumptions 4.9)

**Success Metrics**:
- Fine-tuning improves quality score by ≥10 points
- Prompt caching reduces cost by 40-50%
- Multi-year projects handled correctly

**User Value**:
Improved AI quality and reduced costs enable better ROI and expanded use cases.

---

## Epic Summary Table

| Epic | Priority | Effort | Dependencies | Risk | MVP Phase |
|------|----------|--------|--------------|------|-----------|
| Epic 1: Excel Template & Data Upload | P0 | Medium (2-3w) | None | Low | ✅ Phase 1 |
| Epic 2: AI-Powered Project Card Generation | P0 | High (4-6w) | Epic 1 | High | ✅ Phase 1 |
| Epic 3: Batch Processing & Status Tracking | P0 | Medium (2-3w) | Epic 1, 2 | Medium | ✅ Phase 1 |
| Epic 4: Review & Editing Interface | P0 | Med-High (3-4w) | Epic 2, 3 | Medium | ✅ Phase 1 |
| Epic 5: Word Document Export | P0 | Medium (2-3w) | Epic 2, 4 | Medium | ✅ Phase 1 |
| Epic 6: Dashboard & Batch Management | P1 | Low-Med (1-2w) | Epic 3, 5 | Low | ✅ Phase 2 |
| Epic 7: Quality Assurance & Validation | P1 | Medium (2-3w) | Epic 2 | Medium | ✅ Phase 2 |
| Epic 8: User Authentication & Security | P1 | Low-Med (1-2w) | None | Low | ✅ Phase 2 |
| Epic 9: GDPR Compliance & Data Management | P1 | Low-Med (1-2w) | All storage | Medium | ✅ Phase 2 |
| Epic 10: Error Recovery & Help System | P2 | Low (1w) | Epic 1, 3 | Low | Post-MVP |
| Epic 11: Performance Optimization & Monitoring | P2 | Low-Med (1-2w) | All P0/P1 | Low | Post-MVP |
| Epic 12: Accessibility & Internationalization | P2 | Medium (2w) | All frontend | Low | Post-MVP |
| Epic 13: Mobile & Responsive Design | P3 | Low-Med (1-2w) | All frontend | Low | Future |
| Epic 14: Advanced AI Features | P3 | High (4-6w) | Epic 2 | High | Future |

**Total MVP Effort Estimate**: 23-33 weeks (5.5-8 months) with single full-stack developer

**Critical Path**: Epic 1 → Epic 2 → Epic 3 → Epic 4 → Epic 5 (16-22 weeks core functionality)

---

## 6. PRD Validation Checklist Results

This section documents the comprehensive validation of this PRD against the BMad Method PM Checklist to ensure readiness for the architecture phase.

### Executive Summary

**Overall PRD Completeness**: 95% ✅

**MVP Scope Appropriateness**: Just Right ✅
- P0/P1 epics represent true MVP scope (9 epics, ~23-33 weeks)
- P2/P3 clearly deferred to post-MVP
- Core workflow complete: Upload → AI Generate → Review → Export

**Readiness for Architecture Phase**: READY ✅
- All critical requirements documented with clarity
- Technical assumptions from research report integrated
- No blocking gaps identified
- UX specifications complete and referenced

**Most Critical Observations**:
1. ✅ **Strength**: Excellent technical foundation from comprehensive tech research report
2. ✅ **Strength**: Clear GDPR compliance requirements with EU-only processing
3. ⚠️ **Note**: Epic 2 (AI Generation) carries HIGH risk due to quality variance - requires careful prompt engineering and pilot testing
4. ⚠️ **Note**: No detailed user stories provided (intentionally deferred per BMad workflow - will be created during story sharding)

### Category Analysis

| Category | Status | Critical Issues | Notes |
|----------|--------|-----------------|-------|
| 1. Problem Definition & Context | **PASS** ✅ | None | Clear problem statement with 20-40 hour manual work quantified; 3 personas defined; success metrics measurable |
| 2. MVP Scope Definition | **PASS** ✅ | None | P0/P1 clearly separated from P2/P3; rationale documented; 14 epics with explicit priorities |
| 3. User Experience Requirements | **PASS** ✅ | None | Complete UX spec in separate doc (72KB); 5 core screens; accessibility WCAG 2.1 AA; Figma design specs complete |
| 4. Functional Requirements | **PASS** ✅ | None | 20 FRs covering complete workflow; testable and specific; mapped to epics |
| 5. Non-Functional Requirements | **PASS** ✅ | None | 20 NFRs with measurable targets (1min/card, 70% quality, 99% uptime, WCAG AA) |
| 6. Epic & Story Structure | **PASS** ✅ | None | 14 epics with priorities, effort, dependencies, risks, success metrics; user stories deferred to sharding phase per BMad |
| 7. Technical Guidance | **PASS** ✅ | None | Complete tech stack from research report; AWS/Azure architecture; cost model (€2-4/doc); GDPR compliance detailed |
| 8. Cross-Functional Requirements | **PASS** ✅ | None | Data retention policies (90 days); PostgreSQL + S3 storage; API integrations (AWS Bedrock, Azure OpenAI) |
| 9. Clarity & Communication | **PASS** ✅ | None | Well-structured, consistent terminology, references to supporting docs (brief, tech report, UX spec, Figma) |

**Overall Assessment**: All 9 categories PASS with ≥90% completeness

### Top Issues by Priority

#### BLOCKERS
**None identified** - PRD is ready for architecture phase

#### HIGH Priority Observations
1. **AI Quality Risk (Epic 2)**: HIGH risk due to hallucination and Polish language variance
   - **Mitigation Documented**: Multi-stage prompts, grounding instructions, automated fact-checking, mandatory consultant review
   - **Recommendation**: Architect should include AI quality monitoring and prompt versioning in architecture
   - **Action**: Plan 2-week POC sprint (per tech report Section 10.2) to validate quality before full development

2. **Authentication Implementation TBD**: NFR18 specifies authentication required but implementation method deferred to Architect
   - **Status**: Acceptable - Architect will specify (email/password vs OAuth2 vs SSO)
   - **Guidance Provided**: Section 4.5 specifies JWT tokens, 24-hour expiry, per-user isolation
   - **Action**: Architect to select auth method in architecture document

#### MEDIUM Priority Improvements
1. **No Visual Diagrams in PRD**: Epic dependencies and workflow could benefit from visual diagrams
   - **Status**: Acceptable - Mermaid diagrams exist in UX spec; Architect will create system architecture diagrams
   - **Optional Enhancement**: Could add epic dependency graph to Section 5

2. **User Stories Not Detailed**: Epic list provides high-level capabilities but no granular user stories with acceptance criteria
   - **Status**: EXPECTED - BMad Method defers detailed user stories to sharding phase after Architect completes architecture
   - **Next Step**: Product Owner (PO) will shard PRD into story-level documents after architecture phase

#### LOW Priority Enhancements
1. **Cost Model Could Include Revenue Projections**: Section 4.9 documents costs (€2-4/doc) but not pricing strategy or revenue model
   - **Status**: Acceptable for MVP PRD - business model is separate concern
   - **Note**: Brief.md mentions potential €10-15 pricing, implying 50-66% margins

2. **Accessibility Testing Plan Could Be More Specific**: NFR11 requires WCAG 2.1 AA but Epic 12 deferred to P2 (post-MVP)
   - **Recommendation**: Consider elevating accessibility testing to P1 if target users include consultants with disabilities
   - **Current Status**: Acceptable - desktop web app with keyboard navigation meets baseline needs

### MVP Scope Assessment

#### True MVP Analysis
**Current P0/P1 Scope**: 9 epics, 23-33 weeks

**Scope Appropriateness**: ✅ **Just Right**

**Could Be Cut (if aggressive timeline required)**:
- Epic 7 (Quality Assurance & Validation) could be simplified - reduce automated grammar checking, keep compliance validation only
  - **Impact**: Consultant reviews become primary quality gate; saves 2-3 weeks
  - **Risk**: Lower quality scores, more consultant editing required
- Epic 9 (GDPR Compliance) could defer audit logging and focus only on EU regions + encryption
  - **Impact**: Saves 1 week; still GDPR compliant but with manual compliance verification
  - **Risk**: Compliance audit more manual

**Should NOT Be Cut**:
- All P0 epics (1-5) are critical path - removing any breaks core workflow
- Epic 8 (Authentication) is security-critical and low effort (1-2 weeks)
- Epic 6 (Dashboard) is essential for batch management - consultants need to resume work

**Missing from MVP**: None identified - scope is complete for stated problem

#### Complexity Concerns

**Highest Complexity Epics**:
1. **Epic 2 (AI Generation)** - 4-6 weeks, HIGH risk
   - Prompt engineering requires iteration
   - Quality validation needs native Polish speaker
   - Multi-model failover adds complexity
   - **Mitigation**: Well-researched (60+ examples, tech report POC), strong technical foundation

2. **Epic 4 (Review & Editing Interface)** - 3-4 weeks, MEDIUM risk
   - Rich text editing with real-time quality scoring
   - Yellow highlighting for AI vs edited content
   - Section regeneration UX
   - **Mitigation**: Existing UX spec with wireframes, standard React patterns

3. **Epic 3 (Batch Processing)** - 2-3 weeks, MEDIUM risk
   - Celery + Redis asynchronous processing
   - Real-time WebSocket updates every 2 seconds
   - Retry logic with exponential backoff
   - **Mitigation**: Well-established patterns, tech stack chosen for this capability

#### Timeline Realism

**Estimated Timeline**: 23-33 weeks (5.5-8 months) with single full-stack developer

**Assessment**: ✅ **Realistic but Aggressive**

**Assumptions Requiring Validation**:
- Developer has strong React + Python experience (if not, add 20-30% to timeline)
- Prompt engineering succeeds within 4-6 week window (high uncertainty)
- python-docx template matching requires ≤2 weeks (validated via POC in tech report)
- No major scope changes or feature creep during development

**Recommended Approach**:
1. **Phase 1 (P0 Critical Path)**: 16-22 weeks - Deliver core workflow end-to-end
2. **Pilot Testing**: 2-4 weeks - Test with 10-15 real consultants, gather feedback
3. **Phase 2 (P1 Completion)**: 7-11 weeks - Add Dashboard, Auth, GDPR, Quality validation
4. **MVP Launch**: Target 6-9 months from kickoff to production

### Technical Readiness

#### Clarity of Technical Constraints ✅
- **Frontend**: React 18+ TypeScript, Material-UI v5, Vercel deployment
- **Backend**: Python 3.11+, FastAPI, Celery, Docker on AWS ECS Fargate
- **AI**: Claude 3.5 Sonnet (AWS Bedrock EU-Central-1) + GPT-4 (Azure OpenAI West Europe)
- **Database**: PostgreSQL 15+, Redis 7+, S3 file storage with lifecycle policies
- **Compliance**: EU-only processing, TLS 1.3, 90-day retention

**Architect Flexibility**: Technology stack specified but Architect may propose alternatives with rationale

#### Identified Technical Risks ✅
1. **AI Hallucination** (HIGH) - Mitigation: Grounding prompts, fact-checking, mandatory review
2. **Polish Language Quality Variance** (MEDIUM) - Mitigation: Multi-model, native QA, quality scoring
3. **API Outages** (MEDIUM-HIGH) - Mitigation: Multi-provider, automatic failover, queue-based
4. **Token Cost Escalation** (MEDIUM) - Mitigation: Cost monitoring, budget alerts, prompt optimization

All risks documented with concrete mitigation strategies

#### Areas Needing Architect Investigation
1. **Authentication Method Selection**: Email/password vs OAuth2 vs SSO (guidance provided, final decision to Architect)
2. **WebSocket vs Polling for Real-Time Updates**: NFR7 requires 2-second status updates (Architect to choose mechanism)
3. **Database Schema Design**: PostgreSQL JSONB for metadata vs normalized tables (Architect to design)
4. **CI/CD Pipeline Details**: GitHub Actions specified, but pipeline stages and deployment strategy to be designed
5. **Monitoring Stack**: CloudWatch specified, but specific metrics, dashboards, alerts to be architected

**Assessment**: Appropriate level of constraint - PM provides guard rails, Architect has design freedom within bounds

### PRD Quality Strengths

1. ✅ **Comprehensive Technical Foundation**: 44KB technology research report provides validated tech stack, cost model, POC evidence
2. ✅ **Complete UX Specification**: 72KB front-end spec with wireframes, component library, user flows, accessibility requirements
3. ✅ **Measurable Requirements**: All NFRs have specific targets (1 min/card, 70% quality, 99% uptime, <200ms UI, WCAG AA)
4. ✅ **Clear Prioritization**: 14 epics with P0/P1/P2/P3 priorities, effort estimates, dependencies, risks
5. ✅ **GDPR Compliance**: Detailed data retention, EU processing, DPAs, encryption requirements
6. ✅ **User-Centric**: 3 personas, problem quantified (20-40 hours → <5 hours), success metrics tied to user value
7. ✅ **Risk-Aware**: HIGH risks identified (AI quality, hallucination) with documented mitigations
8. ✅ **Traceability**: FRs and NFRs mapped to epics; epics reference requirements; all tie back to user needs

### Recommendations

#### For Architect (Next Phase)
1. **Prioritize AI Quality Architecture**: Design prompt versioning system, quality monitoring dashboard, A/B testing framework for Epic 2
2. **Select Authentication Method**: Choose between email/password (simplest MVP) vs OAuth2 (better UX) vs SSO (enterprise)
3. **Design Real-Time Update Mechanism**: WebSocket (lower latency) vs HTTP polling (simpler) for batch processing status
4. **Plan POC Sprint**: Allocate 2 weeks for AI generation POC before full architecture (per tech report recommendation)
5. **Create Architecture Diagram**: System architecture, data flow, deployment architecture, CI/CD pipeline

#### For Product Owner (After Architecture)
1. **Shard PRD into Stories**: Use BMad PO sharding workflow to break epics into detailed user stories with acceptance criteria
2. **Validate Story Sequence**: Ensure first epic includes all setup/scaffolding (dev environment, CI/CD, infrastructure as code)
3. **Create Master Checklist**: Run PO master checklist to validate PRD + Architecture alignment

#### For Scrum Master (Before Development)
1. **Story Grooming**: Refine stories with development team, size stories (story points), identify technical unknowns
2. **Sprint Planning**: Recommend 2-week sprints; first sprint focuses on setup + Epic 1 (Excel upload)
3. **Risk Mitigation**: Plan AI POC as separate spike story before committing to Epic 2 timeline

#### For QA (Parallel to Architecture)
1. **Test Strategy**: Design test approach for Epic 2 (AI quality validation) - requires native Polish speaker
2. **Test Data**: Curate 10-15 representative Excel files from 60+ examples in brief.md for integration testing
3. **Quality Metrics**: Define how to measure "70% AI-generated content quality" (character count changes? manual rating?)

### Final Decision

✅ **READY FOR ARCHITECT**

The PRD is comprehensive, properly structured, and ready for architectural design. All 9 checklist categories pass with ≥90% completeness. No blocking gaps identified.

**Confidence Level**: HIGH (95%)

**Next Steps**:
1. Architect creates architecture document (see Section 7 below)
2. Product Owner runs master checklist to validate PRD + Architecture alignment
3. Product Owner shards PRD and Architecture into epic/story documents
4. Scrum Master creates first story for development

---

## 7. Next Steps & Handoff

This section defines the immediate next steps to move from product requirements to implementation.

### Immediate Actions (Week 1)

#### 1. Architect Kickoff
**Owner**: System Architect
**Deliverable**: `docs/architecture.md`
**Timeline**: 2-3 weeks

**Architect Tasks**:
- Review PRD, UX spec, and technology research report
- Create system architecture document including:
  - High-level architecture diagram (frontend, backend, AI services, data layer)
  - Technology stack confirmation (React 18+, Python 3.11+, FastAPI, AWS services)
  - Database schema design (PostgreSQL tables, S3 storage structure)
  - API design (REST endpoints, request/response formats)
  - Authentication architecture (method selection and implementation)
  - Real-time update mechanism (WebSocket vs polling)
  - Deployment architecture (AWS ECS Fargate, Vercel, CloudFront)
  - CI/CD pipeline design (GitHub Actions workflow)
  - Monitoring and observability strategy (CloudWatch metrics, alerts)
  - Security architecture (TLS 1.3, encryption, GDPR compliance)
  - Coding standards and development practices
  - Source tree structure

**Architect Prompt**:
```
Create architecture document for R&D Tax Relief Project Card Generator based on:
- PRD: docs/prd.md
- Tech Research: docs/technology-research-report.md
- UX Spec: docs/front-end-spec.md
- Figma Design: docs/figma-design-specifications.md

Focus on:
1. System architecture for AWS + React + Python FastAPI + Claude/GPT-4
2. Database schema for PostgreSQL + S3 file storage
3. AI integration architecture (Bedrock + Azure OpenAI failover)
4. Real-time batch processing (Celery + Redis)
5. GDPR-compliant data lifecycle
6. Authentication method selection and implementation
```

#### 2. Product Owner Validation
**Owner**: Product Owner
**Deliverable**: Master Checklist Report
**Timeline**: 1 week (after architecture complete)

**PO Tasks**:
- Run `/po` + master checklist to validate PRD + Architecture alignment
- Verify all requirements have architectural solutions
- Identify any gaps or inconsistencies
- Approve architecture or request refinements

#### 3. Document Sharding (PO)
**Owner**: Product Owner
**Deliverable**: `docs/epics/*.md` and `docs/stories/*.md`
**Timeline**: 1-2 weeks

**PO Tasks**:
- Use `/po` + `/shard-doc` command to shard PRD into epic documents
- Use `/po` + `/shard-doc` command to shard Architecture into story documents
- Ensure each story has:
  - Clear user story format ("As a [persona], I want [goal] so that [benefit]")
  - Detailed acceptance criteria
  - References to architecture and coding standards
  - Test requirements
  - Dependencies on other stories

**Sharding Priority**:
1. Epic 1 (Excel Upload) - Shard first for immediate development start
2. Epic 8 (Authentication) - Can develop in parallel
3. Epic 2 (AI Generation) - Shard after POC validates approach
4. Remaining P0 epics (3, 4, 5)
5. P1 epics (6, 7, 9)

### Development Preparation (Weeks 2-4)

#### 4. Story Grooming with Development Team
**Owner**: Scrum Master + Developer(s)
**Timeline**: 1 week (after sharding)

**SM Tasks**:
- Run `/sm` + create first story from Epic 1
- Groom stories with development team
- Size stories (story points or t-shirt sizes)
- Identify technical unknowns or spikes needed
- Sequence stories for first 3 sprints

#### 5. AI Generation POC Sprint (CRITICAL)
**Owner**: Developer(s)
**Deliverable**: POC validation report
**Timeline**: 2 weeks (can run parallel to architecture)

**POC Goals** (from tech report Section 10.2):
- Build minimal prompt → AI → Word pipeline
- Test with 3-5 real example projects from brief.md
- Validate token costs with actual API calls (target: €0.80-1.50/doc)
- Confirm Polish language quality with native speaker
- Measure generation time (target: 1 min average, ≤15 min max)

**POC Success Criteria**:
- ✅ Generated cards rated ≥70% usable by consultant
- ✅ Cost within €0.80-1.50 per document
- ✅ No critical hallucinations (invented facts)
- ✅ Polish grammar acceptable to native speaker
- ✅ Generation time ≤15 minutes

**POC Failure Response**:
- If quality <70%: Refine prompts, try alternative models, adjust expectations
- If cost >€2.00: Optimize prompts, reduce example count, consider GPT-4 Turbo
- If hallucination critical: Strengthen grounding instructions, add fact-checking
- If time >20 min: Switch to GPT-4 Turbo (faster), optimize prompt length

#### 6. Development Environment Setup
**Owner**: Developer(s) + DevOps (if available)
**Timeline**: 1 week

**Setup Tasks**:
- Clone repository, set up local development environment
- Install dependencies (Node.js, Python, PostgreSQL, Redis)
- Configure AWS accounts (Bedrock, S3, RDS, ECS)
- Set up GitHub Actions CI/CD pipeline
- Create development, staging, production environments
- Configure secrets management (API keys, database credentials)
- Set up monitoring (CloudWatch dashboards)

### Sprint 0 (Week 5): Foundation Sprint

**Goals**:
- Complete all setup and scaffolding
- Validate development workflow (code → test → deploy)
- Establish quality gates (linting, tests, coverage)

**Sprint 0 Stories**:
1. Set up React 18 TypeScript project with Vite and Material-UI
2. Set up Python FastAPI backend with project structure
3. Configure PostgreSQL database with initial schema
4. Set up S3 file storage with lifecycle policies
5. Implement CI/CD pipeline (GitHub Actions)
6. Create infrastructure as code (Terraform or AWS CDK)
7. Set up local development environment documentation

**Sprint 0 Acceptance**:
- ✅ Developer can run full stack locally (React + FastAPI + PostgreSQL + Redis)
- ✅ CI/CD pipeline builds, tests, and deploys to staging
- ✅ Infrastructure can be torn down and recreated via IaC
- ✅ Code coverage reporting enabled

### Sprint 1-3 (Weeks 6-11): P0 Epic 1 Implementation

**Focus**: Excel Template & Data Upload (Epic 1)

**Sprint 1**: Excel template creation and download
**Sprint 2**: File upload and client-side validation
**Sprint 3**: Server-side validation and error reporting

**Sprint Goals**:
- Consultants can download Excel template
- Consultants can upload Excel files
- System validates files and shows clear Polish error messages
- Upload flow completable in <2 minutes for valid files

### Sprint 4-9 (Weeks 12-23): P0 Remaining Epics

**Sprint 4-6**: Epic 2 (AI Generation) - 6 weeks
**Sprint 7-8**: Epic 3 (Batch Processing) - 4 weeks
**Sprint 9-11**: Epic 4 (Review & Editing) - 6 weeks
**Sprint 12-13**: Epic 5 (Word Export) - 4 weeks

**Milestone**: End-to-end workflow functional - Upload → Generate → Review → Download

### Pilot Testing Phase (Weeks 24-27)

**Goals**:
- Test with 10-15 real R&D tax consultants
- Validate 70% AI quality threshold
- Gather feedback on UX and workflow
- Identify bugs and usability issues

**Pilot Success Criteria**:
- ✅ Consultants complete batches successfully
- ✅ Average quality score ≥70
- ✅ Generation time ≤1 min average per card
- ✅ User satisfaction ≥4/5
- ✅ <5 critical bugs identified

### Sprint 14-20 (Weeks 28-40): P1 Epic Completion

**Sprint 14-15**: Epic 6 (Dashboard) + Epic 8 (Auth) - 4 weeks
**Sprint 16-17**: Epic 7 (Quality Validation) - 4 weeks
**Sprint 18-19**: Epic 9 (GDPR Compliance) - 4 weeks
**Sprint 20**: Integration testing, bug fixes, performance tuning - 2 weeks

**Milestone**: MVP complete and production-ready

### MVP Launch (Week 41+)

**Pre-Launch Checklist**:
- [ ] All P0 and P1 epics complete
- [ ] Pilot testing feedback incorporated
- [ ] GDPR compliance audit passed
- [ ] Performance testing passed (50 concurrent users)
- [ ] Security testing passed (penetration test)
- [ ] Accessibility testing passed (WCAG 2.1 AA audit ≥95%)
- [ ] Documentation complete (user guide, API docs, deployment guide)
- [ ] Support processes established
- [ ] Monitoring dashboards configured
- [ ] Cost tracking and budget alerts active

**Launch Approach**: Phased rollout
1. **Week 1**: Invite pilot users (10-15 consultants)
2. **Week 2-3**: Monitor closely, fix urgent issues
3. **Week 4+**: Open to broader market (50+ consultants)

### Post-MVP Roadmap

**Phase 2** (P2 Epics):
- Epic 10: Error Recovery & Help System
- Epic 11: Performance Optimization & Monitoring
- Epic 12: Accessibility & Internationalization

**Phase 3** (P3 Epics - Future):
- Epic 13: Mobile & Responsive Design
- Epic 14: Advanced AI Features (fine-tuning, prompt caching)

**Continuous Improvements**:
- Prompt engineering refinement based on quality metrics
- Cost optimization (target: <€1/doc with prompt caching)
- Additional language support (if expanding beyond Poland)
- API for third-party integrations

---

## Document Approval

**Product Manager**: John (BMad PM Agent)
**Date**: October 22, 2025
**Version**: 1.0 - Draft

**Status**: ✅ Ready for Architecture Phase

**Next Document**: `docs/architecture.md` (to be created by Architect)

**Related Documents**:
- `docs/brief.md` - Project brief with user research and 60+ example cards
- `docs/technology-research-report.md` - Technology stack validation and cost analysis
- `docs/front-end-spec.md` - Complete UX specification with wireframes and component library
- `docs/figma-design-specifications.md` - iNOV brand visual design system

---

**End of Product Requirements Document**
