# AI Generation POC
## R&D Tax Relief Project Card Generator

This directory contains the Proof of Concept (POC) for validating AI-powered generation of Polish-language R&D tax relief project cards.

---

## Directory Structure

```
poc/
├── README.md                    # This file
├── test-cases.md                # Detailed test case specifications
├── ai-generation/              # POC execution workspace
│   ├── test-cases.csv          # Excel-compatible test input data
│   ├── prompts/                # Optimized prompts (TBD - Day 6)
│   ├── results/                # Generated outputs (TBD - Day 7-8)
│   ├── src/                    # POC implementation scripts (TBD - Day 1-6)
│   └── README.md               # POC execution guide (TBD)
└── reports/                    # POC outcomes (TBD - Day 10)
```

---

## Quick Start

### Phase 1: Review Test Cases

1. **Read detailed specifications**: `test-cases.md`
   - 15 test cases across 5 industries
   - Complexity levels: Simple (6), Medium (6), Advanced (3)
   - Input quality: Rich (9), Sparse (6)

2. **Open test data**: `ai-generation/test-cases.csv`
   - Import into Excel or use directly
   - Required columns: Nazwa projektu, Opis, Data rozpoczęcia, Data zakończenia, Cel projektu, Osoba odpowiedzialna

### Phase 2: Execute POC

Follow the detailed 10-day plan in `/docs/ai-poc-plan.md`:

**Week 1: Setup & Prompt Engineering**
- Days 1-2: Environment setup, baseline pipeline
- Days 3-6: Multi-stage prompts, grounding, compliance

**Week 2: Testing & Decision**
- Day 7: Claude 3.5 Sonnet testing (15 cases)
- Day 8: GPT-4 testing (15 cases)
- Day 9: Automated quality checks
- Day 10: Native speaker review → **GO/NO-GO DECISION**

---

## Test Case Summary

| ID | Project | Industry | Complexity | Input | Target Quality |
|----|---------|----------|------------|-------|----------------|
| TC-001 | ERP System | IT | Simple | Rich | ≥80 |
| TC-002 | Task Management | IT | Simple | Sparse | ≥65 |
| TC-003 | Mobile Construction App | IT | Medium | Rich | ≥75 |
| TC-004 | HAUTAU Windows | Manufacturing | Simple | Rich | ≥78 |
| TC-005 | Aluminum Welding | Manufacturing | Medium | Sparse | ≥60 |
| TC-006 | NFC Door System | Manufacturing | Medium | Rich | ≥80 |
| TC-007 | Autonomous Forklifts | Manufacturing | Advanced | Rich | ≥85 |
| TC-008 | Fuel System | Energy | Simple | Rich | ≥75 |
| TC-009 | Turbine Upgrade | Energy | Medium | Sparse | ≥55 |
| TC-010 | Energy Storage | Energy | Advanced | Rich | ≥90 |
| TC-011 | Heritage Tynks | Construction | Simple | Rich | ≥78 |
| TC-012 | High-Rise Facade | Construction | Medium | Sparse | ≥58 |
| TC-013 | Smart Windows | Construction | Advanced | Rich | ≥92 |
| TC-014 | Pharma Logistics | Other | Medium | Rich | ≥82 |
| TC-015 | Wood Processing | Other | Simple | Sparse | ≥50 |

**Average Target Quality:** 72.5 (meets ≥70 POC success threshold)

---

## Success Criteria

### ✅ GO Criteria (Proceed to Epic 2)

All must pass:
- Quality score ≥70 on 12/15 test cases (80%)
- Cost ≤€2.00 per document
- Generation time ≤15 min max
- Polish grammar <2 errors/1000 words
- Compliance coverage 100% (all 3 Ulga B+R criteria)
- Hallucination rate 0 critical errors

### ⚠️ PIVOT Criteria (Refine & Retry)

- Quality 50-70 → Optimize prompts
- Cost €2-3 → Reduce prompt complexity
- Time 15-25 min → Switch models

### 🛑 NO-GO Criteria (Reassess Product)

- Quality <50 on >5 test cases
- Cost >€3.00 after optimization
- Hallucination rate >20%

---

## Critical Requirements

### 🚨 Native Polish Speaker

**MANDATORY** for Day 10 quality validation:
- Must have R&D tax relief knowledge (consultant/tax expert preferred)
- Sourcing options:
  - Freelancer platforms (Upwork, Fiverr): €200-400
  - Tax consulting firm partnership
  - University contact (linguistics/tax law)

**Without native speaker**: POC cannot validate quality threshold

---

## Budget

- **AI Costs**: €50-70 (30 documents, 2 models)
- **Native Speaker**: €200-400 (1 day review)
- **Total POC**: €250-470

---

## Expected Deliverables

1. **POC Report** (`reports/ai-poc-report.md`)
   - GO/NO-GO decision with rationale
   - Quality scores for all 30 outputs
   - Cost and speed analysis
   - Native speaker feedback
   - Model comparison (Claude vs GPT-4)

2. **Optimized Prompts** (`ai-generation/prompts/`)
   - Stage 1-3 prompt files
   - Few-shot examples
   - Grounding instructions

3. **Test Results** (`ai-generation/results/`)
   - 30 generated Word documents
   - Quality metrics CSV
   - Cost breakdown

4. **Implementation Code** (`ai-generation/src/`)
   - Generation scripts
   - Validation tools
   - Fact-checking engine

---

## References

- **Full POC Plan**: `/docs/ai-poc-plan.md`
- **PRD**: `/docs/prd.md`
- **Example Project Cards**: `/docs/project-cards/examples/` (66 files)
- **Template**: `/docs/project-cards/input/2025_09_10_Szablon karty projektu - do uzupełnienia.docx`

---

## Status

**Current Phase:** ✅ Test Cases Ready
**Next Action:** Set up POC environment (Day 1)
**Blocking:** Secure native Polish speaker

---

**Document Control:**
- **Created:** 2025-10-30
- **Author:** BMad Master
- **Version:** 1.0
