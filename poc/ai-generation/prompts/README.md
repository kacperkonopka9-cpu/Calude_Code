# AI Generation Prompts
## R&D Tax Relief Project Card Generator - POC

**Version:** 1.0 (Draft)
**Date:** 2025-10-30
**Status:** Ready for POC Testing

---

## Overview

This directory contains production-ready prompts for the AI-powered generation of Polish R&D tax relief (Ulga B+R) project cards using a **multi-stage pipeline**:

1. **Stage 1:** Project Analysis & R&D Identification
2. **Stage 2:** Section-by-Section Generation (8 sections)
3. **Stage 3:** Coherence Review & Compliance Validation

---

## Files in This Directory

### Core Prompt Files

| File | Purpose | Token Count | Stage |
|------|---------|-------------|-------|
| `stage1-analysis.txt` | R&D aspect identification and Ulga B+R qualification | ~1,500 | Stage 1 |
| `stage2-generation.txt` | Main generation prompt for all 8 sections | ~3,000 | Stage 2 |
| `stage3-review.txt` | Quality assurance and compliance validation | ~3,500 | Stage 3 |

### Supporting Documents

| File | Purpose |
|------|---------|
| `grounding-instructions.md` | Anti-hallucination guidelines (DO NOT / MAY INFER rules) |
| `few-shot-examples-guide.md` | Guide for selecting and using example project cards |
| `examples/` | Directory for extracted example cards (TBD - POC Day 4) |

---

## Multi-Stage Pipeline Architecture

```
INPUT DATA
(Excel row: project name, description, dates, goal, responsible person)
    ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1: Analysis & R&D Identification                     │
│ - Identify R&D aspects                                      │
│ - Check 3 Ulga B+R criteria (celowość, twórczość, wiedza) │
│ - List research challenges                                  │
│ - Assess data completeness                                  │
└─────────────────────────────────────────────────────────────┘
    ↓ (Analysis output becomes input to Stage 2)
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2: Section-by-Section Generation                     │
│ - Generate all 8 required sections                         │
│ - Use Stage 1 analysis + original data                     │
│ - Apply grounding rules (no invented facts)                │
│ - Flag uncertainties with [WYMAGA WERYFIKACJI]            │
│ - Target: 5,000-6,500 words (6-8 pages)                   │
└─────────────────────────────────────────────────────────────┘
    ↓ (Generated card becomes input to Stage 3)
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3: Review & Validation                               │
│ - Fact-check against original input                        │
│ - Validate all 3 Ulga B+R criteria present                │
│ - Check coherence and flow                                 │
│ - Review Polish grammar quality                            │
│ - Provide quality score (0-100)                            │
│ - Output final validated card                              │
└─────────────────────────────────────────────────────────────┘
    ↓
OUTPUT: Final Project Card (Word .docx)
```

---

## Prompt Design Principles

### 1. Strict Grounding (Anti-Hallucination)

**Problem:** AI models can invent facts not present in input data.

**Solution:**
- Explicit "DO NOT INVENT" lists in all prompts
- "MAY INFER" guidance for acceptable generalizations
- `[WYMAGA WERYFIKACJI]` flagging for insufficient data
- Stage 3 fact-checking validates against original input

**Reference:** `grounding-instructions.md`

---

### 2. Explicit Compliance Requirements

**Problem:** Ulga B+R requires ALL THREE criteria explicitly addressed.

**Solution:**
- Stage 1 checklist: celowość, element twórczy, nowa wiedza
- Stage 2 section requirements explicitly mention where criteria should appear
- Stage 3 validation fails if any criterion missing

**Criteria Locations:**
- **Celowość** → Section 1 (Cel projektu) or Section 3 (Nowatorskość)
- **Element twórczy** → Section 3 (Nowatorskość i innowacyjność)
- **Nowa wiedza** → Section 3 and Section 6 (Rezultaty projektu)

---

### 3. Professional Polish Language

**Problem:** AI-generated Polish can have grammar errors or unnatural phrasing.

**Solution:**
- Explicit tone guidance ("professional consulting tone")
- Examples of appropriate terminology
- Stage 3 grammar review
- Native speaker final validation (POC Day 10)

---

### 4. Few-Shot Learning

**Problem:** AI needs style and quality reference points.

**Solution:**
- Include 2-3 high-quality example cards in Stage 2 prompt
- Domain-matched examples when possible
- Examples demonstrate structure, depth, and compliance

**Reference:** `few-shot-examples-guide.md`

---

### 5. Structured Output Format

**Problem:** Consistent formatting required for Word export.

**Solution:**
- Exact output format specified in each stage
- Markdown-style headers for easy parsing
- Clear section delimiters
- Metadata block (project name, dates, responsible person)

---

## Token Budget Analysis

### Stage 1: Analysis (~3,000-4,000 tokens total)

| Component | Tokens |
|-----------|--------|
| Prompt instructions | ~1,500 |
| Input data | ~500-1,500 |
| Output (analysis) | ~800-1,000 |

**Cost:** ~$0.012 per generation (Claude 3.5 Sonnet)

---

### Stage 2: Generation (~27,000-32,000 tokens total)

| Component | Tokens |
|-----------|--------|
| Prompt instructions | ~3,000 |
| Input data | ~500-1,500 |
| Stage 1 analysis | ~800-1,000 |
| Few-shot examples (2) | ~16,000-20,000 |
| **Input subtotal** | ~20,000-25,000 |
| Output (generated card) | ~3,500-5,000 |

**Cost:** ~$0.11-0.13 per generation (Claude 3.5 Sonnet)

---

### Stage 3: Review (~9,000-11,000 tokens total)

| Component | Tokens |
|-----------|--------|
| Prompt instructions | ~3,500 |
| Input data (original) | ~500-1,500 |
| Generated card (Stage 2) | ~3,500-5,000 |
| **Input subtotal** | ~7,500-10,000 |
| Output (review + final card) | ~1,500-2,000 |

**Cost:** ~$0.04-0.05 per generation (Claude 3.5 Sonnet)

---

### **Total Per Document: ~€0.16-0.20**

✅ **Well under €2.00 target** (POC success criterion)

**POC Total Cost (15 docs × 2 models):**
- 30 generations × €0.18 avg = **€5.40**
- Add buffer (retries, experiments): **€8-12 total**
- ✅ **Within €50-70 POC budget**

---

## Usage Instructions

### For POC Execution (Days 7-8)

#### Day 7: Claude 3.5 Sonnet Testing

```python
# Pseudocode - actual implementation in src/generate.py

for test_case in test_cases:
    # Stage 1: Analysis
    stage1_prompt = load_prompt('stage1-analysis.txt')
    stage1_input = format_input(test_case)
    stage1_response = call_claude(stage1_prompt + stage1_input)

    # Stage 2: Generation
    stage2_prompt = load_prompt('stage2-generation.txt')
    few_shot_examples = load_examples(test_case.industry)  # 2 examples
    stage2_input = format_input(test_case) + stage1_response + few_shot_examples
    stage2_response = call_claude(stage2_prompt + stage2_input)

    # Stage 3: Review
    stage3_prompt = load_prompt('stage3-review.txt')
    stage3_input = format_input(test_case) + stage2_response
    stage3_response = call_claude(stage3_prompt + stage3_input)

    # Extract final card and quality score
    final_card = extract_final_card(stage3_response)
    quality_score = extract_quality_score(stage3_response)

    # Save outputs
    save_word_doc(final_card, f'results/claude/tc-{test_case.id}.docx')
    save_metadata(test_case.id, quality_score, token_counts, cost)
```

#### Day 8: GPT-4 Testing

Same process, replace `call_claude()` with `call_gpt4()`.

---

### For Production (Post-POC)

If POC succeeds, integrate optimized prompts into production codebase:

1. **Prompt Versioning:** Track prompt versions (v1.0, v1.1, etc.)
2. **A/B Testing:** Compare prompt variants for quality improvement
3. **Cost Optimization:** Consider excerpt-based examples (60-70% cost reduction)
4. **Caching:** Use prompt caching for repeated examples (if API supports)
5. **Monitoring:** Log quality scores, costs, and generation times

---

## Prompt Improvement Workflow

### After POC Day 10 (Based on Results)

If quality scores are suboptimal (60-75 range):

**Iteration Plan:**

1. **Analyze Failure Patterns:**
   - Which sections consistently score low?
   - Which test cases struggle (sparse input? specific domains?)
   - Common errors (hallucinations, missing criteria, grammar)

2. **Refine Prompts:**
   - Add more explicit instructions for weak sections
   - Strengthen grounding rules for hallucination-prone areas
   - Add domain-specific guidance (if certain industries struggle)
   - Improve few-shot example selection

3. **Test Refinements:**
   - Re-run 5 failing test cases with refined prompts
   - Measure improvement in quality scores
   - Iterate until ≥70 quality achieved

4. **Version Control:**
   - Save refined prompts as v1.1, v1.2, etc.
   - Document changes in `CHANGELOG.md`
   - Track which version used for each test

---

## Key Success Factors

### What Makes These Prompts Effective?

1. **Multi-Stage Pipeline:**
   - Separates analysis, generation, and review (reduces cognitive load per stage)
   - Stage 1 output guides Stage 2 (better R&D aspect identification)
   - Stage 3 validates and corrects (quality assurance built-in)

2. **Grounding Rules:**
   - Explicit lists of what NOT to invent
   - Guidance on acceptable inferences
   - Flagging mechanism for uncertain content

3. **Compliance Checklist:**
   - All three Ulga B+R criteria explicitly required
   - Specific sections identified for each criterion
   - Validation in Stage 3 catches omissions

4. **Few-Shot Learning:**
   - Real examples demonstrate quality and style
   - Domain-matched examples improve relevance
   - 2-3 examples balance quality vs. cost

5. **Quality Scoring:**
   - Stage 3 provides objective quality estimate (0-100)
   - Enables POC success measurement
   - Identifies improvement areas

---

## Limitations & Risks

### Known Limitations

**Input Data Dependency:**
- Quality ceiling depends on input richness
- Sparse input (TC-002, TC-009, TC-015) will score lower
- Cannot generate details not inferable from input

**Domain Knowledge:**
- AI may struggle with highly specialized domains
- Cutting-edge technology descriptions may be generic
- Regulatory/compliance terminology may be imprecise

**Polish Language:**
- Grammar accuracy depends on model training
- Native speaker review is essential (POC Day 10)
- Technical terminology may have translation issues

### Risk Mitigation

✓ **Grounding rules** prevent major hallucinations
✓ **[WYMAGA WERYFIKACJI] flagging** alerts to uncertain content
✓ **Stage 3 review** catches errors before output
✓ **Native speaker validation** catches language issues
✓ **Consultant review** remains final quality gate (human in the loop)

---

## Next Steps

### POC Day 4: Few-Shot Example Preparation

**Action Items:**
1. Review example project cards in `/docs/project-cards/examples/`
2. Select 3-5 high-quality examples across domains (IT, Manufacturing, Energy, Construction)
3. Extract to text files: `examples/example1-erp.txt`, etc.
4. Validate completeness (all 8 sections)
5. Measure token counts
6. Test loading into Stage 2 prompt

**Deliverable:** `examples/` directory with 3-5 .txt files

---

### POC Days 5-6: Prompt Refinement

**Action Items:**
1. Test Stage 1 prompt with 2-3 test cases manually
2. Review Stage 1 outputs for R&D identification quality
3. Test Stage 2 prompt with 1 test case manually (with examples)
4. Test Stage 3 prompt with Stage 2 output
5. Measure total token costs
6. Refine prompts based on initial tests
7. Version as v1.0 (production-ready)

**Deliverable:** Finalized prompt files v1.0

---

### POC Days 7-8: Automated Testing

**Action Items:**
1. Implement generation scripts (`src/generate.py`)
2. Run all 15 test cases through Claude 3.5 Sonnet
3. Run all 15 test cases through GPT-4
4. Collect quality scores, costs, and timing data
5. Generate Word documents for all 30 outputs

**Deliverable:** 30 generated project cards + metadata CSV

---

### POC Days 9-10: Validation & Decision

**Action Items:**
1. Automated validation (grammar, compliance, fact-checking)
2. Native speaker review (all 30 cards)
3. Calculate average quality scores
4. Analyze cost and speed metrics
5. Prepare POC report with GO/NO-GO recommendation

**Deliverable:** POC report with GO/NO-GO decision

---

## Support & Documentation

**Questions about prompts:**
- Review `grounding-instructions.md` for anti-hallucination rules
- Review `few-shot-examples-guide.md` for example selection

**Prompt issues or improvements:**
- Document in `/poc/ai-generation/prompt-issues.md` (create as needed)
- Track prompt version changes in `CHANGELOG.md`

**POC execution questions:**
- Refer to `/docs/ai-poc-plan.md` for full 10-day plan
- Check `/poc/README.md` for POC overview

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 (Draft) | 2025-10-30 | Initial prompt creation for POC | BMad Master |

---

**End of Prompts README**
