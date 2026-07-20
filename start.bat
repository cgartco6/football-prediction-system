@echo off
echo === Football Predictor ===
call venv\Scripts\activate.bat 2>nul || echo Create venv first!
python src\main.py
pause
