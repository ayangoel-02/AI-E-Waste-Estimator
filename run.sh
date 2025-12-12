#!/bin/bash
# Quick start script for E-Waste Estimator

echo "🤖 AI-Powered E-Waste Material Recovery Estimator"
echo "=================================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Check if data exists
if [ ! -f "data/synthetic_ewaste.csv" ]; then
    echo "Generating synthetic data..."
    python src/gen_data.py
fi

# Check if model exists
if [ ! -f "models/ewaste_estimator.pkl" ]; then
    echo "Training model..."
    python src/train.py
fi

# Start the server
echo ""
echo "Starting server..."
echo "Open http://localhost:8000 in your browser"
echo ""
cd src
python app.py

