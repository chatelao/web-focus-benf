#!/bin/bash
# Script to build a standalone executable using PyInstaller

# Ensure we are in the project root
cd "$(dirname "$0")/.."

# Install dependencies if needed
pip install -r requirements.txt

# Run PyInstaller
# --onefile: Create a single executable
# --name transpile: Name of the output binary
# --paths src: Include src in the search path for modules
# --add-data "src/templates:templates": Bundle Jinja2 templates
pyinstaller --onefile \
            --name transpile \
            --paths src \
            --add-data "src/templates:templates" \
            scripts/transpile.py

echo "Build complete. Executable is available in dist/transpile"
