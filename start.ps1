Write-Host "=== Football Predictor ===" -ForegroundColor Green
& .\venv\Scripts\Activate.ps1 2>$null
python src/main.py
Read-Host "Press Enter to exit"
