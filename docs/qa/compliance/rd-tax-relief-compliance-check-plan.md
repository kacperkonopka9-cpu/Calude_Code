# R&D Tax Relief Compliance Check Plan
## Innovation Tax Relief Analysis - Quality Assurance Framework

**Document Version:** 1.0
**Date:** 2025-10-29
**QA Architect:** Quinn
**Project:** R&D Tax Relief Project Card Generator
**Status:** Active

---

## Executive Summary

This compliance check plan establishes a comprehensive quality assurance framework for the R&D Tax Relief Project Card Generator system. The plan ensures that AI-generated project cards meet Polish Ulga B+R (Research & Development tax relief) regulatory requirements while maintaining high quality standards for consultant use.

**Quality Targets:**
- ≥70% AI-generated content quality (NFR3)
- ≥90% compliance validation pass rate
- <2 grammar errors per 1,000 words
- Quality score ≥70 for 80%+ of generated cards

---

## 1. Regulatory Compliance Requirements

### 1.1 Ulga B+R Core Criteria

The Polish R&D tax relief program (Ulga B+R) requires project cards to demonstrate three mandatory criteria:

| Criterion | Polish Term | Validation Method | Pass Threshold |
|-----------|-------------|-------------------|----------------|
| **Purposefulness** | Celowość | Keyword analysis + semantic validation | Must be explicitly addressed in "Cel projektu" section |
| **Creative Element** | Element twórczy | Presence of innovation indicators, technical challenges | Must be documented in "Prace o charakterze twórczym" section |
| **New Knowledge** | Nowa wiedza | Documentation of learning outcomes, novel solutions | Must be articulated in "Nowatorskość i innowacyjność" section |

### 1.2 Mandatory Documentation Sections

All generated project cards must contain the following 8 sections (per FR6):

1. **Nazwa projektu** - Project title
2. **Cel projektu** - Project goal/objective
3. **Opis projektu** - Project description
4. **Nowatorskość i innowacyjność** - Innovation and novelty
5. **Metodologia prac B+R** - R&D methodology
6. **Rezultaty projektu** - Project results
7. **Koszty kwalifikowane** - Qualified costs
8. **Harmonogram** - Timeline/schedule

**Completeness Threshold:** 100% (all 8 sections must be present and non-empty)

### 1.3 Content Quality Requirements

**Polish Language Standards:**
- Professional technical terminology
- Clear, non-specialist language (per Ulga B+R guidelines)
- Proper grammar and syntax
- Target: <2 grammar errors per 1,000 words

**Content Length Requirements:**
- **Minimum thresholds** (per FR2):
  - Opis: ≥100 characters input → 200-400 words output
  - Cel projektu: ≥50 characters input → 150-300 words output
  - Other sections: ≥100 words each

**Technical Depth:**
- Detailed technical descriptions (3-4 paragraphs per major section)
- Explicit R&D problem statements
- Solution methodology documentation
- Innovation level justification (company vs. national scale)

---

## 2. Quality Assurance Framework

### 2.1 Three-Stage Validation Model

```
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: Pre-Generation Validation (Input Quality)         │
│  - Excel structure validation                                │
│  - Required column presence                                  │
│  - Data type correctness                                     │
│  - Content length adequacy                                   │
│  - Date logic consistency                                    │
│  Result: PASS → Proceed | FAIL → Display errors, block      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: Post-Generation Validation (AI Output Quality)    │
│  - Section completeness check (8/8)                          │
│  - Compliance keyword validation                             │
│  - Polish grammar checking (LanguageTool)                    │
│  - Fact-checking vs. input data                              │
│  - Quality scoring algorithm (0-100%)                        │
│  Result: Quality score + flagged sections                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3: Consultant Review (Human QA Gate)                 │
│  - Manual content review                                     │
│  - Factual accuracy verification                             │
│  - Technical correctness assessment                          │
│  - Section approval workflow                                 │
│  Result: Edited content → Final export                       │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Quality Scoring Algorithm (FR9)

**Composite Score (0-100%):**

| Component | Weight | Calculation Method |
|-----------|--------|-------------------|
| **Section Completeness** | 40% | (Present sections / 8) × 40 |
| **Content Length Adequacy** | 20% | Average section length vs. threshold |
| **Polish Language Quality** | 20% | Grammar score from LanguageTool |
| **Ulga B+R Keyword Presence** | 20% | Compliance keywords detected / expected |

**Quality Thresholds:**
- **≥80**: Excellent (green badge) - Minimal editing expected
- **70-79**: Good (yellow badge) - Light editing recommended
- **50-69**: Fair (orange badge) - Moderate editing required
- **<50**: Poor (red badge) - Substantial editing or regeneration needed

**Target:** ≥70 quality score for 80%+ of generated cards (per Epic 2 success metrics)

### 2.3 Automated Validation Checks

#### 2.3.1 Compliance Validation
**Check:** Ulga B+R criteria presence
**Implementation:** Epic 7 - Automated keyword and semantic analysis

```yaml
Validation Rules:
  celowość_check:
    required_keywords: ["cel", "zamiar", "przyczyna", "potrzeba"]
    required_section: "Cel projektu"
    threshold: at_least_one_keyword_present

  element_twórczy_check:
    required_keywords: ["twórczy", "innowacyjny", "nowy", "oryginalny", "unikatowy"]
    required_section: "Prace o charakterze twórczym"
    threshold: at_least_two_keywords_present

  nowa_wiedza_check:
    required_keywords: ["wiedza", "nauka", "badania", "rozwój", "poznanie"]
    required_section: "Nowatorskość i innowacyjność"
    threshold: at_least_one_keyword_present
```

**Pass Criteria:** All 3 criteria must be validated (100% compliance coverage)

#### 2.3.2 Fact-Checking Validation
**Check:** Consistency with input Excel data
**Implementation:** Epic 7 - Automated cross-reference

```yaml
Fact_Checks:
  - name: "Project Name Consistency"
    rule: Generated "Nazwa projektu" must match input "Nazwa projektu"
    tolerance: exact_match

  - name: "Date Consistency"
    rule: Generated dates must match input "Data rozpoczęcia" and "Data zakończenia"
    tolerance: exact_match

  - name: "Person Responsibility"
    rule: Generated "Osoba odpowiedzialna" must match input
    tolerance: exact_match

  - name: "Goal Alignment"
    rule: Generated "Cel projektu" must incorporate input "Cel projektu" text
    tolerance: semantic_similarity ≥ 0.7
```

**Pass Criteria:** ≥95% fact accuracy (per Epic 7 success metrics)

#### 2.3.3 Polish Grammar Validation
**Check:** Grammar, spelling, and syntax correctness
**Implementation:** LanguageTool integration (Epic 7)

**Validation Rules:**
- Run LanguageTool Polish language checker on all generated text
- Flag grammar errors, spelling mistakes, stylistic issues
- Categorize by severity: CRITICAL / MAJOR / MINOR
- Calculate grammar score: `100 - (errors × 2)`

**Pass Criteria:**
- <2 grammar errors per 1,000 words (per Epic 2 success metrics)
- False positive rate ≤10% (per Epic 7 success metrics)

#### 2.3.4 Section Completeness Validation
**Check:** All 8 required sections present and non-empty
**Implementation:** Structural validation

**Validation Rules:**
```python
required_sections = [
    "Nazwa projektu",
    "Cel projektu",
    "Opis projektu",
    "Nowatorskość i innowacyjność",
    "Metodologia prac B+R",
    "Rezultaty projektu",
    "Koszty kwalifikowane",
    "Harmonogram"
]

for section in required_sections:
    assert section in generated_card
    assert len(generated_card[section]) >= MIN_LENGTH_THRESHOLD
```

**Pass Criteria:** 100% completeness (all 8 sections present and adequate length)

---

## 3. Testing Strategy

### 3.1 Test Coverage Framework

| Test Type | Coverage Target | Responsibility | Tooling |
|-----------|----------------|----------------|---------|
| **Unit Tests** | 80%+ code coverage | Developer | pytest (backend), Jest (frontend) |
| **Integration Tests** | All API endpoints | Developer + QA | pytest-asyncio, React Testing Library |
| **E2E Tests** | Critical user paths | QA | Playwright |
| **AI Quality Tests** | 60+ example validation | QA + Domain Expert | Custom validation suite |
| **Compliance Tests** | Ulga B+R criteria | QA + Legal | Automated compliance checker |
| **Performance Tests** | NFR targets | QA + DevOps | k6, Lighthouse |
| **Accessibility Tests** | WCAG 2.1 AA | QA | axe-core, Pa11y |

### 3.2 AI Quality Validation Test Suite

**Test Data:** 60+ real project card examples (from brief.md)

**Test Categories:**

1. **Domain Diversity Tests**
   - Construction projects (10+ examples)
   - Industrial/energy systems (15+ examples)
   - IT systems (10+ examples)
   - Manufacturing processes (10+ examples)
   - Specialized equipment (15+ examples)

2. **Quality Benchmark Tests**
   ```yaml
   test_approach: "Generate cards from sample inputs, compare against gold standard"

   metrics:
     - content_similarity: ≥70% semantic similarity to reference cards
     - quality_score: ≥70 for 80%+ of generated cards
     - grammar_errors: <2 per 1,000 words
     - compliance_coverage: 100% (all 3 criteria addressed)
     - edit_distance: ≤30% character changes needed
   ```

3. **Regression Tests**
   - Lock baseline quality scores for 10 representative examples
   - Run on every prompt change or model update
   - Alert if quality drops >5 points
   - Prevent deployment if quality drops >10 points

4. **Edge Case Tests**
   - Minimal input data (50-100 characters)
   - Maximum input data (500+ characters)
   - Multi-year projects
   - Cross-industry projects
   - Non-standard terminology

### 3.3 Manual QA Testing Protocol

**Frequency:** Every sprint + before major releases

**Test Team:**
- QA Engineer: Technical validation
- Native Polish Speaker: Language quality
- Domain Expert (R&D Consultant): Compliance validation

**Test Scenarios:**
1. **Happy Path Testing**
   - Upload valid Excel with 5 projects
   - Monitor batch processing
   - Review all generated cards
   - Verify quality scores
   - Export to Word documents
   - Validate Word formatting

2. **Error Path Testing**
   - Upload invalid Excel (missing columns, wrong formats)
   - Verify error messages clarity
   - Test retry functionality
   - Test generation failures
   - Verify graceful degradation

3. **Quality Validation Testing**
   - Review 10 generated cards end-to-end
   - Rate content quality (1-5 scale)
   - Verify compliance criteria addressed
   - Check grammar and terminology
   - Measure edit time required

4. **Accessibility Testing**
   - Keyboard-only navigation
   - Screen reader compatibility (NVDA/JAWS)
   - Color contrast validation
   - Focus indicator visibility

**Pass Criteria:**
- Zero blocking bugs
- ≥4.0/5.0 quality rating from domain expert
- All compliance criteria addressed in generated cards
- WCAG 2.1 AA violations = 0

---

## 4. Compliance Checklist for AI-Generated Cards

### 4.1 Pre-Export Validation Checklist

**Use Case:** Consultant reviews this checklist before exporting project card

| # | Validation Check | Automated | Manual | Pass Criteria |
|---|-----------------|-----------|--------|---------------|
| 1 | All 8 sections present | ✅ | - | 8/8 sections |
| 2 | Celowość (purposefulness) addressed | ✅ | ✅ | Keyword present + semantically validated |
| 3 | Element twórczy (creativity) documented | ✅ | ✅ | Creative aspects explicitly described |
| 4 | Nowa wiedza (new knowledge) articulated | ✅ | ✅ | Learning outcomes documented |
| 5 | Project name matches input data | ✅ | - | Exact match |
| 6 | Dates match input data | ✅ | - | Exact match |
| 7 | Responsible person matches input | ✅ | - | Exact match |
| 8 | Project goal aligns with input | ✅ | ✅ | Semantic similarity ≥0.7 |
| 9 | Technical description adequate depth | - | ✅ | 200-400 words, 3-4 paragraphs |
| 10 | R&D problems clearly stated | - | ✅ | Specific technical challenges identified |
| 11 | Solutions/methodology documented | - | ✅ | Clear approach described |
| 12 | Innovation level justified | - | ✅ | Company or national scale specified |
| 13 | Polish grammar correct | ✅ | ✅ | <2 errors per 1,000 words |
| 14 | Professional terminology used | - | ✅ | Domain-appropriate language |
| 15 | Non-specialist language clarity | - | ✅ | Understandable to non-experts |
| 16 | No hallucinated facts | ✅ | ✅ | All claims verifiable from input |
| 17 | Quality score ≥70 | ✅ | - | System-calculated score |
| 18 | Word template formatting correct | - | ✅ | Matches government template |
| 19 | No sensitive data exposure | - | ✅ | Only intended project info included |
| 20 | Final consultant approval | - | ✅ | Consultant marks as "Approved" |

**Overall Pass Criteria:**
- All automated checks: 100% pass rate
- All manual checks: Consultant approval required
- Quality score: ≥70 (target), ≥50 (minimum acceptable)

### 4.2 Batch Quality Assessment

**Frequency:** After each batch completes generation

**Metrics to Review:**

```yaml
Batch Quality Report:
  batch_id: "BATCH-2025-001"
  total_projects: 15

  quality_distribution:
    excellent (≥80): 8 cards (53%)
    good (70-79): 5 cards (33%)
    fair (50-69): 2 cards (13%)
    poor (<50): 0 cards (0%)

  average_quality_score: 76.4

  compliance_validation:
    celowość_coverage: 15/15 (100%)
    element_twórczy_coverage: 15/15 (100%)
    nowa_wiedza_coverage: 15/15 (100%)

  grammar_quality:
    total_words: 42,500
    grammar_errors: 68
    error_rate: 1.6 per 1,000 words ✅

  fact_accuracy:
    facts_checked: 225
    facts_correct: 220
    accuracy_rate: 97.8% ✅

  generation_performance:
    average_time: 52 seconds
    target: ≤60 seconds ✅
```

**Decision Framework:**
- **All checks pass:** Proceed to consultant review
- **Quality score low (<70 for >20% cards):** Flag batch for intensive review
- **Compliance failure:** Regenerate affected cards
- **Grammar issues:** Apply automated corrections, re-validate
- **Fact errors:** Block export, require manual correction

---

## 5. Risk Assessment & Mitigation

### 5.1 Quality Risks

| Risk | Probability | Impact | Mitigation Strategy | Owner |
|------|------------|--------|---------------------|-------|
| **AI Hallucination** | HIGH | CRITICAL | Grounding prompts + fact-checking + mandatory review | Dev + QA |
| **Polish Language Quality Variance** | MEDIUM | HIGH | Multi-model strategy + native QA + LanguageTool | QA |
| **Compliance Gaps** | MEDIUM | CRITICAL | Automated compliance validation + domain expert review | QA + Legal |
| **Inconsistent Quality Across Domains** | MEDIUM | MEDIUM | Domain-specific examples + project type detection | Dev |
| **False Positive Grammar Flags** | LOW | LOW | Manual review workflow + error categorization | QA |
| **Template Format Mismatch** | LOW | HIGH | Automated format validation + visual diff testing | QA |

### 5.2 Regulatory Risks

| Risk | Probability | Impact | Mitigation Strategy | Owner |
|------|------------|--------|---------------------|-------|
| **Tax Authority Rejection** | LOW | CRITICAL | Pilot testing + consultant validation + compliance checklist | QA + Legal |
| **Ulga B+R Requirements Change** | MEDIUM | HIGH | Regulatory monitoring + update mechanism + version control | Product |
| **Data Privacy Violation** | LOW | CRITICAL | EU-only processing + encryption + GDPR compliance audit | Security + Legal |
| **Audit Trail Insufficiency** | LOW | MEDIUM | Comprehensive logging + retention policies | DevOps |

### 5.3 Mitigation Success Criteria

**Monitoring:**
- Track tax authority acceptance rates (target: ≥95%)
- Monitor consultant satisfaction scores (target: ≥4.0/5.0)
- Log quality score trends over time
- Alert on quality degradation

**Escalation:**
- Quality score drops >10 points: Immediate investigation
- Tax authority rejection: Root cause analysis + process review
- Compliance violation: Legal review + system audit
- Multiple consultant complaints: QA deep dive

---

## 6. Quality Gates & Decision Framework

### 6.1 QA Gate Process

**Integration with BMad Workflow:**

```
Story Implementation → Dev Testing → QA Gate Decision → Deployment

Gate Statuses:
  PASS: All quality criteria met, ready for production
  CONCERNS: Minor issues identified, can proceed with monitoring
  FAIL: Critical issues, blocks deployment
  WAIVED: Known issues accepted with explicit rationale
```

### 6.2 QA Gate Criteria by Story Type

#### For AI Generation Stories:
- [ ] Quality score ≥70 for 80%+ test cases
- [ ] Compliance validation 100% pass rate
- [ ] Grammar error rate <2 per 1,000 words
- [ ] Fact accuracy ≥95%
- [ ] Domain expert approval obtained
- [ ] No hallucinations detected in sample testing

#### For Validation Stories:
- [ ] Automated checks execute successfully
- [ ] False positive rate ≤10%
- [ ] Performance targets met (validation <2 seconds)
- [ ] Clear error messages in Polish
- [ ] Edge cases handled gracefully

#### For Export Stories:
- [ ] Word format matches government template
- [ ] All 8 sections properly formatted
- [ ] Encoding correct (UTF-8, Polish characters)
- [ ] File size ≤2MB (per NFR10)
- [ ] Batch export (ZIP) successful

### 6.3 Post-Deployment Quality Monitoring

**Continuous Monitoring Metrics:**
1. **Quality Score Trend** - Weekly average
2. **Consultant Edit Rate** - % of content modified
3. **Regeneration Frequency** - How often sections re-generated
4. **Export Success Rate** - % of cards exported without errors
5. **Consultant Satisfaction** - Post-batch surveys
6. **Tax Authority Feedback** - Acceptance/rejection tracking (when available)

**Alert Thresholds:**
- Quality score drops >5 points from baseline: WARNING
- Edit rate increases >10% from baseline: INVESTIGATE
- Export failures >5%: CRITICAL
- Consultant satisfaction <4.0/5.0: REVIEW PROCESS

---

## 7. Implementation Recommendations

### 7.1 For Architect
- Design prompt versioning system for A/B testing quality improvements
- Implement quality monitoring dashboard with real-time metrics
- Create automated regression testing pipeline for prompt changes
- Design compliance validation as separate microservice for flexibility

### 7.2 For Developer
- Implement all Epic 7 automated validation checks
- Create comprehensive unit tests for quality scoring algorithm
- Build fact-checking engine with semantic similarity comparison
- Integrate LanguageTool API with error categorization
- Implement quality score caching to avoid redundant calculations

### 7.3 For QA (Immediate Actions)
1. **Create Test Data Repository** (Week 1)
   - Curate 15 representative examples from 60+ project cards
   - Categorize by domain, complexity, edge cases
   - Create gold standard reference outputs
   - Document expected quality scores

2. **Build AI Quality Test Suite** (Weeks 2-3)
   - Automated generation of all 15 test cases
   - Quality score validation
   - Compliance keyword checking
   - Grammar error rate calculation
   - Semantic similarity scoring vs. reference

3. **Establish Baseline Metrics** (Week 4)
   - Run test suite on initial prompt version
   - Lock baseline quality scores
   - Document acceptable variance ranges
   - Create regression test automation

4. **Design Manual QA Protocol** (Week 2)
   - Develop test scenarios document
   - Create quality rating rubric for consultants
   - Design feedback collection forms
   - Plan pilot testing approach (2-3 consultants, 2-4 weeks)

5. **Pilot Testing Preparation** (Before MVP launch)
   - Recruit 3-5 pilot consultants
   - Provide test batches (10-15 cards each)
   - Collect detailed feedback on quality, compliance, usability
   - Measure time savings and edit rates
   - Validate compliance acceptance

### 7.4 For Product Owner
- Define acceptance criteria for Epic 7 stories with specific quality thresholds
- Prioritize native Polish speaker involvement in testing
- Plan consultant pilot program timeline
- Establish feedback loop from tax authorities (if possible)

---

## 8. Appendices

### Appendix A: Ulga B+R Reference Documentation
- Government template: `input/2025_09_10_Szablon karty projektu - do uzupełnienia.docx`
- Instructions: `input/Instrukcja do karty projektu.pdf`
- 60+ example cards: `examples/` directory

### Appendix B: Quality Scoring Algorithm (Detailed)

```python
def calculate_quality_score(generated_card, input_data):
    """
    Calculate 0-100 quality score for generated project card
    """
    scores = {}

    # Component 1: Section Completeness (40 points)
    required_sections = 8
    present_sections = count_present_sections(generated_card)
    scores['completeness'] = (present_sections / required_sections) * 40

    # Component 2: Content Length Adequacy (20 points)
    length_scores = []
    for section in generated_card.sections:
        actual_length = len(section.content.split())
        expected_length = get_expected_length(section.type)
        length_ratio = min(actual_length / expected_length, 1.0)
        length_scores.append(length_ratio)
    scores['length'] = mean(length_scores) * 20

    # Component 3: Polish Language Quality (20 points)
    grammar_result = languagetool_check(generated_card.full_text)
    total_words = count_words(generated_card.full_text)
    error_rate = len(grammar_result.errors) / (total_words / 1000)
    grammar_score = max(100 - (error_rate * 10), 0)  # Penalize 10 pts per error/1000 words
    scores['grammar'] = (grammar_score / 100) * 20

    # Component 4: Ulga B+R Keyword Presence (20 points)
    compliance_keywords = {
        'celowość': ['cel', 'zamiar', 'przyczyna', 'potrzeba'],
        'element_twórczy': ['twórczy', 'innowacyjny', 'nowy', 'oryginalny'],
        'nowa_wiedza': ['wiedza', 'nauka', 'badania', 'rozwój']
    }
    keyword_coverage = calculate_keyword_coverage(generated_card, compliance_keywords)
    scores['compliance'] = keyword_coverage * 20

    # Total Score
    total_score = sum(scores.values())

    return {
        'total': round(total_score, 1),
        'breakdown': scores,
        'grade': get_grade(total_score)  # Excellent/Good/Fair/Poor
    }
```

### Appendix C: Test Data Examples

**Example 1: High-Quality Expected Output**
```
Project: Mycie łopatek i korpusu turbiny
Input Opis: "System czyszczenia łopatek turbiny parowej"
Expected Output Quality: ≥80
Expected Content: 300-400 word technical description including:
  - New cleaning technology description
  - Technical parameters and challenges
  - R&D aspects (creative solutions, new knowledge gained)
  - Innovation justification at company level
```

**Example 2: Edge Case - Minimal Input**
```
Project: Nowy system IT
Input Opis: "System zarządzania projektami" (50 chars - minimum threshold)
Expected Output Quality: 65-75
Expected Content: AI must expand limited input into adequate description
  - Should prompt for more details in future enhancement
  - Must not hallucinate specific technical details
  - Should use general IT project B+R language patterns
```

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **QA Architect** | Quinn | ________________ | 2025-10-29 |
| **Product Owner** | ________________ | ________________ | ________ |
| **Technical Lead** | ________________ | ________________ | ________ |
| **Domain Expert (R&D Consultant)** | ________________ | ________________ | ________ |

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-29 | Quinn (QA Agent) | Initial compliance check plan created |

---

**End of Compliance Check Plan**
