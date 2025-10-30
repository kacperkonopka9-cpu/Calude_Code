#!/bin/bash
# Wrapper script for server upload
# This allows running from the main directory

cd "$(dirname "$0")"
bash scripts/upload-to-server.sh "$@"
