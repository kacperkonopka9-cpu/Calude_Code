# 2. Requirements

## 2.1 Functional Requirements

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

## 2.2 Non-Functional Requirements

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

## 2.3 Requirements Rationale

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
