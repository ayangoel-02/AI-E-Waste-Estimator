# 🤖 AI-Powered E-Waste Material Recovery Estimator

A machine learning-powered web application that predicts recoverable materials (copper, gold, plastic, lithium) from electronic waste devices, along with recycling difficulty scores and environmental risk assessments.

## 🌟 Features

- **Material Recovery Prediction**: Estimates recoverable amounts of:
  - Copper (grams)
  - Gold (milligrams)
  - Plastic (grams)
  - Lithium (grams)

- **Recycling Metrics**:
  - Recycling Difficulty Score (0-100)
  - Environmental Risk Score (0-100)

- **Device Database**: Pre-loaded database of common device models (iPhone, Galaxy, Dell laptops, etc.) for quick lookup

- **Modern Web Interface**: Beautiful, responsive UI with real-time predictions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "AI Powered E-Waste"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Setup and Training

1. **Generate synthetic training data**:
   ```bash
   python src/gen_data.py
   ```
   This creates `data/synthetic_ewaste.csv` with 1000 synthetic device samples.

2. **Train the machine learning model**:
   ```bash
   python src/train.py
   ```
   This trains a Random Forest regression model and saves it to `models/ewaste_estimator.pkl`.

### Running the Application

1. **Start the FastAPI server**:
   ```bash
   cd src
   python app.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn src.app:app --reload
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

3. **Enter device information**:
   - Device Model (e.g., "iPhone 12", "Dell Latitude 3520")
   - Device Type, Brand, Launch Year, Age, Weight, etc.
   - Click "Predict Recovery" to get estimates

## 📁 Project Structure

```
AI Powered E-Waste/
├── data/
│   └── synthetic_ewaste.csv          # Training dataset
├── models/
│   └── ewaste_estimator.pkl         # Trained ML model
├── src/
│   ├── app.py                        # FastAPI application
│   ├── train.py                      # Model training script
│   ├── gen_data.py                   # Synthetic data generator
│   └── device_database.py            # Device specifications database
├── static/
│   └── index.html                    # Web interface
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 🔧 How It Works

### Machine Learning Model

- **Algorithm**: Random Forest Regressor (Multi-output)
- **Features**: Device type, brand, launch year, age, weight, battery type, condition, refurbished status, metal chassis, screen size
- **Targets**: 6 outputs (copper, gold, plastic, lithium, recycling difficulty, environmental risk)
- **Preprocessing**: One-hot encoding for categorical features, standardization for numerical features

### Device Database

The application includes a database of common device models. When you enter a device model name (e.g., "iPhone 12"), it automatically fills in specifications like:
- Device type
- Brand
- Launch year
- Weight
- Battery type
- Screen size
- Metal chassis status

### Prediction Pipeline

1. User enters device information (or device model name)
2. System looks up device in database (if model name provided)
3. Features are extracted and preprocessed
4. ML model predicts material recovery amounts and scores
5. Results are displayed with visualizations

## 📊 Example Predictions

**iPhone 12 (3 years old, working condition)**:
- Copper: ~12.5g
- Gold: ~45mg
- Plastic: ~30g
- Lithium: ~2.8g
- Recycling Difficulty: ~35/100
- Environmental Risk: ~42/100

**Dell Latitude 3520 Laptop (2 years old, working condition)**:
- Copper: ~320g
- Gold: ~200mg
- Plastic: ~400g
- Lithium: ~40g
- Recycling Difficulty: ~60/100
- Environmental Risk: ~55/100

## 🎯 Use Cases

- **E-Waste Recycling Centers**: Estimate material recovery potential
- **Environmental Assessment**: Evaluate environmental impact of devices
- **Research & Education**: Study e-waste composition and recovery
- **Sustainability Projects**: Make informed decisions about device disposal

## 🔬 Technical Details

### Model Performance

The model is trained on synthetic data that simulates real-world e-waste characteristics:
- Device type-specific material compositions
- Age-based degradation factors
- Condition-based recovery adjustments
- Weight-proportional material amounts

### Data Generation

The synthetic dataset (`gen_data.py`) generates realistic device samples based on:
- Industry-standard device specifications
- Material composition research
- Real-world e-waste patterns

## 🛠️ Development

### Regenerating Data

To generate a new dataset with different parameters:
```bash
python src/gen_data.py
```
Edit `n_samples` in the script to change dataset size.

### Retraining the Model

After modifying data or features:
```bash
python src/train.py
```

### API Documentation

FastAPI provides automatic API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📝 API Endpoints

- `GET /`: Serve the web interface
- `POST /predict`: Make predictions
  ```json
  {
    "device_model": "iPhone 12",
    "device_type": "smartphone",
    "brand": "Apple",
    "launch_year": 2020,
    "age_years": 3.0,
    "weight_g": 164.0,
    "battery_type": "li-ion",
    "condition": "working",
    "is_refurbished": false,
    "has_metal_chassis": false,
    "screen_size_in": 6.1
  }
  ```

## 🎓 Why This Project is Unique

- **Metal Recovery Prediction**: Most student projects focus on classification or general recycling, but this specifically predicts recoverable precious metals (copper, gold)
- **Multi-output Regression**: Predicts 6 different metrics simultaneously
- **Real-world Application**: Addresses the growing e-waste problem with actionable insights
- **Device Database Integration**: Smart lookup system for common devices

## 📚 Future Enhancements

- [ ] Add more device models to database
- [ ] Integrate real-world e-waste datasets
- [ ] Add image recognition for device identification
- [ ] Implement batch prediction for multiple devices
- [ ] Add export functionality for reports
- [ ] Include more materials (silver, palladium, etc.)

## 🤝 Contributing

Feel free to contribute by:
- Adding more device models to the database
- Improving the ML model with better features
- Enhancing the UI/UX
- Adding new material types

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built with FastAPI, scikit-learn, and modern web technologies
- Inspired by the need for better e-waste management and recycling

---

**Made with ❤️ for a sustainable future**

