# train.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from pathlib import Path

# Get base directory (parent of src)
BASE_DIR = Path(__file__).parent.parent

# 1. Load data
data_path = BASE_DIR / "data" / "synthetic_ewaste.csv"
if not data_path.exists():
    raise FileNotFoundError(f"Data file not found at {data_path}. Please run gen_data.py first.")

df = pd.read_csv(data_path)

# 2. Feature engineering
df['age_years'] = df['age_years'].astype(float)
df['weight_g'] = df['weight_g'].astype(float)
df['launch_year'] = df['launch_year'].astype(int)

# boolean to int (handle both string and boolean types)
def bool_to_int(val):
    if isinstance(val, bool):
        return int(val)
    if isinstance(val, str):
        return 1 if val.lower() in ['true', '1', 'yes'] else 0
    return int(bool(val))

df['is_refurbished'] = df['is_refurbished'].apply(bool_to_int)
df['has_metal_chassis'] = df['has_metal_chassis'].apply(bool_to_int)

# Drop device_model (text) to keep it simple, or keep brand/type
X = df[['device_type','brand','launch_year','age_years','weight_g','battery_type','condition','is_refurbished','has_metal_chassis','screen_size_in']]
y = df[['copper_g','gold_mg','plastic_g','lithium_g','recycling_difficulty','environmental_risk']]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Preprocessing
categorical_features = ['device_type','brand','battery_type','condition']
numeric_features = ['launch_year','age_years','weight_g','is_refurbished','has_metal_chassis','screen_size_in']

cat_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
num_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, numeric_features),
        ('cat', cat_transformer, categorical_features)
    ],
    remainder='drop'
)

# 5. Model pipeline - multioutput with RandomForest
rf = RandomForestRegressor(n_estimators=200, random_state=42)
multi = MultiOutputRegressor(rf)

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', multi)])

# 6. Train
pipeline.fit(X_train, y_train)

# 7. Evaluate
y_pred = pipeline.predict(X_test)
for i, col in enumerate(y.columns):
    mae = mean_absolute_error(y_test.iloc[:, i], y_pred[:, i])
    rmse = np.sqrt(mean_squared_error(y_test.iloc[:, i], y_pred[:, i]))
    r2 = r2_score(y_test.iloc[:, i], y_pred[:, i])
    print(f"{col} -> MAE: {mae:.3f}, RMSE: {rmse:.3f}, R2: {r2:.3f}")

# 8. Save model
models_dir = BASE_DIR / "models"
models_dir.mkdir(exist_ok=True)
model_path = models_dir / "ewaste_estimator.pkl"
joblib.dump(pipeline, model_path)
print(f"Model saved to {model_path}")
