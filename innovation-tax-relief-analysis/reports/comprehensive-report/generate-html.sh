#!/bin/bash
# Wrapper script for HTML generation
# This allows running from the main directory

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"
cd scripts && bash generate-html.sh "$@"
