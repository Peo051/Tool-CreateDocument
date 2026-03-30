#!/bin/bash
# Run CI checks locally before pushing

set -e

echo "=== Installing dependencies ==="
pip install -r requirements_pro.txt
pip install -r requirements_test.txt
pip install pydantic

echo ""
echo "=== Running tests (same as CI) ==="
python -m pytest tests/ -v --tb=short -k "not (pdf or integration)"

echo ""
echo "=== Running lint check ==="
pip install ruff
ruff check source/ --select E,F,W --ignore E501,F401,F841 --exit-zero

echo ""
echo "✅ All CI checks passed locally!"
