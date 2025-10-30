#!/bin/bash
# ============================================
# Automated FTP Upload Script for Inov Report
# Uploads website-upload/ to cyber-folks server
# ============================================

# Color codes for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
CREDENTIALS_FILE=".ftp-credentials"
LOCAL_DIR="../output/website"

echo -e "${BLUE}========================================"
echo "Inov Report - Automated Upload"
echo -e "========================================${NC}"
echo ""

# Check if credentials file exists
if [ ! -f "$CREDENTIALS_FILE" ]; then
    echo -e "${RED}ERROR: Credentials file not found!${NC}"
    echo ""
    echo "Please create credentials file:"
    echo "  1. Copy template: cp .ftp-credentials.template .ftp-credentials"
    echo "  2. Edit file: nano .ftp-credentials (or any text editor)"
    echo "  3. Fill in your FTP username, password, and host"
    echo "  4. Run this script again"
    echo ""
    exit 1
fi

# Load credentials
source "$CREDENTIALS_FILE"

# Validate credentials
if [ -z "$FTP_HOST" ] || [ -z "$FTP_USER" ] || [ -z "$FTP_PASS" ]; then
    echo -e "${RED}ERROR: Incomplete credentials!${NC}"
    echo "Please check your .ftp-credentials file"
    echo "Required: FTP_HOST, FTP_USER, FTP_PASS, REMOTE_PATH"
    exit 1
fi

# Check if local directory exists
if [ ! -d "$LOCAL_DIR" ]; then
    echo -e "${RED}ERROR: Local directory '$LOCAL_DIR' not found!${NC}"
    echo "Please run ./generate-html.sh first to create HTML files"
    exit 1
fi

echo -e "${BLUE}Upload Configuration:${NC}"
echo "  Host: $FTP_HOST"
echo "  User: $FTP_USER"
echo "  Remote path: $REMOTE_PATH"
echo "  Local directory: $LOCAL_DIR/"
echo ""

# Ask for confirmation
read -p "Upload files to server? (y/n): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Upload cancelled."
    exit 0
fi

echo ""
echo -e "${BLUE}Starting upload...${NC}"
echo ""

# Method 1: Try using lftp (best option)
if command -v lftp &> /dev/null; then
    echo -e "${YELLOW}Using lftp for upload...${NC}"

    lftp -c "
    set ftp:ssl-allow no
    set net:timeout 10
    set net:max-retries 3
    open -u $FTP_USER,$FTP_PASS $FTP_HOST
    lcd $LOCAL_DIR
    cd $REMOTE_PATH
    mirror --reverse --delete --verbose --parallel=3
    bye
    "

    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}========================================"
        echo "✓ Upload successful!"
        echo -e "========================================${NC}"
        echo ""
        echo "Your report is now live at:"
        echo "  https://inovgroup.pl/raport-ulgi-br/"
        echo ""
    else
        echo -e "${RED}Upload failed!${NC}"
        echo "Please check your credentials and try again."
        exit 1
    fi

# Method 2: Try using ncftp (alternative)
elif command -v ncftpput &> /dev/null; then
    echo -e "${YELLOW}Using ncftp for upload...${NC}"

    ncftpput -R -u "$FTP_USER" -p "$FTP_PASS" "$FTP_HOST" "$REMOTE_PATH" "$LOCAL_DIR"/*

    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓ Upload successful!${NC}"
        echo "Your report is live at: https://inovgroup.pl/raport-ulgi-br/"
    else
        echo -e "${RED}Upload failed!${NC}"
        exit 1
    fi

# Method 3: Use curl (slower but widely available)
elif command -v curl &> /dev/null; then
    echo -e "${YELLOW}Using curl for upload (this may take a while)...${NC}"
    echo -e "${YELLOW}Note: curl uploads one file at a time${NC}"
    echo ""

    # Upload all HTML files
    for file in "$LOCAL_DIR"/*.html "$LOCAL_DIR"/*.css "$LOCAL_DIR"/*.txt; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            echo "Uploading: $filename"
            curl -T "$file" "ftp://$FTP_HOST$REMOTE_PATH$filename" --user "$FTP_USER:$FTP_PASS" --ftp-create-dirs
        fi
    done

    # Upload images directory
    echo "Uploading images..."
    for image in "$LOCAL_DIR/images"/*; do
        if [ -f "$image" ]; then
            filename=$(basename "$image")
            echo "Uploading: images/$filename"
            curl -T "$image" "ftp://$FTP_HOST${REMOTE_PATH}images/$filename" --user "$FTP_USER:$FTP_PASS" --ftp-create-dirs
        fi
    done

    echo ""
    echo -e "${GREEN}✓ Upload complete!${NC}"
    echo "Your report is live at: https://inovgroup.pl/raport-ulgi-br/"

else
    echo -e "${RED}ERROR: No FTP client found!${NC}"
    echo ""
    echo "Please install one of these:"
    echo "  - lftp (recommended):    sudo apt-get install lftp"
    echo "  - ncftp:                 sudo apt-get install ncftp"
    echo "  - curl (usually pre-installed)"
    echo ""
    echo "Or upload manually using instructions in:"
    echo "  INSTRUKCJA-PUBLIKACJI-RAPORTU.md"
    exit 1
fi

echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. Test your website: https://inovgroup.pl/raport-ulgi-br/"
echo "  2. Check all pages load correctly"
echo "  3. Test navigation links"
echo "  4. View on mobile device"
echo ""
echo -e "${YELLOW}To update in the future:${NC}"
echo "  1. Edit markdown files"
echo "  2. Run: ./generate-html.sh"
echo "  3. Run: ./upload-to-server.sh"
echo ""
