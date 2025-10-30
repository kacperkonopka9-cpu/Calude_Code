# Few-Shot Examples Guide
## Selecting and Using Example Project Cards

**Version:** 1.0
**Purpose:** Guidelines for selecting and incorporating example project cards into AI prompts

---

## Overview

Few-shot learning uses 2-3 high-quality example project cards to demonstrate the desired output format, style, and quality. Examples are included in Stage 2 prompts to guide AI generation.

---

## Selection Criteria

### How Many Examples?

**Recommended:** 2-3 examples per generation

**Why not more?**
- Token cost increases significantly (8,000-10,000 tokens per example)
- Diminishing returns after 3 examples
- Risk of overfitting to example style

**Why not fewer?**
- 1 example may not demonstrate variability
- AI may copy too literally from single example

### Which Examples to Select?

**Domain Similarity (Primary Factor):**

Match example domain to target project when possible:

| Target Project Domain | Recommended Example Domain |
|----------------------|----------------------------|
| IT/Software | IT system, ERP, logistics software |
| Manufacturing | Window/door production, welding, equipment |
| Construction | Facade system, building tech, materials |
| Energy/Industrial | Fuel systems, turbines, power equipment |

**Quality Characteristics (Secondary Factors):**

Select examples that demonstrate:
- ✅ All 8 sections present and substantive
- ✅ Professional Polish language
- ✅ Explicit reference to all 3 Ulga B+R criteria
- ✅ Technical depth without excessive jargon
- ✅ Clear structure and logical flow
- ✅ 5-7 pages in length (when formatted)

**Diversity (Tertiary Factor):**

If using 3 examples, vary:
- Project complexity (simple, medium, advanced)
- Industry (don't use 3 examples from same industry)
- Project duration (1-year, multi-year)

---

## Recommended Examples from Repository

Based on analysis of `/docs/project-cards/examples/` (66 files), these are high-quality candidates:

### Example Set A: IT/Software Projects

**Primary:** `11. Karta projektu_BR ERP.docx`
- Domain: IT system development (ERP)
- Complexity: Medium
- Quality: High (comprehensive, well-structured)
- Use for: IT, software, or logistics projects

**Secondary:** `10. Karta projektu_BR logistyka Genetix.docx`
- Domain: Logistics IT system (pharmaceutical)
- Complexity: Medium-Advanced
- Quality: High (regulatory compliance aspects)
- Use for: IT projects with compliance requirements

### Example Set B: Manufacturing Projects

**Primary:** `10. Karta projektu_BR HAUTAU.docx`
- Domain: Window production technology
- Complexity: Simple-Medium
- Quality: High (clear manufacturing process)
- Use for: Manufacturing, production line, equipment projects

**Secondary:** `11. Karta projektu_BR zgrzewanie ram z progiem aluminowym.docx`
- Domain: Welding technology (aluminum)
- Complexity: Medium
- Quality: High (materials science aspects)
- Use for: Manufacturing with materials R&D

### Example Set C: Energy/Industrial Projects

**Primary:** `12. Karta projektu_BR System do paliw.docx` or `16. Karta projektu_BR System do paliw.docx`
- Domain: Alternative fuel system
- Complexity: Medium
- Quality: High (energy and environmental aspects)
- Use for: Energy, environmental, industrial automation projects

**Secondary:** `13. Karta projektu_BR Mobilne wózki widłowe.docx` or `17. Karta projektu_BR Mobilne wózki widłowe.docx`
- Domain: Industrial equipment (autonomous forklifts)
- Complexity: Advanced
- Quality: High (AI/automation aspects)
- Use for: Automation, robotics, advanced equipment projects

### Example Set D: Construction Projects

**Primary:** `1. i 2. Karta projektu_BR Winkhaus Skyline.docx`
- Domain: Window system (construction)
- Complexity: Simple-Medium
- Quality: High
- Use for: Building systems, construction materials

**Secondary:** (Select from specialized construction examples as needed)

---

## How to Use Examples in Prompts

### Stage 2 Prompt Integration

**Location:** Insert examples AFTER the input data section, BEFORE the task description.

**Format:**

```
===== INPUT DATA =====

[Project data here]

===== EXAMPLE REFERENCE CARDS =====

You have access to 2-3 example project cards that demonstrate the expected quality,
structure, and style. Study these examples carefully:

**PRZYKŁAD 1: System ERP**
[Full text of example card 1 - ~8,000 tokens]

**PRZYKŁAD 2: System logistyczny Genetix**
[Full text of example card 2 - ~8,000 tokens]

**PRZYKŁAD 3: System drzwi NFC** (optional)
[Full text of example card 3 - ~8,000 tokens]

===== YOUR TASK =====

Generate a project card following the same structure, style, and quality level as
the examples above, but for the new project described in INPUT DATA.

CRITICAL: Use examples as STYLE GUIDE only - do NOT copy content. Generate original
content based on the new project's input data.

[Rest of Stage 2 prompt...]
```

### Token Budget Considerations

**Example Token Costs:**
- Short example (5 pages, ~2,500 words): ~8,000 tokens
- Medium example (7 pages, ~3,500 words): ~10,000 tokens
- Long example (10 pages, ~5,000 words): ~12,000 tokens

**Total Cost for 2 Examples:** ~16,000-20,000 tokens (input)

**With Input + Prompt + Examples:**
- Prompt instructions: ~3,000 tokens
- Input data: ~500-1,500 tokens
- 2 Examples: ~16,000-20,000 tokens
- **Total Stage 2 input:** ~20,000-25,000 tokens

**Output:**
- Generated card: ~3,500-5,000 tokens (target 6-8 pages)

**Per-Generation Cost (Claude 3.5 Sonnet):**
- Input: 24,000 tokens × $3/1M = $0.072
- Output: 4,000 tokens × $15/1M = $0.060
- **Total: ~$0.13 per generation**

**Within POC Budget:** ✅ 15 docs × $0.13 = $1.95 (well under €50 budget)

---

## Extracting Examples from Repository

### Manual Extraction (Recommended for POC)

1. **Open Word file** from `/docs/project-cards/examples/`
2. **Copy full text** (Ctrl+A, Ctrl+C)
3. **Paste into text file**: `example1-erp-system.txt`
4. **Clean formatting:**
   - Remove headers/footers
   - Keep section headers
   - Preserve Polish characters (UTF-8 encoding)
   - Remove page numbers
5. **Verify completeness:** All 8 sections present

### Automated Extraction (For Production)

Use `python-docx` to extract text:

```python
from docx import Document

def extract_example(docx_path, output_txt):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_text))

# Extract ERP example
extract_example(
    'docs/project-cards/examples/11. Karta projektu_BR ERP.docx',
    'poc/ai-generation/prompts/examples/example1-erp.txt'
)
```

---

## Example Selection Strategy Per Test Case

**TC-001 (ERP System - IT):**
- Use: ERP + Logistics examples
- Domain match: Perfect

**TC-002 (Task Management - IT):**
- Use: ERP + Task management (if available)
- Domain match: Good

**TC-003 (Mobile Construction App - IT):**
- Use: Logistics + ERP (mobile aspects)
- Domain match: Moderate (IT but different subdomain)

**TC-004 (HAUTAU Windows - Manufacturing):**
- Use: HAUTAU + Door NFC examples
- Domain match: Perfect

**TC-005 (Aluminum Welding - Manufacturing):**
- Use: Welding + HAUTAU examples
- Domain match: Perfect

**TC-006 (NFC Door - Manufacturing):**
- Use: Door NFC + HAUTAU examples
- Domain match: Perfect

**TC-007 (Autonomous Forklifts - Manufacturing):**
- Use: Forklifts + Logistics automation examples
- Domain match: Perfect

**TC-008 (Fuel System - Energy):**
- Use: Fuel system + (Energy example if available)
- Domain match: Perfect

**TC-009 (Turbine Upgrade - Energy):**
- Use: Fuel system + Industrial equipment
- Domain match: Moderate

**TC-010 (Energy Storage - Energy):**
- Use: Fuel system + Power/energy examples
- Domain match: Moderate (cutting-edge may lack exact match)

**TC-011 (Heritage Tynks - Construction):**
- Use: Construction materials + Winkhaus examples
- Domain match: Moderate

**TC-012 (High-Rise Facade - Construction):**
- Use: Winkhaus + Building system examples
- Domain match: Moderate

**TC-013 (Smart Windows - Construction):**
- Use: HAUTAU + Winkhaus (both window systems)
- Domain match: Excellent

**TC-014 (Pharma Logistics - Other):**
- Use: Genetix logistics + ERP
- Domain match: Perfect

**TC-015 (Wood Processing - Other):**
- Use: Manufacturing general examples
- Domain match: Generic

---

## POC Day 4 Task: Example Selection

**Action Items:**

1. **Review example files** in `/docs/project-cards/examples/`
2. **Select 3-5 high-quality examples** covering diverse domains:
   - 1-2 IT/Software
   - 1-2 Manufacturing
   - 1 Energy/Construction
3. **Extract to text files** (UTF-8 encoding)
4. **Validate completeness** (all 8 sections present)
5. **Measure token count** (use `tiktoken` or similar)
6. **Create example library**: `prompts/examples/example{1-5}.txt`

**Estimated Time:** 2-3 hours

---

## Quality Validation Checklist

Before using an example in prompts, verify:

- [ ] All 8 sections present and substantive
- [ ] Professional Polish language (no grammar errors)
- [ ] Explicit mention of celowość, element twórczy, nowa wiedza
- [ ] Technical depth appropriate to domain
- [ ] Clear structure with section headers
- [ ] 5-8 pages in length (2,500-4,000 words)
- [ ] Consistent terminology throughout
- [ ] No obvious errors or placeholder text
- [ ] Successfully extracted to text format (UTF-8)
- [ ] Token count measured (~8,000-12,000 tokens)

---

## Alternative: Use Example Excerpts

If full examples exceed token budget, consider using **section-level excerpts**:

**Approach:**
- Instead of full 8-section card, show 2-3 exemplary sections per example
- Select best-written sections (typically Section 3, 5, or 6)
- Reduces token cost by 60-70% while preserving style guidance

**Example:**

```
PRZYKŁAD 1 (Excerpt - Sections 3 & 5 only):

## 3. NOWATORSKOŚĆ I INNOWACYJNOŚĆ

[Show only Section 3 from Example 1]

## 5. PROBLEMY BADAWCZE

[Show only Section 5 from Example 1]

---

PRZYKŁAD 2 (Excerpt - Sections 3 & 6 only):

[Similar format]
```

**Trade-off:**
- ✅ Reduces cost (~3,000 tokens per example vs 10,000)
- ⚠️ Less comprehensive style guidance
- ⚠️ AI may need more explicit instructions for non-excerpted sections

**Recommendation:** Use full examples for POC (cost is acceptable). Consider excerpts for production cost optimization.

---

## Summary

**POC Recommendation:**
- Select **2 examples per test case** based on domain similarity
- Use **full example cards** (all 8 sections)
- Budget **20,000 tokens** for examples in Stage 2 input
- Total cost per generation: **~€0.13** (acceptable)

**Production Optimization:**
- Consider **section excerpts** to reduce cost by 60-70%
- Cache examples across multiple generations (if API supports prompt caching)
- Build domain-specific example libraries (3-5 examples per industry)

---

**End of Few-Shot Examples Guide**
