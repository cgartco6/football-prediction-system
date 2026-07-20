#!/bin/bash
echo "=== Football Predictor ==="
source venv/bin/activate 2>/dev/null || echo "Create venv first!"
python src/main.py
read -p "Press Enter to exit..."
