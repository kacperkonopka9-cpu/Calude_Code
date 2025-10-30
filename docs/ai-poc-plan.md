# AI Generation POC Plan
## R&D Tax Relief Project Card Generator

**Document Version:** 1.0
**Date:** 2025-10-30
**Owner:** BMad Master
**Status:** Ready for Execution
**Estimated Duration:** 2 weeks (10 working days)

---

## Executive Summary

This POC validates the feasibility of using AI (Claude 3.5 Sonnet / GPT-4) to generate Polish-language R&D tax relief project cards (Ulga B+R) with ≥70% usable quality. The POC is a **CRITICAL GO/NO-GO DECISION POINT** before committing to Epic 2 (AI Generation) development.

**Why This POC is Critical:**
- Epic 2 is the **highest-risk component** of the entire project
- AI quality variance in Polish language is unproven
- Token costs could exceed budget (€0.80-1.50/doc target)
- Hallucination risk could compromise legal compliance
- Generation time must meet ≤1 min average target

**Decision Gates:**
- ✅ **GO**: If all success criteria met → Proceed with Epic 2 full development
- ⚠️ **PIVOT**: If quality 50-70% → Adjust prompts, retry with different model
- 🛑 **NO-GO**: If quality <50% or cost >€2.00/doc → Reassess product viability

---

## 1. POC Objectives

### Primary Objective
Validate that AI can generate Polish-language Ulga B+R project cards meeting the 70% usable quality threshold with acceptable cost and speed.

### Secondary Objectives
1. **Quality Validation**: Confirm ≥70% of AI-generated content requires ≤30% consultant editing
2. **Cost Validation**: Confirm generation cost is €0.80-1.50 per document (target) or ≤€2.00 (acceptable)
3. **Speed Validation**: Confirm generation time ≤1 min average, ≤15 min maximum
4. **Polish Quality**: Confirm <2 grammar errors per 1,000 words with native speaker validation
5. **Compliance Coverage**: Confirm 100% of outputs address all 3 Ulga B+R criteria (celowość, element twórczy, nowa wiedza)
6. **Hallucination Prevention**: Confirm no factual errors (invented dates, names, or project details)

---

## 2. Success Criteria (GO/NO-GO Decision)

### ✅ GO Criteria (All Must Pass)

| Criterion | Threshold | Measurement Method |
|-----------|-----------|-------------------|
| **Quality Score** | ≥70/100 | Consultant rating (0-100) on usability |
| **Cost per Document** | ≤€2.00 | Actual token cost from API calls |
| **Generation Time** | ≤15 min max | Actual wall-clock time measurement |
| **Polish Grammar** | <2 errors/1000 words | Native speaker manual review |
| **Compliance Coverage** | 100% | Keyword validation (celowość, etc.) |
| **Hallucination Rate** | 0 critical | Fact-checking vs. input data |

### ⚠️ PIVOT Criteria (Adjust & Retry)

- Quality score 50-69: Refine prompts, try alternative models
- Cost €2.00-3.00: Optimize prompts, reduce example count
- Generation time 15-25 min: Switch to GPT-4 Turbo (faster)
- Grammar errors 2-4/1000 words: Add grammar-specific instructions

### 🛑 NO-GO Criteria (Reassess Product)

- Quality score <50: AI not viable for this use case
- Cost >€3.00: Economics don't work at target pricing
- Generation time >25 min: User experience unacceptable
- Hallucination rate >1 critical per 5 docs: Legal risk too high

---

## 3. Test Dataset

### 3.1 Selection Criteria

From the 60+ example project cards in `docs/brief.md`, select **15 representative examples** covering:

**Industry Diversity** (3 from each category):
1. **Construction** - Building projects, infrastructure
2. **IT/Software** - Software development, digital solutions
3. **Manufacturing** - Industrial processes, machinery
4. **Healthcare** - Medical devices, pharmaceuticals
5. **Other** - Agriculture, energy, services

**Complexity Levels**:
- **Simple** (5 cards): 1-year projects, single technology, straightforward R&D
- **Medium** (7 cards): Multi-year projects, multiple technologies, complex methodology
- **Advanced** (3 cards): Long-duration projects, novel innovations, extensive R&D activities

**Data Quality**:
- **Rich Input** (8 cards): Detailed descriptions (>300 chars), clear objectives
- **Sparse Input** (7 cards): Minimal descriptions (<150 chars), vague objectives

### 3.2 Test Cases

**Test Case Template:**
```
TC-{ID}: {Project Name}
Industry: {Construction|IT|Manufacturing|Healthcare|Other}
Complexity: {Simple|Medium|Advanced}
Input Quality: {Rich|Sparse}
Input Data:
  - Nazwa projektu: {name}
  - Opis: {description}
  - Data rozpoczęcia: {start_date}
  - Data zakończenia: {end_date}
  - Cel projektu: {objective}
  - Osoba odpowiedzialna: {owner}
Expected Challenges:
  - {specific challenges for this case}
Success Criteria:
  - Quality score ≥70
  - All 8 sections generated
  - No hallucinations
```

**Example Test Cases:**

**TC-001: Construction - Simple - Rich**
- **Project**: Opracowanie energooszczędnego systemu wentylacji budynków
- **Input**: Detailed description of HVAC R&D project
- **Expected Challenge**: Technical terminology accuracy
- **Target**: Quality score ≥75 (rich input should yield high quality)

**TC-007: IT - Medium - Sparse**
- **Project**: Aplikacja mobilna do zarządzania projektami budowlanymi
- **Input**: Minimal description (120 chars)
- **Expected Challenge**: AI must infer methodology from limited context
- **Target**: Quality score ≥65 (sparse input acceptable if flagged)

**TC-015: Healthcare - Advanced - Rich**
- **Project**: System monitorowania parametrów życiowych pacjentów w czasie rzeczywistym
- **Input**: Complex medical device with multiple R&D phases
- **Expected Challenge**: Regulatory compliance terminology, multi-year timeline
- **Target**: Quality score ≥80 (critical domain)

---

## 4. POC Implementation Plan

### Phase 1: Setup (Days 1-2)

#### Day 1: Environment & Credentials
- [ ] Set up AWS Bedrock account (EU-Central-1 region)
- [ ] Set up Azure OpenAI account (West Europe region)
- [ ] Configure API credentials in `.env.local`
- [ ] Create POC project structure: `poc/ai-generation/`
- [ ] Install dependencies: `anthropic`, `openai`, `python-docx`, `openpyxl`

#### Day 2: Baseline Prompt & Pipeline
- [ ] Create minimal prompt → AI → Word pipeline
- [ ] Implement single-stage generation (no multi-stage yet)
- [ ] Use 1-2 example cards for few-shot learning
- [ ] Test with TC-001 (simple case) to verify pipeline works
- [ ] Measure baseline cost and time

**Deliverable**: Working end-to-end pipeline (Excel → AI → Word)

---

### Phase 2: Prompt Engineering (Days 3-6)

#### Day 3: Multi-Stage Prompts
- [ ] Implement Stage 1: Project analysis & R&D identification
- [ ] Implement Stage 2: Section-by-section generation (8 sections)
- [ ] Implement Stage 3: Coherence review & compliance check
- [ ] Test with TC-001 and TC-002 to validate stages

#### Day 4: Few-Shot Learning
- [ ] Add 2-3 example project cards to prompts
- [ ] Select examples based on domain similarity (construction → construction)
- [ ] Measure token cost impact (8,000-10,000 tokens per generation)
- [ ] Test with TC-003 and TC-004

#### Day 5: Grounding & Fact-Checking
- [ ] Add strict grounding instructions ("use only provided data")
- [ ] Implement automated fact-checking (dates, names, project titles)
- [ ] Add low-confidence flagging ([WYMAGA WERYFIKACJI] markers)
- [ ] Test with TC-005 (sparse input) to verify flagging

#### Day 6: Compliance Validation
- [ ] Add Ulga B+R keyword validation (celowość, element twórczy, nowa wiedza)
- [ ] Ensure all 3 criteria explicitly addressed in prompts
- [ ] Test with TC-006 and TC-007
- [ ] Document final prompt versions (v1.0)

**Deliverable**: Optimized multi-stage prompts with grounding and compliance checks

---

### Phase 3: Full Test Execution (Days 7-8)

#### Day 7: Claude 3.5 Sonnet Testing
- [ ] Run all 15 test cases through Claude 3.5 Sonnet via AWS Bedrock
- [ ] Measure cost per document (input + output tokens)
- [ ] Measure generation time (wall-clock)
- [ ] Generate Word documents for all 15 cases
- [ ] Save raw API responses and metadata

#### Day 8: GPT-4 Fallback Testing
- [ ] Run same 15 test cases through GPT-4 via Azure OpenAI
- [ ] Compare quality, cost, and speed vs. Claude
- [ ] Identify which model performs better per industry/complexity
- [ ] Document model selection recommendations

**Deliverable**: 30 generated project cards (15 × 2 models) with metadata

---

### Phase 4: Quality Validation (Days 9-10)

#### Day 9: Automated Quality Checks
- [ ] Run compliance keyword validation on all 30 outputs
- [ ] Run fact-checking on all 30 outputs (dates, names)
- [ ] Count grammar errors using LanguageTool (pl-PL)
- [ ] Calculate preliminary quality scores
- [ ] Identify hallucinations and low-confidence sections

#### Day 10: Native Speaker Review
- [ ] **CRITICAL**: Native Polish speaker reviews all 30 outputs
- [ ] Rate each output 0-100 for usability (consultant perspective)
- [ ] Mark sections requiring editing (measure 70% vs 30% threshold)
- [ ] Validate grammar quality (<2 errors/1000 words)
- [ ] Provide qualitative feedback (tone, terminology, professionalism)

**Deliverable**: Quality assessment report with native speaker validation

---

## 5. Resource Requirements

### Human Resources

**Required:**
1. **Developer** (full-time, 10 days)
   - Implement POC pipeline
   - Run prompt engineering experiments
   - Analyze results

2. **Native Polish Speaker** (1 day, Day 10)
   - **CRITICAL REQUIREMENT**
   - Must have R&D tax relief knowledge (ideally consultant)
   - Reviews all 30 generated cards
   - Provides quality ratings and feedback
   - **Sourcing Options**:
     - Freelancer from Upwork/Fiverr (€200-400 for 1 day)
     - Tax consulting firm contact (pro bono for pilot access)
     - University partnership (linguistics/tax law student)

**Optional:**
3. **Product Owner** (20% time, checkpoint reviews)
   - Review Day 2, Day 6, and Day 10 deliverables
   - Adjust success criteria if needed

### Technical Resources

**Cloud Services:**
- AWS Bedrock (Claude 3.5 Sonnet): ~€20-30 budget for 15 test cases
- Azure OpenAI (GPT-4): ~€25-35 budget for 15 test cases
- **Total AI Cost**: €50-70 for POC

**Software:**
- Python 3.11+ with libraries: anthropic, openai, python-docx, openpyxl
- LanguageTool (open-source grammar checker)
- Excel for test case input
- Word for output validation

**Data:**
- 15 test cases extracted from `docs/brief.md` (60+ examples)
- 2-3 high-quality example cards for few-shot prompts

---

## 6. Cost & Time Estimation

### 6.1 Token Cost Calculation

**Assumptions** (from tech report):
- Average input: 11,000-15,000 tokens (prompt + examples + data)
- Average output: 2,800-4,150 tokens (8 sections)
- Claude 3.5 Sonnet pricing: $3 input / $15 output per 1M tokens
- GPT-4 pricing: $5 input / $15 output per 1M tokens (Azure)

**Per Document Cost:**

| Model | Input Tokens | Output Tokens | Input Cost | Output Cost | Total |
|-------|--------------|---------------|------------|-------------|-------|
| Claude 3.5 | 13,000 avg | 3,500 avg | €0.036 | €0.049 | **€0.085** |
| GPT-4 | 13,000 avg | 3,500 avg | €0.061 | €0.049 | **€0.110** |

**With Retry Buffer (30%):**
- Claude: €0.085 × 1.3 = **€0.11 per doc**
- GPT-4: €0.110 × 1.3 = **€0.14 per doc**

**POC Total Cost:**
- 15 docs × 2 models × €0.12 avg = **€3.60 AI cost**
- Add infrastructure overhead: **€5-10 total**
- ✅ **WELL UNDER €2.00/doc target**

### 6.2 Time Estimation

**Generation Time per Document:**
- Claude API latency: 30-90 seconds (avg 60s)
- GPT-4 API latency: 20-60 seconds (avg 40s)
- Multi-stage (3 stages): 3× latency
- **Estimated**: 2-5 minutes per document

**POC Execution Time:**
- 15 docs × 2 models × 4 min avg = **120 minutes (2 hours)**
- ✅ **Easily meets ≤1 min target (single-stage) or ≤5 min (multi-stage)**

---

## 7. Deliverables

### POC Outputs

1. **POC Report** (`docs/ai-poc-report.md`)
   - Executive summary with GO/NO-GO decision
   - Quality scores for all 30 generated cards
   - Cost analysis (actual vs. target)
   - Speed analysis (actual vs. target)
   - Native speaker qualitative feedback
   - Model comparison (Claude vs GPT-4)
   - Recommendations for Epic 2 implementation

2. **Optimized Prompts** (`poc/ai-generation/prompts/`)
   - `stage1-analysis.txt` - Project analysis prompt
   - `stage2-generation.txt` - Section generation prompt
   - `stage3-review.txt` - Coherence review prompt
   - `few-shot-examples.md` - Example cards used
   - `grounding-instructions.md` - Anti-hallucination guidelines

3. **Test Results** (`poc/ai-generation/results/`)
   - `test-cases.xlsx` - 15 test case inputs
   - `claude-outputs/` - 15 Word documents from Claude
   - `gpt4-outputs/` - 15 Word documents from GPT-4
   - `quality-scores.csv` - All quality metrics
   - `cost-breakdown.csv` - Token usage and costs
   - `native-speaker-feedback.md` - Detailed review notes

4. **Code Artifacts** (`poc/ai-generation/src/`)
   - `generate.py` - Main generation script
   - `validate.py` - Quality validation script
   - `fact_check.py` - Fact-checking engine
   - `requirements.txt` - Python dependencies
   - `README.md` - How to run POC

---

## 8. Risk Mitigation

### High Risks

**Risk 1: Polish Quality Unacceptable**
- **Probability**: Medium (30%)
- **Impact**: High (blocks Epic 2)
- **Mitigation**:
  - Test both Claude and GPT-4 (fallback option)
  - Iterate prompts if initial results are 50-70%
  - Accept lower threshold (60%) with stronger consultant editing workflow
- **Contingency**: If <50%, reassess product viability or pivot to template-based approach

**Risk 2: Hallucination Rate Too High**
- **Probability**: Medium (25%)
- **Impact**: High (legal risk)
- **Mitigation**:
  - Strict grounding instructions in prompts
  - Automated fact-checking vs. input data
  - Native speaker validation flags invented facts
  - Low-confidence section flagging
- **Contingency**: Add human verification step before final output

**Risk 3: Cost Exceeds Budget**
- **Probability**: Low (15%)
- **Impact**: Medium (economics don't work)
- **Mitigation**:
  - Optimize prompt length (reduce example count)
  - Use GPT-4 Turbo (cheaper than GPT-4)
  - Consider single-stage vs. multi-stage trade-off
- **Contingency**: Accept €2.00-3.00/doc if quality is exceptional

**Risk 4: Cannot Find Native Polish Speaker**
- **Probability**: Low (10%)
- **Impact**: High (cannot validate quality)
- **Mitigation**:
  - Source freelancer from Upwork/Fiverr immediately
  - Reach out to tax consulting firms for pilot partnership
  - Use LanguageTool + self-assessment as fallback (not ideal)
- **Contingency**: Extend POC timeline by 3-5 days to find qualified reviewer

---

## 9. Decision Framework

### Day 10: GO/NO-GO Decision

**GO Decision** (Proceed to Epic 2):
- ✅ Quality score ≥70 on ≥12/15 test cases (80%)
- ✅ Cost ≤€2.00/doc
- ✅ Generation time ≤15 min
- ✅ Native speaker confirms <2 grammar errors/1000 words
- ✅ Zero critical hallucinations
- ✅ 100% compliance coverage (all 3 Ulga B+R criteria)

**PIVOT Decision** (Adjust & Retry):
- ⚠️ Quality score 50-70 → Refine prompts, retry with 5 new test cases
- ⚠️ Cost €2.00-3.00 → Optimize prompts, retry
- ⚠️ Time 15-25 min → Switch models, retry
- **Timeline**: +5 days for pivot iteration

**NO-GO Decision** (Reassess Product):
- 🛑 Quality score <50 on >5 test cases
- 🛑 Cost >€3.00/doc even after optimization
- 🛑 Time >25 min consistently
- 🛑 Hallucination rate >20% (>3 critical in 15 docs)
- **Action**: Escalate to Product Owner for product strategy reassessment

---

## 10. Success Metrics

### Quantitative Metrics

| Metric | Target | Acceptable | Unacceptable |
|--------|--------|-----------|--------------|
| Quality Score | ≥75/100 | ≥70/100 | <70/100 |
| Cost per Doc | €0.80-1.50 | ≤€2.00 | >€2.00 |
| Generation Time | ≤1 min | ≤5 min | >15 min |
| Grammar Errors | <1/1000 | <2/1000 | >2/1000 |
| Compliance Coverage | 100% | 100% | <100% |
| Hallucination Rate | 0% | <5% | >10% |

### Qualitative Metrics (Native Speaker)

- **Professional Tone**: Appropriate for tax authority submission
- **Technical Accuracy**: Correct use of R&D terminology
- **Coherence**: Logical flow between sections
- **Completeness**: All 8 sections substantive (not placeholder text)
- **Consultant Confidence**: Would consultant submit this with <30% editing?

---

## 11. Timeline

### 2-Week POC Schedule

```
Week 1:
├─ Mon (Day 1): Environment setup, API credentials
├─ Tue (Day 2): Baseline pipeline implementation
├─ Wed (Day 3): Multi-stage prompt engineering
├─ Thu (Day 4): Few-shot learning optimization
└─ Fri (Day 5): Grounding & fact-checking

Week 2:
├─ Mon (Day 6): Compliance validation, prompt v1.0
├─ Tue (Day 7): Claude testing (15 test cases)
├─ Wed (Day 8): GPT-4 testing (15 test cases)
├─ Thu (Day 9): Automated quality checks
└─ Fri (Day 10): Native speaker review, GO/NO-GO decision
```

**Milestones:**
- **Day 2**: Pipeline working (smoke test)
- **Day 6**: Prompts optimized and versioned
- **Day 8**: All 30 outputs generated
- **Day 10**: **GO/NO-GO DECISION**

---

## 12. Handoff to Epic 2

### If GO Decision

**Epic 2 Implementation Plan:**
1. **Week 1-2**: Integrate POC prompts into production codebase
2. **Week 3-4**: Build quality scoring algorithm and compliance checks
3. **Week 5-6**: Implement multi-model failover (Claude → GPT-4)
4. **Week 7-8**: Add section regeneration and hint functionality
5. **Week 9-10**: Testing and refinement

**Carry Forward from POC:**
- Optimized prompts (stage 1-3)
- Few-shot example selection strategy
- Fact-checking engine
- Quality scoring baseline
- Native speaker feedback insights

### If PIVOT Decision

**Iteration Plan:**
- 5 additional test cases
- Prompt refinement based on failure analysis
- Model parameter tuning (temperature, top_p)
- Alternative model testing (GPT-4 Turbo, Claude Opus)
- Timeline: +1 week

### If NO-GO Decision

**Product Strategy Reassessment:**
- Can we accept lower quality threshold (e.g., 50% AI, 50% consultant)?
- Should we pivot to template-based generation with AI augmentation?
- Is there alternative market segment (simpler projects only)?
- Escalate to Product Owner and stakeholders

---

## 13. Appendices

### Appendix A: Prompt Engineering Checklist

**Essential Prompt Elements:**
- [ ] Clear role definition ("You are an expert in Polish R&D tax relief")
- [ ] Strict grounding ("Use ONLY the provided project data")
- [ ] Output format specification (8 sections, Polish language)
- [ ] Compliance keywords (celowość, element twórczy, nowa wiedza)
- [ ] Few-shot examples (2-3 cards)
- [ ] Low-confidence flagging instructions
- [ ] Professional tone guidance
- [ ] Length targets per section (500-800 words)

### Appendix B: Fact-Checking Rules

**Automated Checks:**
1. Project name matches input exactly
2. Start/end dates match input exactly
3. Responsible person name matches input exactly
4. No dates before start_date or after end_date
5. No invented company names, technologies, or methodologies
6. All numbers (budgets, timelines) traceable to input

### Appendix C: Quality Scoring Algorithm (Preliminary)

```python
quality_score = (
    section_completeness_score * 0.30 +  # All 8 sections present
    content_length_score * 0.20 +        # Minimum length thresholds
    grammar_score * 0.20 +               # <2 errors/1000 words
    compliance_score * 0.20 +            # All 3 criteria present
    factual_accuracy_score * 0.10        # No hallucinations
)
```

**Range**: 0-100, where:
- 90-100: Excellent (minimal editing needed)
- 70-89: Good (target quality)
- 50-69: Acceptable (significant editing needed)
- <50: Poor (faster to write from scratch)

---

## Document Control

**Author**: BMad Master
**Reviewers**: Product Owner, QA Architect
**Approvers**: Product Owner
**Next Review**: After Day 10 (GO/NO-GO decision)

**Change Log:**

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-10-30 | 1.0 | Initial POC plan created | BMad Master |

---

**END OF POC PLAN**
