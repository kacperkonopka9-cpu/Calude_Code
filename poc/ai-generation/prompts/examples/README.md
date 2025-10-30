# Few-Shot Examples Directory

**Status:** Examples need to be extracted manually (Day 4 task)

---

## Required Actions

### Extract 3-5 Example Cards from Repository

**Source:** `/workspaces/Calude_Code/docs/project-cards/examples/` (66 .docx files)

**Recommended examples:**

1. **example1-erp-system.txt**
   - Source: `11. Karta projektu_BR ERP.docx`
   - Domain: IT/Software (ERP system)
   - Use for: IT projects (TC-001, TC-002, TC-003)

2. **example2-logistics-genetix.txt**
   - Source: `10. Karta projektu_BR logistyka Genetix.docx`
   - Domain: IT/Logistics (pharmaceutical logistics)
   - Use for: IT projects with compliance (TC-014)

3. **example3-hautau-windows.txt**
   - Source: `10. Karta projektu_BR HAUTAU.docx`
   - Domain: Manufacturing (window production)
   - Use for: Manufacturing projects (TC-004, TC-006, TC-013)

4. **example4-fuel-system.txt** (optional)
   - Source: `12. Karta projektu_BR System do paliw.docx`
   - Domain: Energy/Industrial
   - Use for: Energy projects (TC-008, TC-009, TC-010)

5. **example5-nfc-doors.txt** (optional)
   - Source: `18. Karta projektu_BR drzwi NT773619.docx`
   - Domain: Manufacturing/IoT
   - Use for: Advanced manufacturing (TC-006, TC-007)

---

## Extraction Method

### Manual Method (Recommended)

1. Open Word file in Microsoft Word or LibreOffice
2. Select All (Ctrl+A)
3. Copy (Ctrl+C)
4. Create new text file: `example1-erp-system.txt`
5. Paste text
6. Save as UTF-8 encoding
7. Verify all 8 sections are present

### Automated Method (If python-docx works)

```python
from docx import Document

def extract_example(docx_path, output_txt):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text)

    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(full_text))

# Extract examples
extract_example(
    '/workspaces/Calude_Code/docs/project-cards/examples/11. Karta projektu_BR ERP.docx',
    'example1-erp-system.txt'
)
```

---

## Validation Checklist

After extracting, verify each example:

- [ ] All 8 sections present (Cel, Opis, Nowatorskość, Metodologia, Problemy, Rezultaty, Koszty, Harmonogram)
- [ ] Professional Polish language
- [ ] No placeholders or incomplete sections
- [ ] UTF-8 encoding (no garbled characters)
- [ ] File size ~8,000-12,000 tokens (~4-6 KB text)

---

## If Examples Missing

**Option A:** Run POC without examples (lower quality expected)
- Quality will be 5-10 points lower
- Still worth testing to establish baseline

**Option B:** Use example excerpts (partial cards)
- Extract only Sections 3, 5, 6 (most critical)
- Reduces token cost by 60%
- Moderate quality impact

**Option C:** Skip POC until examples ready
- Not recommended - POC can proceed without optimal examples

---

## Token Budget

Each full example: ~8,000-12,000 tokens
- 2 examples: ~18,000 tokens input (€0.054)
- 3 examples: ~27,000 tokens input (€0.081)

**Recommendation:** Use 2 examples per generation to balance cost vs. quality.

---

## Current Status

```bash
# Check if examples exist
ls -lh prompts/examples/*.txt

# Count examples
ls prompts/examples/*.txt 2>/dev/null | wc -l
```

**Expected:** 3-5 .txt files, each 4-6 KB

---

## Next Steps

1. ✅ Extract 3 examples (1-2 hours)
2. ✅ Validate completeness
3. ✅ Test loading in generate.py
4. ✅ Proceed with POC Day 7 (testing)
