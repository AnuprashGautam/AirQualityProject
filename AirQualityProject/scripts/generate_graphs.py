import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cities = ["Delhi", "Mumbai", "Hyderabad", "Bangalore"]
pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

dfs = []
for city in cities:
    df = pd.read_csv(f"../data/{city.lower()}.csv")
    df["City"] = city
    df["Date"] = pd.to_datetime(df["Date"])
    dfs.append(df)

full_df = pd.concat(dfs)

# AQI Trend
latest_date = full_df["Date"].max()
last_7_days = full_df[full_df["Date"] >= latest_date - pd.Timedelta(days=7)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=last_7_days, x="Date", y="AQI", hue="City", marker="o")
plt.title("AQI Trend Over Last 7 Days")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pollutant Comparison
latest_df = full_df[full_df["Date"] == latest_date]
melted = latest_df.melt(id_vars=["City"], value_vars=pollutants, var_name="Pollutant", value_name="Level")

plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x="Pollutant", y="Level", hue="City")
plt.title("Pollutant Levels by City")
plt.xlabel("Pollutant")
plt.ylabel("Concentration (µg/m³)")
plt.tight_layout()
plt.show()