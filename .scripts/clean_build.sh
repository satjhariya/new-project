#!/usr/bin/env bash

set -e

echo "🧹 Cleaning build artifacts..."

rm -rf \
    build \
    dist \
    .coverage \
    htmlcov

find . -maxdepth 2 -type d -name "*.egg-info" -exec rm -rf {} +

echo "✅ Build artifacts removed."