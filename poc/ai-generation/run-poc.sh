#!/bin/bash
#
# POC Execution Script
# Runs full AI generation POC with comprehensive logging
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

LOG_FILE="poc-execution-$(date +%Y%m%d-%H%M%S).log"
RESULTS_DIR="results"

# Functions
log() {
    echo -e "${BLUE}[$(date +%H:%M:%S)]${NC} $1" | tee -a "$LOG_FILE"
}

log_success() {
    echo -e "${GREEN}[$(date +%H:%M:%S)] ✅ $1${NC}" | tee -a "$LOG_FILE"
}

log_warning() {
    echo -e "${YELLOW}[$(date +%H:%M:%S)] ⚠️  $1${NC}" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[$(date +%H:%M:%S)] ❌ $1${NC}" | tee -a "$LOG_FILE"
}

# Header
echo ""
echo "=========================================================="
echo "   AI GENERATION POC - R&D Tax Relief Project Cards"
echo "=========================================================="
echo ""
echo "Execution Log: $LOG_FILE"
echo ""

# Pre-flight checks
log "Running pre-flight checks..."

# Check Python
if ! command -v python3 &> /dev/null; then
    log_error "Python 3 not found. Please install Python 3.11+"
    exit 1
fi
log_success "Python 3: $(python3 --version)"

# Check virtual environment
if [ -d "venv" ]; then
    log_success "Virtual environment found"
    source venv/bin/activate || source venv/Scripts/activate
else
    log_warning "No virtual environment found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate || source venv/Scripts/activate
    log_success "Virtual environment created and activated"
fi

# Check dependencies
log "Checking dependencies..."
if ! python3 -c "import anthropic" &> /dev/null; then
    log_warning "Dependencies not installed. Installing now..."
    pip install -r requirements.txt >> "$LOG_FILE" 2>&1
    log_success "Dependencies installed"
else
    log_success "Dependencies OK"
fi

# Check .env file
if [ ! -f ".env" ]; then
    log_error ".env file not found. Please create it from .env.example and add API keys."
    exit 1
fi
log_success ".env file found"

# Check API keys
if ! grep -q "ANTHROPIC_API_KEY=sk-ant-" .env && ! grep -q "AZURE_OPENAI_API_KEY=" .env; then
    log_error "No API keys configured in .env. Please add Anthropic or Azure OpenAI credentials."
    exit 1
fi
log_success "API credentials configured"

# Check test cases
if [ ! -f "test-cases.csv" ]; then
    log_error "test-cases.csv not found. Please ensure test data is present."
    exit 1
fi
log_success "Test cases file found"

# Check examples
EXAMPLE_COUNT=$(ls prompts/examples/*.txt 2>/dev/null | wc -l)
if [ "$EXAMPLE_COUNT" -lt 2 ]; then
    log_warning "Only $EXAMPLE_COUNT example(s) found. Recommend 2-3 for optimal quality."
    log_warning "Continue anyway? (y/n)"
    read -r CONTINUE
    if [ "$CONTINUE" != "y" ]; then
        log "Execution cancelled. Please extract examples first."
        exit 0
    fi
else
    log_success "$EXAMPLE_COUNT examples found"
fi

# All checks passed
log_success "All pre-flight checks passed!"
echo ""

# Ask user what to run
echo "Select execution mode:"
echo "  1) Quick test (TC-001 only, ~2 min, €0.18)"
echo "  2) Claude full run (15 cases, ~20 min, €2.70)"
echo "  3) GPT-4 full run (15 cases, ~15 min, €3.30)"
echo "  4) Both models (30 cases, ~40 min, €6.00)"
echo ""
read -p "Enter choice [1-4]: " CHOICE

case $CHOICE in
    1)
        log "Running quick test with TC-001..."
        COMMAND="python src/generate.py --test-ids TC-001 --models claude"
        ;;
    2)
        log "Running full Claude test suite (15 cases)..."
        COMMAND="python src/generate.py --models claude"
        ;;
    3)
        log "Running full GPT-4 test suite (15 cases)..."
        COMMAND="python src/generate.py --models gpt4"
        ;;
    4)
        log "Running both models (30 cases total)..."
        log_warning "This will take ~40 minutes and cost ~€6.00"
        read -p "Continue? (y/n): " CONFIRM
        if [ "$CONFIRM" != "y" ]; then
            log "Execution cancelled."
            exit 0
        fi
        COMMAND="python src/generate.py --models claude,gpt4"
        ;;
    *)
        log_error "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
log "Starting execution at $(date)"
log "Command: $COMMAND"
echo ""

# Run the command
START_TIME=$(date +%s)

$COMMAND 2>&1 | tee -a "$LOG_FILE"

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
DURATION_MIN=$((DURATION / 60))
DURATION_SEC=$((DURATION % 60))

echo ""
log_success "Execution complete!"
log "Duration: ${DURATION_MIN}m ${DURATION_SEC}s"
echo ""

# Summary
log "Generating summary..."

# Count results
CLAUDE_COUNT=$(ls "$RESULTS_DIR/claude/"*.md 2>/dev/null | wc -l)
GPT4_COUNT=$(ls "$RESULTS_DIR/gpt4/"*.md 2>/dev/null | wc -l)
TOTAL_COUNT=$((CLAUDE_COUNT + GPT4_COUNT))

echo ""
echo "=========================================================="
echo "                      SUMMARY"
echo "=========================================================="
echo ""
echo "Documents Generated: $TOTAL_COUNT"
echo "  - Claude: $CLAUDE_COUNT"
echo "  - GPT-4: $GPT4_COUNT"
echo ""

# Calculate costs (if metadata exists)
if [ -d "$RESULTS_DIR/metadata" ] && [ "$(ls -A $RESULTS_DIR/metadata/*.json 2>/dev/null)" ]; then
    TOTAL_COST=$(python3 -c "
import json, glob
total = 0
for f in glob.glob('$RESULTS_DIR/metadata/*.json'):
    with open(f) as fp:
        total += json.load(fp).get('cost_eur', 0)
print(f'{total:.2f}')
" 2>/dev/null || echo "0.00")

    echo "Total Cost: €$TOTAL_COST"
    echo ""
fi

# Quality score summary (if available)
if [ -d "$RESULTS_DIR/metadata" ] && [ "$(ls -A $RESULTS_DIR/metadata/*.json 2>/dev/null)" ]; then
    python3 << 'EOF'
import json, glob

scores = []
for f in glob.glob('results/metadata/*.json'):
    with open(f) as fp:
        data = json.load(fp)
        if data.get('quality_score', 0) > 0:
            scores.append(data['quality_score'])

if scores:
    avg_score = sum(scores) / len(scores)
    pass_count = sum(1 for s in scores if s >= 70)
    pass_rate = (pass_count / len(scores)) * 100

    print(f"Quality Scores:")
    print(f"  Average: {avg_score:.1f}/100")
    print(f"  Pass Rate (≥70): {pass_count}/{len(scores)} ({pass_rate:.0f}%)")
    print(f"  Min: {min(scores)}, Max: {max(scores)}")
    print()

    # Success criteria
    if pass_count >= 12:
        print("✅ SUCCESS: Quality criterion met (≥12/15 pass)")
    elif pass_count >= 8:
        print("⚠️  PIVOT: Quality borderline (8-11/15 pass)")
    else:
        print("❌ FAIL: Quality below threshold (<8/15 pass)")
EOF
fi

echo ""
echo "Results saved to: $RESULTS_DIR/"
echo "Execution log: $LOG_FILE"
echo ""

# Next steps
log "Next steps:"
echo "  1. Review generated cards in $RESULTS_DIR/"
echo "  2. Check quality scores in $RESULTS_DIR/metadata/"
echo "  3. Send cards to native Polish speaker for validation"
echo "  4. See /poc/EXECUTION-CHECKLIST.md for Day 8-10 tasks"
echo ""

log_success "POC execution script complete!"
