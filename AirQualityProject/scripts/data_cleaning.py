# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 23:01:24 2025

@author: KHUSHI ARORA
"""

import pandas as pd
import os

# === CONFIG ===
DATASET_FOLDER = "../dataset_unzipped"
DATASET_FILE = "city_day.csv"  # Change to "city_hour.csv", "station_day.csv", etc.
TARGET_CITY = "Ahmedabad"      # Or use station name if using station-level data
OUTPUT_FILE = "../data/cleaned_aqi.csv"

# === Load Dataset ===
path = os.path.join(DATASET_FOLDER, DATASET_FILE)
df = pd.read_csv(path)

# === Detect Date Column ===
date_col = "Date" if "Date" in df.columns else "Datetime"
df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
df.set_index(date_col, inplace=True)

# === Filter by City or Station ===
if "City" in df.columns:
    df = df[df['City'] == TARGET_CITY]
elif "StationId" in df.columns:
    df = df[df['StationId'] == TARGET_CITY]  # Replace with actual station name or ID

# === Drop Missing Values in Key Pollutants ===
required_cols = ['PM2.5', 'PM10', 'CO', 'NO2', 'SO2', 'O3']
df = df.dropna(subset=required_cols)

# === Keep Only Relevant Columns ===
df = df[required_cols]

# === Save Cleaned Data ===
df.to_csv(OUTPUT_FILE)
print(f"✅ Cleaned data saved to {OUTPUT_FILE}")