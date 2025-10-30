#!/bin/bash
# ============================================
# HTML Generation Script for Inov Report
# Converts markdown files to branded HTML
# ============================================

# Color codes for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
OUTPUT_DIR="../output/html"
CSS_FILE="../report-styles.css"
PANDOC_OPTIONS="--standalone --toc --toc-depth=3 --css=report-styles.css"
MARKDOWN_DIR=".."

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo -e "${RED}ERROR: pandoc is not installed${NC}"
    echo "Install with:"
    echo "  Ubuntu/Debian: sudo apt-get install pandoc"
    echo "  macOS: brew install pandoc"
    echo "  Windows: choco install pandoc"
    exit 1
fi

# Create output directory
echo -e "${BLUE}Creating output directory...${NC}"
mkdir -p "$OUTPUT_DIR"

# Copy CSS to output directory
echo -e "${BLUE}Copying CSS stylesheet...${NC}"
cp "$CSS_FILE" "$OUTPUT_DIR/"

# Copy images to output directory
echo -e "${BLUE}Copying images...${NC}"
mkdir -p "$OUTPUT_DIR/images"
cp $MARKDOWN_DIR/../*.png "$OUTPUT_DIR/images/" 2>/dev/null || echo "No PNG images found"

# List of markdown files to convert (in order)
FILES=(
    "00-cover.md"
    "00-press-summary.md"
    "01-executive-summary-PL.md"
    "02-executive-summary-EN.md"
    "03-chapter-1-introduction.md"
    "04-chapter-2-methodology.md"
    "05-chapter-3-ecosystem-analysis.md"
    "06-chapter-4-statistical-gap.md"
    "07-chapter-5-international-comparisons.md"
    "08-chapter-6-solutions-analysis.md"
    "09-chapter-7-implications-recommendations.md"
    "10-chapter-8-conclusions.md"
    "11-appendices.md"
)

# Counter for statistics
TOTAL=0
SUCCESS=0
FAILED=0

echo -e "${BLUE}Starting HTML generation...${NC}"
echo "========================================"

# Convert each markdown file
for file in "${FILES[@]}"; do
    FULL_PATH="$MARKDOWN_DIR/$file"
    if [ -f "$FULL_PATH" ]; then
        TOTAL=$((TOTAL + 1))
        OUTPUT_FILE="${OUTPUT_DIR}/${file%.md}.html"

        echo -e "${YELLOW}Converting: $file${NC}"

        # Run pandoc conversion
        if pandoc "$FULL_PATH" \
            -f markdown \
            -t html5 \
            $PANDOC_OPTIONS \
            -o "$OUTPUT_FILE" 2>/dev/null; then

            SUCCESS=$((SUCCESS + 1))
            echo -e "${GREEN}✓ Success: $OUTPUT_FILE${NC}"
        else
            FAILED=$((FAILED + 1))
            echo -e "${RED}✗ Failed: $file${NC}"
        fi
    else
        echo -e "${YELLOW}⚠ Skipping (not found): $file${NC}"
    fi
done

echo "========================================"
echo -e "${BLUE}Conversion Summary:${NC}"
echo "  Total files: $TOTAL"
echo -e "  ${GREEN}Successful: $SUCCESS${NC}"
echo -e "  ${RED}Failed: $FAILED${NC}"

# Fix image paths in HTML files (adjust for images subdirectory)
echo -e "${BLUE}Fixing image paths...${NC}"
for html_file in "$OUTPUT_DIR"/*.html; do
    if [ -f "$html_file" ]; then
        # Replace ../ with images/ for local images
        sed -i 's|src="../\([^"]*\.png\)"|src="images/\1"|g' "$html_file" 2>/dev/null || \
        sed -i '' 's|src="../\([^"]*\.png\)"|src="images/\1"|g' "$html_file" 2>/dev/null
    fi
done

echo -e "${GREEN}✓ Image paths updated${NC}"

# Create index.html
echo -e "${BLUE}Creating index page...${NC}"
cat > "$OUTPUT_DIR/index.html" << 'EOF'
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analiza Ulg Proinnowacyjnych w Polsce: Luka raportowa - Inov R&D</title>
    <link rel="stylesheet" href="report-styles.css">
    <style>
        .index-container {
            max-width: 900px;
            margin: 40px auto;
            padding: 40px;
        }
        .chapter-list {
            list-style: none;
            margin: 0;
            padding: 0;
        }
        .chapter-list li {
            margin: 16px 0;
        }
        .chapter-list a {
            display: block;
            padding: 16px 24px;
            background: linear-gradient(135deg, #ECC246 0%, #F4C24A 100%);
            color: #2C3E50;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s ease;
        }
        .chapter-list a:hover {
            transform: translateX(8px);
            box-shadow: 0 4px 12px rgba(236, 194, 70, 0.4);
        }
        .section-title {
            color: #2C3E50;
            border-left: 4px solid #ECC246;
            padding-left: 16px;
            margin: 32px 0 16px 0;
        }
    </style>
</head>
<body>
    <div class="index-container">
        <div style="text-align: center; margin-bottom: 40px;">
            <img src="images/Inov logo (1800 x 1000 px) (10).png" alt="Inov R&D" style="max-width: 300px;">
        </div>

        <h1>Analiza Ulg Proinnowacyjnych w Polsce: Luka raportowa</h1>
        <p style="font-size: 18px; color: #5A5A5A; margin-bottom: 32px;">
            Raport kompleksowy Inov Research & Development
        </p>

        <h2 class="section-title">Materiały Wprowadzające</h2>
        <ul class="chapter-list">
            <li><a href="00-cover.html">📄 Strona Tytułowa</a></li>
            <li><a href="00-press-summary.html">📰 Streszczenie dla Mediów</a></li>
            <li><a href="01-executive-summary-PL.html">📊 Streszczenie Wykonawcze (PL)</a></li>
            <li><a href="02-executive-summary-EN.html">📊 Executive Summary (EN)</a></li>
        </ul>

        <h2 class="section-title">Część I: Kontekst i Diagnoza</h2>
        <ul class="chapter-list">
            <li><a href="03-chapter-1-introduction.html">Rozdział 1: Wprowadzenie i Kontekst</a></li>
            <li><a href="04-chapter-2-methodology.html">Rozdział 2: Metodologia</a></li>
            <li><a href="05-chapter-3-ecosystem-analysis.html">Rozdział 3: Ekosystem Ulg</a></li>
        </ul>

        <h2 class="section-title">Część II: Analiza Głównego Problemu</h2>
        <ul class="chapter-list">
            <li><a href="06-chapter-4-statistical-gap.html">Rozdział 4: Luka Statystyczna</a></li>
            <li><a href="07-chapter-5-international-comparisons.html">Rozdział 5: Porównania Międzynarodowe</a></li>
        </ul>

        <h2 class="section-title">Część III: Rozwiązania i Rekomendacje</h2>
        <ul class="chapter-list">
            <li><a href="08-chapter-6-solutions-analysis.html">Rozdział 6: Analiza Rozwiązań</a></li>
            <li><a href="09-chapter-7-implications-recommendations.html">Rozdział 7: Implikacje i Rekomendacje</a></li>
            <li><a href="10-chapter-8-conclusions.html">Rozdział 8: Wnioski</a></li>
        </ul>

        <h2 class="section-title">Dodatki</h2>
        <ul class="chapter-list">
            <li><a href="11-appendices.html">Dodatki A-D</a></li>
        </ul>

        <div style="margin-top: 60px; padding-top: 20px; border-top: 3px solid #ECC246; text-align: center; color: #5A5A5A;">
            <p><strong>Inov Research & Development</strong></p>
            <p>kkonopka@inovgroup.pl | www.inovgroup.pl</p>
            <p style="margin-top: 16px;">© 2025 Inov Research & Development</p>
        </div>
    </div>
</body>
</html>
EOF

echo -e "${GREEN}✓ Index page created${NC}"

# Final summary
echo ""
echo "========================================"
echo -e "${GREEN}HTML generation complete!${NC}"
echo "========================================"
echo ""
echo "Output location: ./$OUTPUT_DIR/"
echo "View report: open ./$OUTPUT_DIR/index.html"
echo ""
echo "Files generated:"
ls -1 "$OUTPUT_DIR"/*.html 2>/dev/null | sed 's/^/  - /'
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Open $OUTPUT_DIR/index.html in your browser"
echo "  2. Test all navigation links"
echo "  3. Verify images display correctly"
echo "  4. Check responsive design (resize browser)"
echo ""
