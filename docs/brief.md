# Project Brief: R&D Tax Relief Project Card Generation System

**Date:** 2025-10-22
**Version:** 1.0
**Author:** Product Manager (PM Agent)

---

## Executive Summary

This project aims to develop an automated system for generating comprehensive R&D tax relief project cards (Karty projektu B+R) in Polish for construction and engineering projects. The system will process structured input data from Excel files containing basic project information (name, dates, goals, responsible persons) and automatically generate detailed, compliant project documentation following Polish R&D tax relief (Ulga B+R) requirements.

The primary problem being solved is the labor-intensive, time-consuming process of transforming basic project data into comprehensive R&D justification documents. Currently, creating a single compliant project card requires an R&D tax consultant to:
- Analyze basic project information
- Identify and articulate R&D aspects (creativity, new knowledge, technical challenges)
- Expand brief descriptions into 3-4 paragraph technical narratives (200-400 words)
- Document research problems and solutions
- Ensure compliance with Ulga B+R criteria
- Format according to template standards

The target users are R&D tax consultants serving construction and engineering companies seeking R&D tax relief. The key value proposition is intelligent automation that transforms minimal input data into high-quality, tax-authority-ready project cards, reducing document creation time from hours to minutes while maintaining professional quality, compliance, and the specialized expertise expected from an R&D tax consultant.

---

## Problem Statement

### Current State and Pain Points

R&D tax consultants currently face a repetitive, time-intensive manual process when preparing project cards for construction and engineering companies claiming Ulga B+R (Polish R&D tax relief). The workflow involves:

1. **Data Collection Burden**: Gathering basic project information from clients (often provided as simple Excel tables with minimal details)
2. **Manual Analysis**: Reviewing each project to identify qualifying R&D aspects (celowość, element twórczy, nowa wiedza)
3. **Document Expansion**: Transforming sparse project descriptions into comprehensive technical narratives that meet regulatory standards
4. **Compliance Documentation**: Ensuring each card properly addresses all Ulga B+R criteria with clear, non-specialist language
5. **Formatting & Quality Control**: Following template structure, maintaining consistency across multiple project cards

For a typical consulting engagement with 10-20 projects, this process can consume 20-40 hours of consultant time, with each project card requiring 1-3 hours of focused work. The repetitive nature of the task (following the same template structure, addressing the same compliance criteria) makes it an ideal automation candidate, yet the requirement for technical expertise and regulatory compliance makes simple templates insufficient.

### Impact of the Problem

- **Time Cost**: Consultants spend valuable hours on document production rather than higher-value analysis and client advisory
- **Scalability Limitations**: Manual process limits the number of clients a consultant can serve effectively
- **Consistency Risk**: Quality and detail level may vary across documents when produced manually under time pressure
- **Error Potential**: Manual data entry and formatting increases risk of omissions or inconsistencies
- **Client Service Delays**: Longer turnaround times for delivering completed documentation

### Why Existing Solutions Fall Short

- **Simple Templates**: Standard Word templates don't address the core challenge of expanding minimal input into detailed R&D justifications
- **Generic Document Automation**: Tools like mail merge can't interpret project data or generate contextual R&D narratives
- **Manual AI Prompting**: Using ChatGPT/Claude manually for each project is still time-consuming and requires crafting individual prompts
- **Translation Tools**: Can't create R&D-specific content, only translate existing text

### Urgency and Importance

With Polish companies increasingly utilizing Ulga B+R, the demand for high-quality project documentation is growing. Tax authorities are also increasing scrutiny of R&D claims, making comprehensive, well-justified documentation more critical than ever. Consultants need a solution that maintains their expertise and quality standards while dramatically reducing production time.

---

## Proposed Solution

### Core Concept and Approach

The system will be an AI-powered document generation tool that acts as an intelligent R&D tax consultant assistant. It takes structured input data (Excel tables with basic project information) and automatically generates complete, professionally-written project cards in Polish that comply with Ulga B+R requirements.

The solution leverages large language models (LLMs) with:
- **Deep understanding** of Polish R&D tax relief regulations and criteria
- **Domain expertise** in construction/engineering R&D aspects
- **Template mastery** to follow the exact structure from the provided Word template
- **Professional writing** capabilities to produce consultant-quality Polish technical documentation

### Key Differentiators from Existing Solutions

1. **Intelligent Content Generation** (not just templates): The system doesn't simply fill in blanks—it analyzes project data, identifies R&D aspects, and generates contextual technical narratives that justify tax relief eligibility

2. **Regulatory Compliance Built-In**: The system is trained on actual approved project cards and Ulga B+R guidelines, ensuring outputs meet tax authority expectations

3. **Minimal Input, Maximum Output**: Transforms sparse Excel data (5-10 fields per project) into comprehensive 4-6 page Word documents with detailed sections

4. **Batch Processing**: Handles multiple projects simultaneously, generating 10-20 project cards in minutes rather than days

5. **Consultant-Quality Polish**: Produces professional technical Polish that is clear for non-specialists while maintaining appropriate technical terminology

### Why This Solution Will Succeed

- **AI Maturity**: Modern LLMs (GPT-4, Claude) excel at structured document generation with examples
- **Clear Template**: Well-defined input/output structure (template + instructions + examples)
- **Repeatable Pattern**: R&D project cards follow consistent structure and criteria
- **Quality Examples**: 60+ completed project cards provide excellent training references
- **Focused Scope**: Single document type for specific regulatory purpose (not trying to automate all consulting work)

### High-Level Vision

The consultant uploads an Excel file with project data, the system processes each project through an AI pipeline that:
1. Analyzes project description for R&D elements
2. Generates detailed sections following the template structure
3. Ensures compliance with Ulga B+R criteria (celowość, twórczość, nowa wiedza)
4. Formats output as Word documents matching the provided template
5. Delivers a complete set of project cards ready for consultant review and client delivery

The consultant's role shifts from document production to quality review, refinement, and strategic advisory—significantly higher value work.

### Solution with Risk Mitigation Built-In

The solution includes a **two-stage quality assurance approach**:

**Stage 1 - AI Generation** (Automated):
- Validate input data completeness
- Generate draft project cards with grounding in source data
- Flag low-confidence sections
- Apply compliance checklist

**Stage 2 - Consultant Review** (Human):
- Review flagged sections
- Verify factual accuracy against input data
- Refine technical language
- Approve for client delivery

This hybrid approach maintains time savings (hours → minutes for drafting) while ensuring quality and compliance through mandatory human oversight. The system is positioned as a **"consultant assistant"** not a **"fully autonomous generator"**.

---

## Target Users

### Primary User Segment: R&D Tax Consultants

**Demographic/Firmographic Profile:**
- Professional tax consultants or consulting firms specializing in R&D tax relief (Ulga B+R)
- Serving primarily construction, engineering, and industrial manufacturing sectors
- Operating in Poland, fluent in Polish technical and regulatory language
- Firm size: Solo practitioners to small/medium consulting firms (1-20 consultants)
- Client portfolio: 5-50+ companies claiming R&D tax relief annually

**Current Behaviors and Workflows:**
- Conduct client meetings to understand R&D activities and gather project information
- Receive project data in various formats (Excel, emails, verbal descriptions, internal company documents)
- Manually create project cards using Word templates or previous examples as reference
- Spend 1-3 hours per project card writing, formatting, and ensuring compliance
- Review and revise documents based on internal QA or client feedback
- Submit finalized documentation to clients for tax filing purposes
- May handle 10-20 projects per client, multiple clients simultaneously during tax season

**Specific Needs and Pain Points:**
- **Time pressure**: Tax filing deadlines create intense workload spikes
- **Quality consistency**: Need to maintain high standards across many documents under pressure
- **Client communication**: Time spent on documentation reduces time for client advisory and business development
- **Scalability**: Manual process limits revenue growth potential
- **Repetitive work**: Same template structure and compliance criteria for every project creates tedious, unfulfilling work
- **Error anxiety**: Manual data entry and formatting increases risk of mistakes in critical tax documents

**Goals They're Trying to Achieve:**
- Deliver high-quality, compliant R&D project documentation efficiently
- Scale consulting practice without proportionally increasing labor hours
- Spend more time on high-value activities (client strategy, tax optimization, business development)
- Maintain competitive advantage through faster turnaround times
- Reduce stress during peak tax season periods
- Build reputation for thorough, professional documentation

### Secondary User Segment: In-House Tax/Finance Teams

**Demographic/Firmographic Profile:**
- Tax managers, finance directors, or dedicated R&D tax specialists within construction/engineering companies
- Companies with 5+ qualifying R&D projects annually who handle Ulga B+R claims internally
- Mid to large companies (50-500+ employees) with structured tax planning functions
- Industries: General contracting, specialized construction, engineering services, industrial facilities

**Current Behaviors and Workflows:**
- Collect project information from internal teams (project managers, engineers, technical directors)
- Attempt to create project cards themselves or hire external consultants
- Struggle with technical writing and R&D justification (core competency is tax/finance, not technical documentation)
- May outsource to consultants due to lack of internal expertise/capacity

**Specific Needs and Pain Points:**
- **Knowledge gap**: Understand tax regulations but struggle with technical R&D narrative writing
- **Internal coordination**: Difficulty extracting needed information from busy technical teams
- **Cost control**: External consultant fees for documentation can be significant
- **Control and timing**: Want ability to produce documentation on their own schedule

**Goals They're Trying to Achieve:**
- Bring R&D documentation production in-house to reduce costs
- Maintain control over documentation quality and timing
- Free up budget currently spent on external consultants for documentation
- Build internal capability for R&D tax compliance

### Primary Focus for MVP: R&D Tax Consultants

While both segments could benefit, the **primary target for MVP is R&D tax consultants** because:
1. They have the domain expertise to effectively review and refine AI-generated content
2. They process higher volumes (multiple clients, many projects each)
3. They have existing workflows to integrate the tool into
4. They understand the quality/compliance requirements deeply
5. ROI is clear and measurable (hours saved × hourly rate × number of projects)

Secondary segment (in-house teams) could be addressed in future versions with additional guidance features and quality assurance tools.

---

## Goals & Success Metrics

### Business Objectives

- **Reduce documentation production time by 70-80%**: From 1-3 hours per project card to 15-30 minutes (including AI generation + consultant review)
  - *Target*: Average project card production time ≤ 30 minutes by end of MVP phase

- **Enable consultant scalability**: Allow consultants to handle 2-3x more projects per tax season without increasing labor hours
  - *Target*: Consultants process 30+ project cards per week (vs. current 10-15)

- **Maintain quality and compliance**: Zero increase in tax authority rejection rates for AI-assisted documentation
  - *Target*: ≥95% of generated project cards approved with minimal edits

- **Achieve consultant adoption**: Successful integration into daily workflow for early adopter consultants
  - *Target*: 3-5 active consultant users within 3 months of MVP launch

- **Demonstrate clear ROI**: Quantifiable time/cost savings that justify adoption
  - *Target*: 20+ hours saved per consultant per month during active periods

### User Success Metrics

- **Time savings realized**: Consultants report significant reduction in documentation hours
  - *Measurement*: Pre/post surveys, time tracking data

- **Quality satisfaction**: Consultants rate AI-generated drafts as "good starting point" or better
  - *Measurement*: Quality rating survey (1-5 scale) after each batch, target ≥4.0/5.0

- **Edit ratio**: Minimal consultant editing required to finalize documents
  - *Measurement*: Track percentage of AI-generated content retained in final documents, target ≥70%

- **Workflow integration**: Tool becomes standard part of consultant workflow
  - *Measurement*: Weekly active usage, repeat usage rate ≥80%

- **Client satisfaction**: End clients (construction companies) satisfied with documentation quality
  - *Measurement*: Indirect feedback via consultant reports, zero quality complaints

### Key Performance Indicators (KPIs)

- **Generation Success Rate**: Percentage of projects successfully processed without errors
  - *Definition*: (Projects with complete outputs / Total projects attempted) × 100
  - *Target*: ≥95% success rate

- **Average Generation Time**: Time from input upload to output delivery
  - *Definition*: Mean processing time per project card
  - *Target*: ≤5 minutes per project card

- **Consultant Review Time**: Time spent by consultant reviewing/editing AI output
  - *Definition*: Mean time from generation to consultant approval
  - *Target*: ≤25 minutes per project card (vs. 60-180 minutes for manual creation)

- **Compliance Pass Rate**: Percentage of AI-generated cards meeting Ulga B+R criteria without major revisions
  - *Definition*: Cards rated "compliant" or "minor edits needed" by consultant
  - *Target*: ≥90%

- **Content Quality Score**: Assessment of technical writing quality, Polish language correctness, and completeness
  - *Definition*: Composite score based on: section completeness (40%), language quality (30%), technical accuracy (30%)
  - *Target*: ≥80/100 average score

- **User Retention Rate**: Percentage of consultants who continue using tool after initial trial
  - *Definition*: (Active users month 3 / Trial users month 1) × 100
  - *Target*: ≥70%

- **Batch Processing Efficiency**: Number of project cards generated per batch session
  - *Definition*: Mean number of projects processed when consultant uploads input file
  - *Target*: ≥10 projects per batch

- **Cost per Document**: Total system cost (AI API calls, infrastructure) per generated project card
  - *Definition*: Monthly operational costs / Number of project cards generated
  - *Target*: ≤10 PLN per project card (vs. consultant hourly rate of 200-500 PLN)

---

## MVP Scope

### Core Features (Must Have)

1. **Excel Input Processing**
   - Accept standardized Excel file with project data (based on Input.docx structure)
   - Required columns: Nazwa projektu, Opis, Data rozpoczęcia, Data zakończenia, Cel projektu, Osoba odpowiedzialna
   - Validate input data for completeness and format
   - Support multiple projects in single file (batch processing)
   - *Rationale*: Core input mechanism matching consultant's existing workflow

2. **AI-Powered Project Card Generation**
   - Generate complete project cards in Polish following template structure
   - All required sections: Tytuł projektu, Cel/Opis, Podstawowe etapy, Problemy badawcze, Prace twórcze, Poziom innowacyjności, Roczne podsumowanie
   - Ensure compliance with Ulga B+R criteria (celowość, element twórczy, nowa wiedza)
   - Use example project cards as style/quality reference
   - Expand sparse input data into detailed technical narratives (200-400 words per major section)
   - *Rationale*: Core value proposition - intelligent content generation

3. **Word Document Output**
   - Generate formatted .docx files matching "Szablon karty projektu" template
   - Proper table formatting for project stages
   - Professional Polish typography and layout
   - One document per project with standardized naming
   - *Rationale*: Deliverable format expected by tax authorities and clients

4. **Batch Processing Capability**
   - Process 10-20 projects in single operation
   - Progress tracking during generation
   - Summary report of successful/failed generations
   - *Rationale*: Efficiency for consultants handling multiple projects

5. **Quality Assurance Flags**
   - Identify sections with insufficient input data
   - Flag low-confidence AI outputs for consultant review
   - Basic compliance checklist validation (all required sections present)
   - *Rationale*: Risk mitigation - ensure consultant reviews critical areas

### Out of Scope for MVP

- **Multi-language support**: Polish only for MVP (not English, German, etc.)
- **Custom template editing**: Use fixed template structure, no user customization
- **Integration with accounting/ERP systems**: Manual Excel upload only
- **Real-time collaboration**: Single-user workflow, no multi-user editing
- **Version control/history**: Generate fresh documents, no change tracking
- **Client portal**: Consultant-facing only, not client-accessible
- **Advanced AI features**: No project type classification, sentiment analysis, or recommendations engine
- **Mobile app**: Desktop/web only
- **Automated submission to tax authorities**: Document generation only, not filing
- **Financial calculations**: No cost tracking or tax benefit estimation

### MVP Success Criteria

**The MVP is successful if:**

1. **Functional completeness**: System successfully generates compliant project cards for ≥90% of input projects across diverse domains (construction, IT, manufacturing, logistics)

2. **Time savings delivered**: Consultants reduce per-project time from 1-3 hours to ≤30 minutes (70-80% reduction)

3. **Quality threshold met**: Generated content requires ≤30% editing to reach final state (70%+ AI content retained)

4. **User adoption**: 3-5 consultants actively use system for real client work within 3 months

5. **Compliance validation**: Zero tax authority rejections attributed to AI-generated content quality

6. **ROI demonstration**: Clear cost savings vs. manual process (time saved × consultant hourly rate > system costs)

---

## Post-MVP Vision

### Phase 2 Features

**Enhanced Input & Data Management:**
- **Intelligent data extraction**: Parse unstructured input formats (Word documents, PDFs, emails) to extract project information
- **Multi-year project support**: Automatically split projects spanning multiple tax years into separate annual cards
- **Input data enrichment prompts**: System suggests questions to ask clients based on detected data gaps
- **Project database**: Store and retrieve historical project data for reference and reuse

**Advanced AI Capabilities:**
- **Project type classification**: Automatically detect project category (construction, IT, manufacturing, etc.) and apply specialized generation logic
- **Technical terminology extraction**: Identify and correctly use industry-specific Polish terms
- **Consistency checking**: Ensure alignment between project goals, stages, problems, and outcomes
- **Cross-project insights**: Identify similar past projects to inform current generation

**Workflow & Collaboration:**
- **Multi-user access**: Team collaboration features for consulting firms
- **Review workflow**: Assign projects for review, track approval status
- **Comment and annotation**: Markup AI-generated content with feedback
- **Template customization**: Allow consultants to create firm-specific template variations

**Quality & Compliance:**
- **Advanced compliance validation**: Deep analysis against Ulga B+R criteria with specific recommendations
- **Citation and reference management**: Track supporting documentation and link to specific claims
- **Audit trail**: Complete history of changes and AI generation decisions
- **Quality scoring**: Detailed assessment of generated content against best practices

### Long-Term Vision (1-2 Years)

**Comprehensive R&D Tax Platform:**
Transform from single-purpose document generator into full-service R&D tax relief management system:

- **End-to-end workflow automation**: From project identification → documentation → cost tracking → tax filing
- **Client self-service portal**: Companies input project data directly, consultants review and approve
- **Integration ecosystem**: Connect with ERP systems, project management tools, accounting software
- **Regulatory intelligence**: Automatic updates when Ulga B+R regulations change
- **Analytics dashboard**: Track portfolio-wide metrics, identify optimization opportunities
- **Multi-country support**: Expand beyond Poland to other European R&D tax relief programs

**AI Consultant Assistant:**
- **Natural language interface**: Consultants interact conversationally ("Generate cards for all 2024 construction projects")
- **Proactive recommendations**: System suggests which projects qualify, potential risks, optimization strategies
- **Learning from feedback**: Continuously improve based on consultant edits and preferences
- **Expert knowledge base**: Answer regulatory questions, provide best practice guidance

### Expansion Opportunities

**Market Expansion:**
- **Adjacent tax services**: Extend to other specialized tax documentation (IP Box, innovation relief programs)
- **Geographic expansion**: Adapt for R&D tax programs in Germany, UK, France, EU-wide
- **Industry verticals**: Specialized versions for pharmaceuticals, software development, biotech

**Business Model Evolution:**
- **SaaS platform**: Subscription model for consulting firms
- **White-label solution**: License to larger accounting/tax firms under their brand
- **Marketplace**: Connect consultants with companies seeking R&D tax services
- **Training & certification**: Educational programs for consultants learning R&D tax relief

**Technology Expansion:**
- **Voice input**: Consultants dictate project information, AI transcribes and structures
- **Computer vision**: Extract data from photos of technical drawings, prototypes, lab notes
- **Predictive analytics**: Estimate tax benefit amounts, forecast approval likelihood
- **Automated research**: AI finds supporting evidence for R&D claims from public sources

---

## Technical Considerations

### Platform Requirements

**Target Platforms:**
- **Primary**: Web application (browser-based, cross-platform)
- **Accessibility**: Desktop browsers (Chrome, Firefox, Edge, Safari - latest 2 versions)
- **Operating Systems**: Windows 10/11, macOS 12+, Linux (Ubuntu/Debian)
- **Mobile**: Responsive design for tablet viewing (iPad, Android tablets) - review/download only, not primary generation interface

**Performance Requirements:**
- **Generation speed**: ≤5 minutes per project card
- **Batch processing**: Handle 20 projects concurrently without timeout
- **File upload**: Support Excel files up to 10MB
- **Document download**: Generated Word files available within 30 seconds of completion
- **System availability**: 99% uptime during business hours (8 AM - 8 PM CET, Monday-Friday)

### Technology Preferences

**Frontend:**
- **Framework**: React or Next.js for modern, responsive UI
- **State management**: Redux or Context API for handling multi-project workflows
- **File handling**: Client-side Excel parsing (SheetJS/xlsx) and preview
- **UI components**: Material-UI or Ant Design for professional, polished interface
- *Rationale*: Modern stack with strong Polish language support, excellent Excel/document handling libraries

**Backend:**
- **Runtime**: Python 3.11+ (excellent for AI integration, document processing, data manipulation)
- **Framework**: FastAPI or Flask for RESTful API
- **Document generation**: python-docx for Word document creation with precise template control
- **Excel processing**: pandas + openpyxl for robust data extraction and validation
- *Rationale*: Python ecosystem best-in-class for AI/ML, document processing, and has mature libraries for Polish language handling

**Database:**
- **Primary**: PostgreSQL for structured data (user accounts, project metadata, generation logs)
- **File storage**: AWS S3 or Azure Blob Storage for Excel inputs and Word outputs
- **Caching**: Redis for session management and API response caching
- *Rationale*: Reliable, scalable, well-supported stack with GDPR compliance capabilities

**Hosting/Infrastructure:**
- **Cloud platform**: AWS or Azure (preference: Azure for European data residency)
- **Region**: EU-Central (Frankfurt or Amsterdam) for GDPR compliance and low latency to Poland
- **Compute**: Containerized deployment (Docker) on managed services (ECS, AKS, or App Service)
- **CDN**: CloudFront or Azure CDN for static assets
- **Monitoring**: Application Insights or New Relic for performance tracking
- *Rationale*: European hosting critical for data privacy, managed services reduce operational overhead

**AI/LLM Integration:**
- **Primary model**: OpenAI GPT-4 or Anthropic Claude 3.5 Sonnet via API
- **Fallback**: Azure OpenAI Service for enterprise SLA and data residency guarantees
- **Prompt management**: LangChain or custom framework for prompt versioning and optimization
- **Token optimization**: Intelligent chunking to minimize API costs while maintaining quality
- *Rationale*: Leading models with strong Polish language capabilities, proven document generation quality

### Architecture Considerations

**Repository Structure:**
- **Monorepo** containing frontend, backend, and shared utilities
- *Rationale*: Single deployment pipeline, easier code sharing, better for small team

**Service Architecture:**
- **Modular monolith** for MVP with clear service boundaries
- Components: Web UI → API Gateway → Document Generation Service → AI Service → Storage
- *Rationale*: Simpler than microservices for MVP, can decompose later if needed

**Integration Requirements:**
- **Excel import**: Support .xlsx and .xlsm formats (Input.docx structure)
- **Word template**: Parse and populate existing .docx template programmatically
- **AI API**: RESTful integration with OpenAI/Anthropic with retry logic and error handling
- **File management**: Secure upload/download with virus scanning
- **Email notifications**: Optional completion notifications via SendGrid/AWS SES

**Security/Compliance:**
- **Data encryption**: TLS 1.3 for transit, AES-256 for data at rest
- **Authentication**: OAuth 2.0 / JWT for user sessions
- **Authorization**: Role-based access control (consultant, admin roles)
- **GDPR compliance**: EU data residency, data retention policies, right to deletion
- **API security**: Rate limiting, API key management for AI services with data privacy settings
- **Audit logging**: Track all document generations, user actions, data access
- *Rationale*: Handling sensitive business data requires enterprise-grade security

### Testing Requirements

**Testing Strategy:**
- **Unit testing**: 80%+ code coverage for core logic (Python: pytest, JavaScript: Jest)
- **Integration testing**: API endpoints, database operations, file processing pipelines
- **End-to-end testing**: Full workflow from Excel upload to Word download (Playwright/Cypress)
- **AI output validation**: Automated checks for section completeness, language quality, compliance keywords
- **Manual QA**: Consultant review of sample outputs across all 60+ example project types
- *Rationale*: High quality/compliance requirements demand comprehensive testing

**Quality Assurance:**
- **Polish language validation**: Native speaker review of AI outputs
- **Template compliance**: Automated verification that outputs match template structure
- **Regression testing**: Ensure prompt changes don't degrade quality on existing examples
- **Performance testing**: Load testing for batch processing scenarios
- **Security testing**: Penetration testing, vulnerability scanning

---

## Constraints & Assumptions

### Constraints

**Budget:**
- **Development budget**: Assume bootstrapped/self-funded or small seed investment (€20,000-50,000 for MVP)
- **Operational costs**: AI API costs estimated at €0.50-2.00 per project card (depending on model choice and token usage)
- **Infrastructure**: Cloud hosting €100-500/month for MVP scale (100-500 documents/month)
- **Cost sensitivity**: Must demonstrate clear ROI vs. consultant hourly rates (200-500 PLN/hour)
- *Implication*: Cost-effective tech stack, optimize AI token usage, managed services over custom infrastructure

**Timeline:**
- **MVP delivery**: 3-4 months from project start to first usable version
- **Pilot testing**: 2-3 months with early adopter consultants
- **Market readiness**: 6-8 months total to production-ready system
- **Tax season urgency**: Must be ready before peak tax filing season (Q1 of following year)
- *Implication*: Focused scope, avoid scope creep, use proven technologies vs. experimental approaches

**Resources:**
- **Development team**: Small team (1-3 developers) for MVP
- **Domain expertise**: Access to R&D tax consultant for requirements validation and testing
- **Language expertise**: Native Polish speakers for content quality validation
- **Example data**: 60+ real project cards available as training/testing data
- *Implication*: Leverage no-code/low-code where appropriate, extensive use of AI for development acceleration, clear documentation

**Technical:**
- **AI model availability**: Dependent on external API providers (OpenAI, Anthropic)
- **Token limits**: API rate limits and context window constraints
- **Polish language quality**: LLM performance varies for Polish vs. English
- **Document format compatibility**: Must work with Microsoft Word 2016+ and LibreOffice
- **Internet dependency**: Requires stable internet for AI API calls (no offline mode for MVP)
- *Implication*: Error handling for API failures, fallback strategies, thorough Polish language testing

**Regulatory:**
- **GDPR compliance**: Must handle client data according to EU regulations
- **Data residency**: Prefer EU-based infrastructure and AI services with EU data processing
- **Tax law changes**: Ulga B+R regulations may change, requiring prompt updates
- **No guarantees**: Cannot legally guarantee tax authority acceptance of generated documents
- *Implication*: Clear disclaimers, consultant review mandatory, update mechanisms for regulatory changes

### Key Assumptions

**Market & Users:**
- R&D tax consultants are willing to adopt AI-assisted tools and trust AI-generated content with human oversight
- Consultants have basic technical skills to upload Excel files and download Word documents
- Current manual process is sufficiently painful to justify new tool adoption
- Consultants value time savings over complete control of every word
- Market size in Poland is sufficient to support specialized tool (estimated 100-500 active R&D tax consultants)

**Technical:**
- Modern LLMs (GPT-4, Claude 3.5) have sufficient Polish language capability for professional documentation
- Example project cards (60+) provide representative sample of real-world diversity
- Template structure is stable and unlikely to require major changes
- Excel input format can be standardized across consultant practices
- Python-docx can accurately replicate Word template formatting

**AI Performance:**
- AI can reliably expand sparse input data (50-200 words) into detailed narratives (200-400 words) while maintaining accuracy
- AI can identify R&D aspects from general project descriptions without inventing facts
- Generated Polish will be grammatically correct and professionally appropriate 90%+ of the time
- AI-generated content will pass consultant quality review with ≤30% editing required
- Prompt engineering and few-shot examples will produce consistent, high-quality outputs

**Business:**
- Consultants will pay for tool if it saves them 10+ hours per month (subscription or per-document pricing)
- Word-of-mouth referrals from early adopters will drive additional user acquisition
- Regulatory environment for Ulga B+R will remain stable or expand (not contract)
- Competition is limited - no dominant existing solution for this specific problem
- System can be operated profitably at €5-15 per document price point

**Operational:**
- Single developer or small team can build and maintain MVP
- Customer support burden will be manageable (primarily technical support, not tax consulting)
- System reliability of 95-99% is acceptable for MVP (not mission-critical uptime requirements)
- Updates and improvements can be deployed monthly without disrupting users
- AI API costs will remain within predictable ranges (no massive price increases)

### Critical Dependencies

1. **LLM API availability and pricing**: Core functionality depends on third-party AI services
2. **Example quality**: Training quality depends on the 60+ examples being representative and high-quality
3. **Consultant partnership**: Need at least 1-2 consultants for requirements validation and pilot testing
4. **Template stability**: Major changes to official Ulga B+R template would require significant rework
5. **Regulatory continuity**: Major changes to R&D tax relief program could invalidate approach

---

## Risks & Open Questions

### Key Risks

**1. AI Quality & Consistency Risk**
- **Description**: Generated Polish content quality may be inconsistent across different project types or LLM API updates may degrade performance
- **Impact**: HIGH - Poor quality outputs undermine core value proposition
- **Mitigation**:
  - Extensive testing with all 60+ examples before launch
  - Version pinning of LLM models to prevent unexpected changes
  - A/B testing when switching models or prompts
  - Automated quality scoring system to detect degradation
  - Fallback to previous prompt versions if quality drops

**2. Regulatory Change Risk**
- **Description**: Polish tax authorities change Ulga B+R requirements, template structure, or acceptance criteria
- **Impact**: MEDIUM-HIGH - Could require significant system updates or invalidate approach
- **Mitigation**:
  - Monitor regulatory changes through consultant network
  - Design system with configurable templates and prompts
  - Maintain relationship with tax law experts for early warnings
  - Build update mechanism into architecture
  - Document all regulatory assumptions for quick revision

**3. Consultant Adoption Risk**
- **Description**: Consultants may resist AI-generated content due to trust, liability concerns, or workflow disruption
- **Impact**: HIGH - No users = no business
- **Mitigation**:
  - Position as "assistant" not "replacement"
  - Mandatory human review workflow built into system
  - Early pilot with friendly consultants for testimonials
  - Transparent about AI usage, emphasize consultant remains responsible
  - Demonstrate ROI clearly with time tracking during pilot

**4. Data Privacy & Security Risk**
- **Description**: Client project data exposed through API breach, storage vulnerability, or AI provider data handling
- **Impact**: CRITICAL - Legal liability, business destruction, GDPR violations
- **Mitigation**:
  - EU-based infrastructure and AI services where possible
  - Data processing agreements with all third-party providers
  - Encryption at rest and in transit
  - Minimize data retention (auto-delete after 90 days)
  - Security audit before production launch
  - Clear privacy policy and user consent mechanisms

**5. AI Cost Escalation Risk**
- **Description**: LLM API costs increase or token usage higher than projected, making economics unviable
- **Impact**: MEDIUM - Could eliminate profitability or require price increases
- **Mitigation**:
  - Optimize prompts for token efficiency
  - Cache common patterns and reusable content
  - Monitor costs per document closely
  - Build pricing model with margin for cost increases
  - Evaluate multiple AI providers for competitive pricing
  - Consider local LLM deployment for future cost control

**6. Example Data Bias Risk**
- **Description**: 60+ examples may not represent full diversity of R&D projects, leading to poor performance on edge cases
- **Impact**: MEDIUM - Some project types poorly served
- **Mitigation**:
  - Categorize examples by industry/type to identify gaps
  - Continuously collect new examples from pilot users
  - Build project type detection to warn when handling unfamiliar types
  - Allow consultants to submit examples to improve system
  - Track failure patterns to identify weak areas

**7. Technical Dependency Risk**
- **Description**: OpenAI/Anthropic API outages, rate limiting, or service discontinuation
- **Impact**: MEDIUM-HIGH - Service interruption or complete system failure
- **Mitigation**:
  - Multi-provider strategy (OpenAI + Anthropic + Azure OpenAI)
  - Automatic failover between providers
  - Queue system for handling rate limits gracefully
  - Service level monitoring and alerts
  - Clear communication to users during outages

### Open Questions

**Product & Market:**
1. **What is the optimal pricing model?**
   - Per-document (€5-15)? Monthly subscription (€50-200)? Annual license (€500-2000)?
   - Should pricing vary by project complexity or volume?

2. **What is the actual addressable market size?**
   - How many R&D tax consultants actively serve construction/engineering clients in Poland?
   - What percentage would adopt AI-assisted tools?

3. **What is acceptable quality threshold?**
   - What percentage of AI-generated content must be retained for consultants to perceive value?
   - How much editing time is acceptable before tool feels burdensome?

4. **Should we support multiple template versions?**
   - Are there regional variations or consultant-specific template preferences?
   - How much template customization should be allowed?

5. **What is the customer acquisition strategy?**
   - Direct sales to consultants? Partnership with consulting firms? Marketplace listing?
   - What marketing channels reach R&D tax consultants effectively?

**Technical:**
6. **Which LLM performs best for Polish technical documentation?**
   - GPT-4, Claude 3.5 Sonnet, or other models?
   - Does fine-tuning improve results sufficiently to justify cost/complexity?

7. **What is the optimal prompt architecture?**
   - Single comprehensive prompt vs. multi-step chain?
   - Section-by-section generation vs. full document generation?
   - How many example cards should be included in prompts?

8. **How should we handle multi-year projects?**
   - Automatically split or require manual intervention?
   - How to track continuation across tax years?

9. **What level of input data validation is needed?**
   - Strict enforcement (reject incomplete data) or flexible (work with what's available)?
   - Should system prompt user for missing information interactively?

10. **Should we build custom LLM vs. use APIs?**
    - Would fine-tuned or locally-hosted model provide better cost/quality/privacy?
    - Is development effort justified for MVP?

**Business & Legal:**
11. **What liability protections are needed?**
    - Disclaimers sufficient or require formal legal review of terms?
    - Should consultants sign agreements acknowledging AI assistance?

12. **How to handle intellectual property?**
    - Who owns generated content - system, consultant, or end client?
    - Can generated content be used to improve system (as training data)?

13. **What customer support model is sustainable?**
    - Email only? Live chat? Phone support?
    - Who handles tax regulation questions vs. technical issues?

14. **Should we pursue certifications or endorsements?**
    - Polish tax authority awareness or approval?
    - Professional association endorsements?
    - ISO/security certifications?

### Areas Needing Further Research

**Market Research:**
- **Competitive landscape analysis**: Thorough investigation of existing solutions (even partial/adjacent)
- **Consultant interviews**: 10-15 detailed interviews to validate pain points, willingness to pay, workflow requirements
- **End client perspective**: How do construction companies perceive AI-generated tax documentation?

**Technical Feasibility:**
- **Polish language benchmarking**: Systematic comparison of GPT-4 vs. Claude vs. other models for Polish technical writing
- **Token cost modeling**: Actual cost per document with real examples across all 60+ project types
- **Template compatibility testing**: Verify python-docx can replicate exact formatting of provided template

**Regulatory & Legal:**
- **Tax authority position**: Official or unofficial guidance on AI-assisted documentation
- **Data protection requirements**: Specific GDPR obligations for handling tax-related business data
- **Professional liability**: Insurance and legal protection needs for consultants using AI tools

**Business Model:**
- **Pricing sensitivity research**: What would consultants actually pay? Price elasticity testing
- **Market size validation**: Actual number of potential users in Poland and expansion markets
- **Partnership opportunities**: Could this be white-labeled for larger accounting firms?

---

## Next Steps

### Immediate Actions

1. **Validate Project Brief with stakeholder** - Review and approve this brief before proceeding to PRD
   - Confirm problem statement, solution approach, and scope alignment
   - Validate assumptions and constraints
   - Approve MVP feature set

2. **Conduct consultant interviews (3-5 consultants)** - Validate pain points, workflow, and willingness to adopt
   - Confirm time estimates for manual process
   - Test pricing sensitivity (€5-15 per document or subscription model)
   - Identify must-have vs. nice-to-have features
   - Recruit 1-2 pilot testers

3. **Technical feasibility spike (1 week)** - Prove core technical approach
   - Test GPT-4 vs. Claude 3.5 with 5 sample projects from examples
   - Validate python-docx can replicate template formatting
   - Estimate actual token costs per document
   - Confirm Polish language quality meets professional standards

4. **Analyze all 60+ example project cards** - Categorize and understand full diversity
   - Group by industry/domain (construction, IT, manufacturing, etc.)
   - Identify common patterns and edge cases
   - Extract quality criteria and compliance patterns
   - Build example taxonomy for prompt engineering

5. **Legal & compliance preliminary review** - Understand regulatory constraints
   - Consult with GDPR expert on data handling requirements
   - Research Polish tax authority position on AI-assisted documentation
   - Draft initial terms of service and privacy policy
   - Identify required disclaimers

6. **Develop Product Requirements Document (PRD)** - Detail functional and technical specifications
   - Using this Project Brief as foundation
   - Work with PM agent to create comprehensive PRD

---

## Appendices

### A. Project Assets

**Documentation Location:** `/workspaces/Calude_Code/docs/project-cards/`

**Key Files:**
- **Template**: `input/2025_09_10_Szablon karty projektu - do uzupełnienia.docx`
- **Instructions**: `input/Instrukcja do karty projektu.pdf`
- **Input Example**: `input/Input.docx`
- **Example Cards** (60+): `examples/` directory
- **Analysis Notes**: `analysis-notes.md`

**Example Project Types:**
- Construction projects (heritage restoration, specialized techniques)
- Industrial power/energy systems (turbines, steam systems, fuel systems)
- IT systems (ERP, logistics, task management, cybersecurity)
- Manufacturing processes (window/door production, welding, cutting)
- Specialized equipment (forklifts, conveyors, storage systems)

### B. References

- **Polish R&D Tax Relief (Ulga B+R)**: Official government program documentation
- **Template Instructions**: Detailed guidance in `Instrukcja do karty projektu.pdf`
- **Core Criteria**: Celowość (purposefulness), Element twórczy (creative element), Nowa wiedza (new knowledge)

---

**End of Project Brief**

This brief is ready to serve as the foundation for creating a comprehensive Product Requirements Document (PRD).
