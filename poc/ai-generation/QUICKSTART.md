# POC Quick Start Guide
## 5-Minute Setup to Running POC

**Target:** Get from zero to generating AI project cards in 5 minutes.

---

## Prerequisites

- Python 3.11+ installed
- API keys for Claude (Anthropic) or GPT-4 (Azure OpenAI)
- 15 minutes of API runtime (~€6 budget)

---

## Step 1: Install Dependencies (1 minute)

```bash
# Navigate to POC directory
cd poc/ai-generation

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** If `language-tool-python` fails (requires Java), skip it for now:
```bash
pip install -r requirements.txt --ignore-installed language-tool-python
```

---

## Step 2: Configure API Keys (1 minute)

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use your preferred editor
```

**Minimum configuration (choose one):**

### Option A: Anthropic Claude (Recommended)
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
POC_MODELS=claude
```

### Option B: Azure OpenAI GPT-4
```bash
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4
POC_MODELS=gpt4
```

### Option C: Both (for comparison)
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
POC_MODELS=claude,gpt4
```

---

## Step 3: Prepare Examples (2 minutes)

**Option A: Extract Examples Yourself**

```bash
# Extract 2-3 example cards from Word files
# Example: Open docs/project-cards/examples/11. Karta projektu_BR ERP.docx
# Copy all text → Save as prompts/examples/example1-erp.txt
```

**Option B: Skip Examples (Lower Quality)**

If you don't have time, the POC will run without examples (quality will be lower):
```bash
# Create empty examples directory
mkdir -p prompts/examples
echo "PRZYKŁAD 1: Brak przykładu" > prompts/examples/placeholder.txt
```

**Option C: Use Minimal Example (Coming Soon)**

We'll add pre-extracted examples in the next commit.

---

## Step 4: Run POC (1 minute setup, 15 min runtime)

### Test Single Case (Fast Test)

```bash
# Test with just TC-001 (ERP System)
python src/generate.py --test-ids TC-001 --models claude
```

Expected output:
```
📋 Loaded 1 test case
🤖 MODEL: CLAUDE
TC-001: System ERP zintegrowany z produkcją i logistyką
  Stage 1: Analysis...
  Stage 2: Generation...
  Stage 3: Review...
  Quality Score: 78/100
  Cost: €0.182 ($0.195)
  Duration: 89.3s
✅ Saved: results/claude/TC-001.md
```

### Run Full POC (All 15 Test Cases)

```bash
# Run all test cases with Claude
python src/generate.py --models claude

# Or run with both models
python src/generate.py --models claude,gpt4
```

**Runtime:**
- Claude only: ~20 minutes (15 cases × 90s avg)
- Both models: ~40 minutes (30 total generations)

**Cost:**
- Claude: ~€2.70 (15 × €0.18)
- GPT-4: ~€3.30 (15 × €0.22)
- **Total: ~€6.00**

---

## Step 5: Review Results (ongoing)

### Check Output Files

```bash
# View generated cards
ls results/claude/
ls results/gpt4/

# Read a generated card
cat results/claude/TC-001.md

# Check metadata
cat results/metadata/TC-001-claude.json
```

### View Summary Stats

After POC completes, you'll see:

```
SUMMARY
========================================================

CLAUDE:
  Successful: 15/15
  Avg Quality Score: 76.3/100
  Total Cost: €2.73
  Avg Duration: 87.2s
  Pass Rate (≥70): 12/15 (80%)

GPT4:
  Successful: 15/15
  Avg Quality Score: 74.8/100
  Total Cost: €3.28
  Avg Duration: 65.4s
  Pass Rate (≥70): 11/15 (73%)
```

---

## Troubleshooting

### Issue: API Key Not Working

**Error:** `Anthropic API key not configured` or `401 Unauthorized`

**Fix:**
1. Check `.env` file has correct key format
2. Verify key is valid (test at https://console.anthropic.com/)
3. Ensure no extra spaces or quotes in `.env`

### Issue: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'anthropic'`

**Fix:**
```bash
# Ensure you're in virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Out of Memory

**Error:** `MemoryError` or system hangs

**Fix:**
```bash
# Reduce concurrent processing (edit .env)
MODEL_MAX_TOKENS=6000  # Reduce from 8000

# Or run fewer test cases at a time
python src/generate.py --test-ids TC-001,TC-002,TC-003
```

### Issue: Rate Limiting

**Error:** `Rate limit exceeded` or `429 Too Many Requests`

**Fix:**
```bash
# Increase retry delay (edit .env)
RETRY_DELAY_SECONDS=30  # Increase from 5
MAX_RETRIES=5  # Increase from 3
```

---

## Advanced Options

### Run Specific Test Cases

```bash
# Run only IT projects
python src/generate.py --filter industry=IT

# Run only simple complexity
python src/generate.py --filter complexity=Simple

# Run specific IDs
python src/generate.py --test-ids TC-001,TC-007,TC-013
```

### Adjust Generation Parameters

Edit `.env`:

```bash
# More creative (less deterministic)
MODEL_TEMPERATURE=0.7

# More conservative (more deterministic)
MODEL_TEMPERATURE=0.1

# Increase output length
MODEL_MAX_TOKENS=10000

# Use fewer examples (faster, cheaper)
FEW_SHOT_COUNT=1
```

### Enable Validation

```bash
# Enable grammar checking (requires LanguageTool)
ENABLE_GRAMMAR_CHECK=true

# Enable fact checking
ENABLE_FACT_CHECK=true

# Enable compliance validation
ENABLE_COMPLIANCE_CHECK=true
```

---

## Next Steps After POC

### If Quality ≥70 on 12/15 Cases → GO Decision

1. **Native Speaker Review** (Day 10)
   - Recruit Polish speaker
   - Review all 30 generated cards
   - Validate grammar and tone
   - Confirm quality scores

2. **Finalize POC Report**
   - Document findings
   - Include cost analysis
   - Provide GO/NO-GO recommendation

3. **Proceed to Epic 2** (Full Implementation)
   - Integrate prompts into production
   - Build Word export functionality
   - Add batch processing
   - Implement UI review interface

### If Quality 50-69 → PIVOT Decision

1. **Analyze Failure Patterns**
   - Which test cases struggled?
   - Which sections scored low?
   - Common errors?

2. **Refine Prompts** (iterate)
   - Add more explicit instructions
   - Improve few-shot examples
   - Strengthen grounding rules

3. **Re-test** with 5 failing cases

### If Quality <50 → NO-GO Decision

1. **Reassess Product Viability**
   - Can we accept lower quality threshold (60%)?
   - Should we pivot to template-based approach?
   - Is there alternative market segment?

2. **Escalate to Product Owner**

---

## Files Generated

```
results/
├── claude/
│   ├── TC-001.md          # Final project card
│   ├── TC-002.md
│   └── ... (15 files)
├── gpt4/
│   ├── TC-001.md
│   └── ... (15 files)
└── metadata/
    ├── TC-001-claude.json  # Quality scores, costs, tokens
    ├── TC-001-gpt4.json
    └── ... (30 files)
```

---

## Cost Breakdown

### Per Document

| Model | Input Tokens | Output Tokens | Cost |
|-------|--------------|---------------|------|
| Claude | ~25,000 | ~5,000 | €0.18 |
| GPT-4 | ~25,000 | ~5,000 | €0.22 |

### Full POC

| Scenario | Test Cases | Cost |
|----------|------------|------|
| Claude only | 15 | €2.70 |
| GPT-4 only | 15 | €3.30 |
| Both models | 30 | €6.00 |

**Well under €50 POC budget ✅**

---

## Support

**Questions?**
- Check `/docs/ai-poc-plan.md` for detailed plan
- Review `/poc/README.md` for POC overview
- See `/poc/ai-generation/prompts/README.md` for prompt details

**Issues?**
- Document in `poc/ai-generation/issues.md`
- Check GitHub issues (if applicable)

---

## Success Criteria Reminder

**GO Decision requires:**
- ✅ Quality ≥70 on 12/15 test cases (80%)
- ✅ Cost ≤€2.00 per document
- ✅ Generation time ≤15 min per document
- ✅ Polish grammar <2 errors/1000 words (native speaker)
- ✅ All 3 Ulga B+R criteria present
- ✅ Zero critical hallucinations

**Your POC results will show if we meet these thresholds.**

---

**Ready? Let's go! 🚀**

```bash
python src/generate.py
```
