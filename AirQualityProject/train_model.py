import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os

# Load datasets
data_path = os.path.join(os.path.dirname(__file__), "data")

files = ["Delhi.csv", "Mumbai.csv", "Hyderabad.csv", "Bangalore.csv"]
dfs = [pd.read_csv(os.path.join(data_path, f)) for f in files]
df = pd.concat(dfs, ignore_index=True)

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["dayofyear"] = df["Date"].dt.dayofyear.fillna(0)

features = ["City", "dayofyear", "PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
target = "AQI"

X = df[features]
y = df[target]

cat_cols = ["City"]
num_cols = ["dayofyear", "PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ("num", StandardScaler(), num_cols)
])

model = RandomForestRegressor(n_estimators=120, random_state=42)

pipeline = Pipeline([
    ("pre", preprocessor),
    ("model", model)
])

# Train
pipeline.fit(X, y)

# Save model
model_dir = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(model_dir, exist_ok=True)

joblib.dump(pipeline, os.path.join(model_dir, "aqi_pipeline_joblib.pkl"))

print("Model retrained and saved successfully!")
