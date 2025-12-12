# device_database.py
# Database of common device models with their specifications

DEVICE_DATABASE = {
    # Apple Devices
    "iphone 12": {
        "device_type": "smartphone",
        "brand": "Apple",
        "launch_year": 2020,
        "weight_g": 164,
        "battery_type": "li-ion",
        "screen_size_in": 6.1,
        "has_metal_chassis": False
    },
    "iphone 13": {
        "device_type": "smartphone",
        "brand": "Apple",
        "launch_year": 2021,
        "weight_g": 174,
        "battery_type": "li-ion",
        "screen_size_in": 6.1,
        "has_metal_chassis": False
    },
    "iphone 14": {
        "device_type": "smartphone",
        "brand": "Apple",
        "launch_year": 2022,
        "weight_g": 172,
        "battery_type": "li-ion",
        "screen_size_in": 6.1,
        "has_metal_chassis": False
    },
    "macbook air m1": {
        "device_type": "laptop",
        "brand": "Apple",
        "launch_year": 2020,
        "weight_g": 1200,
        "battery_type": "li-poly",
        "screen_size_in": 13.3,
        "has_metal_chassis": True
    },
    "macbook pro 13": {
        "device_type": "laptop",
        "brand": "Apple",
        "launch_year": 2020,
        "weight_g": 1400,
        "battery_type": "li-poly",
        "screen_size_in": 13.3,
        "has_metal_chassis": True
    },
    "ipad pro": {
        "device_type": "tablet",
        "brand": "Apple",
        "launch_year": 2021,
        "weight_g": 466,
        "battery_type": "li-ion",
        "screen_size_in": 12.9,
        "has_metal_chassis": True
    },
    
    # Samsung Devices
    "galaxy s21": {
        "device_type": "smartphone",
        "brand": "Samsung",
        "launch_year": 2021,
        "weight_g": 169,
        "battery_type": "li-ion",
        "screen_size_in": 6.2,
        "has_metal_chassis": False
    },
    "galaxy s20": {
        "device_type": "smartphone",
        "brand": "Samsung",
        "launch_year": 2020,
        "weight_g": 163,
        "battery_type": "li-ion",
        "screen_size_in": 6.2,
        "has_metal_chassis": False
    },
    "galaxy s9": {
        "device_type": "smartphone",
        "brand": "Samsung",
        "launch_year": 2018,
        "weight_g": 189,
        "battery_type": "li-ion",
        "screen_size_in": 5.8,
        "has_metal_chassis": False
    },
    "galaxy tab s7": {
        "device_type": "tablet",
        "brand": "Samsung",
        "launch_year": 2020,
        "weight_g": 498,
        "battery_type": "li-ion",
        "screen_size_in": 11.0,
        "has_metal_chassis": True
    },
    
    # Dell Devices
    "dell latitude 3520": {
        "device_type": "laptop",
        "brand": "Dell",
        "launch_year": 2021,
        "weight_g": 1500,
        "battery_type": "li-ion",
        "screen_size_in": 15.6,
        "has_metal_chassis": True
    },
    "dell xps 13": {
        "device_type": "laptop",
        "brand": "Dell",
        "launch_year": 2021,
        "weight_g": 1200,
        "battery_type": "li-ion",
        "screen_size_in": 13.4,
        "has_metal_chassis": True
    },
    "dell inspiron 15": {
        "device_type": "laptop",
        "brand": "Dell",
        "launch_year": 2020,
        "weight_g": 1800,
        "battery_type": "li-ion",
        "screen_size_in": 15.6,
        "has_metal_chassis": False
    },
    
    # HP Devices
    "hp pavilion 14": {
        "device_type": "laptop",
        "brand": "HP",
        "launch_year": 2017,
        "weight_g": 1300,
        "battery_type": "li-ion",
        "screen_size_in": 14.0,
        "has_metal_chassis": False
    },
    "hp spectre x360": {
        "device_type": "laptop",
        "brand": "HP",
        "launch_year": 2021,
        "weight_g": 1350,
        "battery_type": "li-ion",
        "screen_size_in": 13.3,
        "has_metal_chassis": True
    },
    
    # Lenovo Devices
    "lenovo thinkpad x1": {
        "device_type": "laptop",
        "brand": "Lenovo",
        "launch_year": 2021,
        "weight_g": 1100,
        "battery_type": "li-ion",
        "screen_size_in": 14.0,
        "has_metal_chassis": True
    },
    "lenovo yoga": {
        "device_type": "laptop",
        "brand": "Lenovo",
        "launch_year": 2020,
        "weight_g": 1400,
        "battery_type": "li-ion",
        "screen_size_in": 14.0,
        "has_metal_chassis": True
    },
    
    # Other Devices
    "google pixel 6": {
        "device_type": "smartphone",
        "brand": "Google",
        "launch_year": 2021,
        "weight_g": 207,
        "battery_type": "li-ion",
        "screen_size_in": 6.4,
        "has_metal_chassis": False
    },
    "oneplus 9": {
        "device_type": "smartphone",
        "brand": "OnePlus",
        "launch_year": 2021,
        "weight_g": 192,
        "battery_type": "li-ion",
        "screen_size_in": 6.55,
        "has_metal_chassis": False
    },
    "surface pro 8": {
        "device_type": "tablet",
        "brand": "Microsoft",
        "launch_year": 2021,
        "weight_g": 891,
        "battery_type": "li-ion",
        "screen_size_in": 13.0,
        "has_metal_chassis": True
    }
}

def lookup_device(device_model: str):
    """
    Look up device specifications from database.
    Returns dict with device specs or None if not found.
    """
    if not device_model:
        return None
    
    # Normalize the device model string
    normalized = device_model.lower().strip()
    
    # Try exact match first
    if normalized in DEVICE_DATABASE:
        return DEVICE_DATABASE[normalized].copy()
    
    # Try partial matches
    for key, value in DEVICE_DATABASE.items():
        if key in normalized or normalized in key:
            return value.copy()
    
    return None

