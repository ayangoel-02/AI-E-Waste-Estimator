# gen_data.py
# Generate synthetic e-waste dataset for training

import pandas as pd
import numpy as np
import random
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Base directory
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Device types and their characteristics
DEVICE_TYPES = {
    "smartphone": {
        "weight_range": (100, 250),
        "copper_base": (8, 20),
        "gold_base": (30, 60),
        "plastic_base": (20, 50),
        "lithium_base": (2, 5),
        "screen_range": (4.5, 7.0),
        "difficulty_base": (30, 45),
        "risk_base": (35, 50)
    },
    "laptop": {
        "weight_range": (1000, 2500),
        "copper_base": (200, 400),
        "gold_base": (150, 300),
        "plastic_base": (200, 500),
        "lithium_base": (25, 60),
        "screen_range": (11.0, 17.0),
        "difficulty_base": (50, 70),
        "risk_base": (45, 65)
    },
    "tablet": {
        "weight_range": (300, 800),
        "copper_base": (15, 40),
        "gold_base": (50, 120),
        "plastic_base": (50, 150),
        "lithium_base": (10, 30),
        "screen_range": (7.0, 13.0),
        "difficulty_base": (40, 60),
        "risk_base": (40, 60)
    },
    "desktop": {
        "weight_range": (5000, 15000),
        "copper_base": (800, 2000),
        "gold_base": (500, 2000),
        "plastic_base": (1000, 3000),
        "lithium_base": (0, 5),
        "screen_range": (0, 0),
        "difficulty_base": (70, 90),
        "risk_base": (60, 80)
    },
    "monitor": {
        "weight_range": (2000, 8000),
        "copper_base": (300, 1500),
        "gold_base": (200, 1000),
        "plastic_base": (500, 2500),
        "lithium_base": (0, 2),
        "screen_range": (15.0, 32.0),
        "difficulty_base": (60, 85),
        "risk_base": (55, 75)
    },
    "charger": {
        "weight_range": (50, 200),
        "copper_base": (1, 5),
        "gold_base": (0.1, 1),
        "plastic_base": (20, 50),
        "lithium_base": (0, 0),
        "screen_range": (0, 0),
        "difficulty_base": (5, 20),
        "risk_base": (3, 15)
    },
    "battery_pack": {
        "weight_range": (200, 1000),
        "copper_base": (5, 15),
        "gold_base": (0.3, 2),
        "plastic_base": (50, 200),
        "lithium_base": (50, 200),
        "screen_range": (0, 0),
        "difficulty_base": (50, 70),
        "risk_base": (70, 90)
    },
    "other": {
        "weight_range": (50, 500),
        "copper_base": (1, 100),
        "gold_base": (0.1, 100),
        "plastic_base": (10, 200),
        "lithium_base": (0, 10),
        "screen_range": (0, 0),
        "difficulty_base": (20, 80),
        "risk_base": (20, 80)
    }
}

BRANDS = ["Apple", "Samsung", "Dell", "HP", "Lenovo", "Microsoft", "Google", "OnePlus", "Sony", "LG", "Generic"]
BATTERY_TYPES = ["li-ion", "li-poly", "none"]
CONDITIONS = ["working", "non-working", "damaged"]

def generate_device_name(device_type, brand, idx):
    """Generate a device model name"""
    if device_type == "smartphone":
        models = ["12", "13", "14", "S21", "S20", "S9", "Pixel 6", "9 Pro"]
    elif device_type == "laptop":
        models = ["Latitude 3520", "XPS 13", "Pavilion 14", "ThinkPad X1", "MacBook Air M1", "Spectre x360"]
    elif device_type == "tablet":
        models = ["iPad Pro", "Tab S7", "Surface Pro 8"]
    else:
        models = [f"Model {idx % 100}"]
    
    return f"{brand} {random.choice(models)}"

def generate_synthetic_data(n_samples=500):
    """Generate synthetic e-waste dataset"""
    data = []
    
    for i in range(n_samples):
        device_type = random.choice(list(DEVICE_TYPES.keys()))
        specs = DEVICE_TYPES[device_type]
        brand = random.choice(BRANDS)
        
        # Generate device characteristics
        launch_year = random.randint(2010, 2023)
        age_years = random.uniform(0.5, min(15, 2024 - launch_year))
        weight_g = random.uniform(*specs["weight_range"])
        battery_type = random.choice(BATTERY_TYPES)
        condition = random.choice(CONDITIONS)
        is_refurbished = random.choice([True, False])
        has_metal_chassis = random.choice([True, False]) if device_type in ["laptop", "tablet", "desktop"] else False
        screen_size = random.uniform(*specs["screen_range"]) if specs["screen_range"][1] > 0 else 0.0
        
        # Calculate material recovery based on device characteristics
        # Base amounts from device type
        copper_g = random.uniform(*specs["copper_base"])
        gold_mg = random.uniform(*specs["gold_base"])
        plastic_g = random.uniform(*specs["plastic_base"])
        lithium_g = random.uniform(*specs["lithium_base"]) if battery_type != "none" else 0.0
        
        # Adjustments based on weight
        weight_factor = weight_g / 1000  # Normalize to kg
        copper_g *= (0.8 + 0.4 * weight_factor)
        gold_mg *= (0.9 + 0.2 * weight_factor)
        plastic_g *= (0.8 + 0.4 * weight_factor)
        
        # Adjustments based on age (older devices may have more/different materials)
        age_factor = 1 + (age_years / 20) * 0.3
        copper_g *= age_factor
        gold_mg *= age_factor
        
        # Adjustments based on condition
        if condition == "damaged":
            copper_g *= 0.9  # Some loss
            gold_mg *= 0.95
            plastic_g *= 0.85
        elif condition == "non-working":
            copper_g *= 0.95
            gold_mg *= 0.98
            plastic_g *= 0.9
        
        # Metal chassis increases metal content
        if has_metal_chassis:
            copper_g *= 1.2
            gold_mg *= 1.1
        
        # Calculate recycling difficulty (0-100)
        difficulty = random.uniform(*specs["difficulty_base"])
        if device_type in ["charger", "battery_pack"]:
            difficulty += 10 if battery_type != "none" else -5
        if condition == "damaged":
            difficulty += 10
        if age_years > 10:
            difficulty += 5
        difficulty = min(100, max(0, difficulty))
        
        # Calculate environmental risk (0-100)
        risk = random.uniform(*specs["risk_base"])
        if battery_type != "none":
            risk += 15
        if lithium_g > 50:
            risk += 10
        if condition == "damaged":
            risk += 5
        risk = min(100, max(0, risk))
        
        device_model = generate_device_name(device_type, brand, i)
        
        data.append({
            "device_model": device_model,
            "device_type": device_type,
            "brand": brand,
            "launch_year": launch_year,
            "age_years": round(age_years, 1),
            "weight_g": round(weight_g, 1),
            "battery_type": battery_type,
            "condition": condition,
            "is_refurbished": is_refurbished,
            "has_metal_chassis": has_metal_chassis,
            "screen_size_in": round(screen_size, 1),
            "copper_g": round(copper_g, 2),
            "gold_mg": round(gold_mg, 2),
            "plastic_g": round(plastic_g, 2),
            "lithium_g": round(lithium_g, 2),
            "recycling_difficulty": round(difficulty, 1),
            "environmental_risk": round(risk, 1)
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating synthetic e-waste dataset...")
    df = generate_synthetic_data(n_samples=1000)
    
    # Ensure data directory exists
    DATA_DIR.mkdir(exist_ok=True)
    
    # Save to CSV
    output_path = DATA_DIR / "synthetic_ewaste.csv"
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} samples")
    print(f"Dataset saved to {output_path}")
    print("\nDataset preview:")
    print(df.head(10))
    print(f"\nDataset statistics:")
    print(df.describe())

