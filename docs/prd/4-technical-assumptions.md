# 4. Technical Assumptions

This section documents the technical assumptions and constraints that inform the architecture and implementation. These assumptions are based on the technology research report (`docs/technology-research-report.md`) and represent the foundational technical decisions for the MVP.

## 4.1 Technology Stack Assumptions

### Frontend Technology
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

### Backend Technology
- **Runtime**: Python 3.11+
- **Framework**: FastAPI for REST API
- **Document Processing**: python-docx (Word generation), pandas + openpyxl (Excel parsing)
- **Task Queue**: Celery + Redis for asynchronous batch processing
- **Deployment**: Docker containers on AWS ECS Fargate or Azure Container Apps

**Assumptions**:
- python-docx library can replicate Ulga B+R template structure (validated in tech research POC)
- Celery provides sufficient reliability for batch job management
- FastAPI automatic OpenAPI documentation will serve as API contract

### Database & Storage
- **Primary Database**: PostgreSQL 15+ for metadata and user sessions
- **File Storage**: AWS S3 (EU-Central-1 region) with lifecycle policies
- **Cache**: Redis 7+ for session cache and Celery message broker

**Assumptions**:
- 90-day data retention is sufficient (per NFR17)
- S3 eventual consistency acceptable for file operations
- PostgreSQL JSONB sufficient for storing generated content and quality metadata

### AI Services
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

## 4.2 GDPR and Data Compliance Assumptions

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

## 4.3 AI Model Assumptions

### Prompt Engineering Approach
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

### Model Performance Expectations

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

## 4.4 Infrastructure and Deployment Assumptions

### Cloud Provider
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

### Scalability Targets (MVP Phase)
- **Concurrent Users**: ≤50 consultants
- **Batch Processing**: 5 parallel AI requests (per FR7)
- **Monthly Volume**: 100-500 project cards generated
- **Storage**: 10GB Excel files + 20GB Word documents (with 90-day rotation)

**Assumptions**:
- Single ECS task (2 vCPU, 4GB RAM) sufficient for MVP scale
- Single PostgreSQL instance (db.t4g.medium) handles metadata load
- No horizontal scaling required until >1,000 cards/month
- Vertical scaling (larger instances) acceptable for growth

### CI/CD and Development Workflow
- **Version Control**: Git + GitHub
- **CI/CD Pipeline**: GitHub Actions
- **Automated Testing**: pytest (backend), Jest + React Testing Library (frontend)
- **Infrastructure as Code**: Terraform or AWS CDK
- **Deployment Strategy**: Blue-green deployment for zero-downtime updates

**Assumptions**:
- GitHub Actions free tier sufficient for MVP CI/CD
- Automated tests cover ≥80% code coverage before production deployment
- Infrastructure can be torn down and recreated via IaC for disaster recovery

## 4.5 Security Assumptions

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

## 4.6 Integration and Dependency Assumptions

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

## 4.7 Quality and Testing Assumptions

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

## 4.8 Performance Assumptions

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

## 4.9 Cost Assumptions

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

## 4.10 Constraints and Limitations

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

## 4.11 Risks and Dependencies

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
