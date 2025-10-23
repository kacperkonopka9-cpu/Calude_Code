# 5. Epic List

This section organizes the product requirements into high-level epics that represent major functional areas. Each epic groups related user stories and represents a cohesive deliverable that provides value to users.

## Epic Prioritization Framework

**Priority Levels**:
- **P0 (Critical)**: Required for MVP launch, blocks core workflow
- **P1 (High)**: Essential for MVP, enhances core experience
- **P2 (Medium)**: Important but can be deferred post-MVP
- **P3 (Low)**: Nice-to-have, future enhancement

**Sequencing Strategy**: P0 epics must be completed first, P1 epics complete MVP, P2-P3 are post-MVP roadmap.

---

## Epic 1: Excel Template & Data Upload
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

## Epic 2: AI-Powered Project Card Generation
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

## Epic 3: Batch Processing & Status Tracking
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

## Epic 4: Review & Editing Interface
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

## Epic 5: Word Document Export
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

## Epic 6: Dashboard & Batch Management
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

## Epic 7: Quality Assurance & Validation
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

## Epic 8: User Authentication & Security
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

## Epic 9: GDPR Compliance & Data Management
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

## Epic 10: Error Recovery & Help System
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

## Epic 11: Performance Optimization & Monitoring
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

## Epic 12: Accessibility & Internationalization
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

## Epic 13: Mobile & Responsive Design
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

## Epic 14: Advanced AI Features (Post-MVP)
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
