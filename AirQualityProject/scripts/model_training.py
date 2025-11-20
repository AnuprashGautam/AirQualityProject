import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

cities = ["Delhi", "Mumbai", "Hyderabad", "Bangalore"]
dfs = []
for city in cities:
    df = pd.read_csv(f"../data/{city.lower()}.csv")
    dfs.append(df)

full_df = pd.concat(dfs)
X = full_df[["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]]
y = full_df["AQI"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "../models/model.pkl")
print("Model trained and saved.")