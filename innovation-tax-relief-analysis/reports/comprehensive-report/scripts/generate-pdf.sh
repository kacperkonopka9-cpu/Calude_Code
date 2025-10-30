#!/bin/bash
# ============================================
# PDF Generation Script for Inov Report
# Converts HTML files to PDF with branding
# ============================================

# Color codes for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
HTML_DIR="html-output"
PDF_DIR="pdf-output"

# Check if wkhtmltopdf is installed
if ! command -v wkhtmltopdf &> /dev/null; then
    echo -e "${RED}ERROR: wkhtmltopdf is not installed${NC}"
    exit 1
fi

# Create output directory
echo -e "${BLUE}Creating PDF output directory...${NC}"
mkdir -p "$PDF_DIR"

echo -e "${BLUE}Starting PDF generation...${NC}"
echo "========================================"

# Function to convert HTML to PDF
convert_to_pdf() {
    local html_file="$1"
    local pdf_file="$2"

    wkhtmltopdf \
        --enable-local-file-access \
        --encoding UTF-8 \
        --page-size A4 \
        --margin-top 20mm \
        --margin-bottom 20mm \
        --margin-left 15mm \
        --margin-right 15mm \
        --print-media-type \
        "$html_file" \
        "$pdf_file" 2>/dev/null

    return $?
}

# Generate individual PDFs
SUCCESS=0
FAILED=0

# Key documents to generate
FILES=(
    "00-cover:Cover_Page"
    "00-press-summary:Press_Summary"
    "01-executive-summary-PL:Executive_Summary_PL"
    "02-executive-summary-EN:Executive_Summary_EN"
    "03-chapter-1-introduction:Chapter_1_Introduction"
    "04-chapter-2-methodology:Chapter_2_Methodology"
    "05-chapter-3-ecosystem-analysis:Chapter_3_Ecosystem"
    "06-chapter-4-statistical-gap:Chapter_4_Statistical_Gap"
    "07-chapter-5-international-comparisons:Chapter_5_International_Comparisons"
    "08-chapter-6-solutions-analysis:Chapter_6_Solutions"
    "09-chapter-7-implications-recommendations:Chapter_7_Recommendations"
    "10-chapter-8-conclusions:Chapter_8_Conclusions"
    "11-appendices:Appendices"
)

for entry in "${FILES[@]}"; do
    IFS=':' read -r html_name pdf_name <<< "$entry"
    HTML_FILE="${HTML_DIR}/${html_name}.html"
    PDF_FILE="${PDF_DIR}/${pdf_name}.pdf"

    if [ -f "$HTML_FILE" ]; then
        echo -e "${YELLOW}Converting: ${html_name}.html${NC}"

        if convert_to_pdf "$HTML_FILE" "$PDF_FILE"; then
            SUCCESS=$((SUCCESS + 1))
            echo -e "${GREEN}✓ Success: ${pdf_name}.pdf${NC}"
        else
            FAILED=$((FAILED + 1))
            echo -e "${RED}✗ Failed: ${html_name}.html${NC}"
        fi
    fi
done

echo "========================================"
echo -e "${BLUE}PDF Conversion Summary:${NC}"
echo "  ${GREEN}Successful: $SUCCESS${NC}"
echo "  ${RED}Failed: $FAILED${NC}"
echo ""

# Generate combined full report
echo -e "${BLUE}Generating combined full report...${NC}"

COMBINED_HTML=(
    "${HTML_DIR}/00-cover.html"
    "${HTML_DIR}/01-executive-summary-PL.html"
    "${HTML_DIR}/02-executive-summary-EN.html"
    "${HTML_DIR}/03-chapter-1-introduction.html"
    "${HTML_DIR}/04-chapter-2-methodology.html"
    "${HTML_DIR}/05-chapter-3-ecosystem-analysis.html"
    "${HTML_DIR}/06-chapter-4-statistical-gap.html"
    "${HTML_DIR}/07-chapter-5-international-comparisons.html"
    "${HTML_DIR}/08-chapter-6-solutions-analysis.html"
    "${HTML_DIR}/09-chapter-7-implications-recommendations.html"
    "${HTML_DIR}/10-chapter-8-conclusions.html"
    "${HTML_DIR}/11-appendices.html"
)

echo -e "${YELLOW}Combining 12 chapters into single PDF...${NC}"
wkhtmltopdf \
    --enable-local-file-access \
    --encoding UTF-8 \
    --page-size A4 \
    --margin-top 20mm \
    --margin-bottom 20mm \
    --margin-left 15mm \
    --margin-right 15mm \
    --print-media-type \
    --footer-center "Strona [page] z [topage]" \
    --footer-font-size 9 \
    "${COMBINED_HTML[@]}" \
    "${PDF_DIR}/Inov_Report_Complete.pdf" 2>/dev/null

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Combined report generated: Inov_Report_Complete.pdf${NC}"
else
    echo -e "${RED}✗ Failed to generate combined report${NC}"
fi

echo ""
echo "========================================"
echo -e "${GREEN}PDF generation complete!${NC}"
echo "========================================"
echo ""
echo "Output location: ./$PDF_DIR/"
echo ""
echo "Files generated:"
ls -lh "$PDF_DIR"/*.pdf 2>/dev/null | awk '{print "  - " $9 " (" $5 ")"}'
echo ""
echo -e "${BLUE}Individual chapter PDFs ready for distribution!${NC}"
echo -e "${BLUE}Complete report: ${PDF_DIR}/Inov_Report_Complete.pdf${NC}"
echo ""
