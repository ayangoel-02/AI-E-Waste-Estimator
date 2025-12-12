@echo off
REM Quick start script for E-Waste Estimator (Windows)

echo 🤖 AI-Powered E-Waste Material Recovery Estimator
echo ==================================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Check if data exists
if not exist "data\synthetic_ewaste.csv" (
    echo Generating synthetic data...
    python src\gen_data.py
)

REM Check if model exists
if not exist "models\ewaste_estimator.pkl" (
    echo Training model...
    python src\train.py
)

REM Start the server
echo.
echo Starting server...
echo Open http://localhost:8000 in your browser
echo.
cd src
python app.py
pause

