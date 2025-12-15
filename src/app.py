# app.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import os
from pathlib import Path
from .device_database import lookup_device

# Get the base directory (parent of src)
BASE_DIR = Path(__file__).parent.parent

# app = FastAPI(title="AI-Powered E-Waste Material Recovery Estimator")
app = FastAPI(
    title="AI-Powered E-Waste Recovery Estimator",
    root_path="/api"
)


# Load model
model_path = BASE_DIR / "models" / "ewaste_estimator.pkl"
if not model_path.exists():
    raise FileNotFoundError(f"Model file not found at {model_path}. Please run train.py first.")

model = joblib.load(model_path)

class DeviceInput(BaseModel):
    device_model: str = ""
    device_type: str
    brand: str
    launch_year: int
    age_years: float
    weight_g: float
    battery_type: str
    condition: str
    is_refurbished: bool = False
    has_metal_chassis: bool = False
    screen_size_in: float = 0.0

@app.get("/")
def read_root():
    """Serve the main HTML page"""
    html_path = BASE_DIR / "static" / "index.html"
    if html_path.exists():
        return FileResponse(html_path)
    return {"message": "E-Waste Material Recovery Estimator API", "docs": "/docs"}

@app.get("/results.html")
async def read_results():
    """Serve the results HTML page"""
    html_path = BASE_DIR / "static" / "results.html"
    if html_path.exists():
        return FileResponse(str(html_path), media_type="text/html")
    raise HTTPException(status_code=404, detail="Results page not found")

@app.get("/index.html")
def read_index():
    """Serve the index HTML page"""
    html_path = BASE_DIR / "static" / "index.html"
    if html_path.exists():
        return FileResponse(html_path, media_type="text/html")
    raise HTTPException(status_code=404, detail="Index page not found")

@app.post("/predict")
def predict(device: DeviceInput):
    """
    Predict recoverable materials and environmental metrics for an e-waste device.
    
    If device_model is provided, it will try to auto-fill missing fields from the database.
    """
    try:
        # Try to lookup device in database if device_model is provided
        device_specs = None
        if device.device_model:
            device_specs = lookup_device(device.device_model)
            if device_specs:
                # Auto-fill missing or default values from database
                if not device.device_type or device.device_type == "smartphone":
                    device.device_type = device_specs.get("device_type", device.device_type)
                if not device.brand or device.brand.lower() == "apple":
                    device.brand = device_specs.get("brand", device.brand)
                if device.launch_year == 2020:  # Default value
                    device.launch_year = device_specs.get("launch_year", device.launch_year)
                if device.weight_g == 164:  # Default value
                    device.weight_g = device_specs.get("weight_g", device.weight_g)
                if device.battery_type == "li-ion":  # Default value
                    device.battery_type = device_specs.get("battery_type", device.battery_type)
                if device.screen_size_in == 0.0 or device.screen_size_in == 6.1:  # Default values
                    device.screen_size_in = device_specs.get("screen_size_in", device.screen_size_in)
                if not device.has_metal_chassis:
                    device.has_metal_chassis = device_specs.get("has_metal_chassis", device.has_metal_chassis)
        
        # Prepare features for prediction as DataFrame (model expects DataFrame)
        X = pd.DataFrame([{
            'device_type': device.device_type,
            'brand': device.brand,
            'launch_year': device.launch_year,
            'age_years': device.age_years,
            'weight_g': device.weight_g,
            'battery_type': device.battery_type,
            'condition': device.condition,
            'is_refurbished': int(device.is_refurbished),
            'has_metal_chassis': int(device.has_metal_chassis),
            'screen_size_in': device.screen_size_in
        }])
        
        # Make prediction
        preds = model.predict(X)[0]
        
        # Format results
        result = {
            "copper_g": max(0.0, float(preds[0])),  # Clamp to non-negative
            "gold_mg": max(0.0, float(preds[1])),
            "plastic_g": max(0.0, float(preds[2])),
            "lithium_g": max(0.0, float(preds[3])),
            "recycling_difficulty": max(0.0, min(100.0, float(preds[4]))),  # Clamp to 0-100
            "environmental_risk": max(0.0, min(100.0, float(preds[5])))  # Clamp to 0-100
        }
        
        return {
            "input": device.dict(),
            "prediction": result,
            "device_found_in_db": device_specs is not None
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Mount static files
static_dir = BASE_DIR / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
