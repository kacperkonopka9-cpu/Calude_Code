# Extract Few-Shot Examples - Step-by-Step Guide

**Time Required:** 1-2 hours
**Required:** Microsoft Word or LibreOffice Writer
**Output:** 3 .txt files with Polish project card examples

---

## Quick Reference

**Source Files:**
1. `/workspaces/Calude_Code/docs/project-cards/examples/11. Karta projektu_BR ERP.docx`
2. `/workspaces/Calude_Code/docs/project-cards/examples/10. Karta projektu_BR logistyka Genetix.docx`
3. `/workspaces/Calude_Code/docs/project-cards/examples/10. Karta projektu_BR HAUTAU.docx`

**Destination:**
- `/workspaces/Calude_Code/poc/ai-generation/prompts/examples/`

---

## Step-by-Step Instructions

### Example 1: ERP System (IT Domain)

**Source:** `11. Karta projektu_BR ERP.docx`

1. **Open the file** in Microsoft Word or LibreOffice
2. **Select all text** (Ctrl+A or Cmd+A)
3. **Copy** (Ctrl+C or Cmd+C)
4. **Create new text file:**
   ```bash
   cd /workspaces/Calude_Code/poc/ai-generation/prompts/examples
   touch example1-erp-system.txt
   ```
5. **Open in text editor** (VS Code, nano, vim, etc.)
6. **Paste** the copied text (Ctrl+V or Cmd+V)
7. **Clean up formatting:**
   - Remove page numbers
   - Remove headers/footers
   - Keep all section headers (## 1. CEL PROJEKTU, etc.)
   - Preserve Polish characters (ą, ć, ę, ł, ń, ó, ś, ź, ż)
8. **Save as UTF-8 encoding**
9. **Verify:** Check file is 4-6 KB and contains all 8 sections

---

### Example 2: Logistics Genetix (IT/Pharma Domain)

**Source:** `10. Karta projektu_BR logistyka Genetix.docx`

Follow same steps as Example 1:
1. Open file
2. Select all (Ctrl+A)
3. Copy (Ctrl+C)
4. Create file: `example2-logistics-genetix.txt`
5. Paste and clean up
6. Save as UTF-8
7. Verify 4-6 KB, 8 sections

---

### Example 3: HAUTAU Windows (Manufacturing Domain)

**Source:** `10. Karta projektu_BR HAUTAU.docx`

Follow same steps:
1. Open file
2. Select all (Ctrl+A)
3. Copy (Ctrl+C)
4. Create file: `example3-hautau-windows.txt`
5. Paste and clean up
6. Save as UTF-8
7. Verify 4-6 KB, 8 sections

---

## Verification Checklist

After extracting all 3 examples, verify:

```bash
cd /workspaces/Calude_Code/poc/ai-generation/prompts/examples

# Check files exist
ls -lh *.txt
# Expected: 3 files, each 4-6 KB

# Check file encoding (should be UTF-8)
file -i example1-erp-system.txt
# Expected: charset=utf-8

# Check for 8 sections in each file
grep -c "^## [0-9]" example1-erp-system.txt
# Expected: 8 (or close to it)

# Check for Polish characters
grep -o "[ąćęłńóśźż]" example1-erp-system.txt | head -5
# Expected: Polish characters displayed correctly
```

**Expected Structure in Each File:**

```
# KARTA PROJEKTU B+R: [Project Name]

**Okres realizacji:** [dates]
**Osoba odpowiedzialna:** [name]

---

## 1. CEL PROJEKTU
[Content...]

## 2. OPIS PROJEKTU
[Content...]

## 3. NOWATORSKOŚĆ I INNOWACYJNOŚĆ
[Content...]

## 4. METODOLOGIA PRAC B+R
[Content...]

## 5. PROBLEMY BADAWCZE
[Content...]

## 6. REZULTATY PROJEKTU
[Content...]

## 7. KOSZTY KWALIFIKOWANE
[Content...]

## 8. HARMONOGRAM
[Content...]

**Podsumowanie:** [Summary...]
```

---

## Alternative: Automated Extraction (If Available)

If you have `python-docx` working:

```python
from docx import Document
from pathlib import Path

def extract_example(docx_path, output_txt):
    doc = Document(docx_path)
    full_text = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            # Preserve formatting markers
            if para.style.name.startswith('Heading'):
                full_text.append(f"\n## {text}\n")
            else:
                full_text.append(text)

    output = '\n\n'.join(full_text)

    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"✅ Extracted: {output_txt} ({len(output)} chars)")

# Extract all 3 examples
examples = [
    ('11. Karta projektu_BR ERP.docx', 'example1-erp-system.txt'),
    ('10. Karta projektu_BR logistyka Genetix.docx', 'example2-logistics-genetix.txt'),
    ('10. Karta projektu_BR HAUTAU.docx', 'example3-hautau-windows.txt'),
]

base_path = Path('/workspaces/Calude_Code/docs/project-cards/examples')
output_path = Path('/workspaces/Calude_Code/poc/ai-generation/prompts/examples')

for docx_file, txt_file in examples:
    try:
        extract_example(base_path / docx_file, output_path / txt_file)
    except Exception as e:
        print(f"❌ Failed to extract {docx_file}: {e}")
```

Save as `extract.py` and run:
```bash
cd /workspaces/Calude_Code/poc/ai-generation
python extract.py
```

---

## Troubleshooting

### Issue: Polish Characters Look Wrong (Garbled)

**Problem:** Characters like ą, ę, ł appear as � or strange symbols

**Fix:**
1. Ensure you save file with UTF-8 encoding
2. In VS Code: Bottom right corner → Select encoding → UTF-8
3. In nano: Use `nano -E` flag
4. In vim: `:set encoding=utf-8`

### Issue: File Too Small (<2 KB)

**Problem:** Not all content copied

**Fix:**
1. Make sure you selected ALL text (Ctrl+A)
2. Check if Word file has multiple sections/pages
3. Scroll through entire document before copying

### Issue: File Too Large (>20 KB)

**Problem:** Includes headers, footers, or extra formatting

**Fix:**
1. Remove page numbers, headers, footers
2. Remove any images or diagrams (descriptions only)
3. Keep only the main text content

---

## Testing Extracted Examples

After extraction, test that they work:

```bash
cd /workspaces/Calude_Code/poc/ai-generation

# Test loading examples
python -c "
from pathlib import Path

examples_dir = Path('prompts/examples')
for txt_file in examples_dir.glob('*.txt'):
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f'{txt_file.name}: {len(content)} chars')
"
```

**Expected Output:**
```
example1-erp-system.txt: 4500-6000 chars
example2-logistics-genetix.txt: 4500-6000 chars
example3-hautau-windows.txt: 4500-6000 chars
```

---

## Time Estimates

- **Manual extraction:** 30-40 minutes per example = 90-120 minutes total
- **Automated extraction:** 5 minutes (if python-docx works)
- **Verification:** 10-15 minutes

**Total:** 1.5-2 hours (manual) or 15-20 minutes (automated)

---

## Once Complete

✅ Mark as done: Update `/POC-STATUS.md`
✅ Test loading: `python src/generate.py --test-ids TC-001`
✅ Verify quality: Check if examples appear in Stage 2 prompts
✅ Proceed to: Native speaker recruitment

---

**Status:** ⏳ In Progress
**Blocking:** POC Day 7 testing
**Priority:** 🚨 HIGH
