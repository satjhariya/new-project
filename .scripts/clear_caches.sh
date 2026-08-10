#!/usr/bin/env bash

set -e

echo "🧹 Clearing caches..."

find . -type d \( \
    -name "__pycache__" \
    -o -name ".pytest_cache" \
    -o -name ".ruff_cache" \
    -o -name ".pyrefly_cache" \
    -o -name ".hypothesis" \
    -o -name ".tox" \
\) -exec rm -rf {} +

find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete

echo "✅ Caches cleared."