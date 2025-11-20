from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("../models/model.pkl")

def get_severity_label(aqi):
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Satisfactory"
    elif aqi <= 200: return "Moderate"
    elif aqi <= 300: return "Poor"
    elif aqi <= 400: return "Very Poor"
    else: return "Severe"

def get_health_advice(severity, age_group):
    if severity == "Good":
        return "Air quality is good. Enjoy your day!"
    elif severity == "Satisfactory":
        return "Air quality is acceptable. Sensitive individuals should be cautious."
    elif severity == "Moderate":
        return "May cause minor breathing discomfort. Children and elderly should reduce outdoor activity."
    elif severity == "Poor":
        return "Avoid outdoor exertion. Use masks if needed."
    elif severity == "Very Poor":
        return "Stay indoors. Use air purifiers if possible."
    else:
        return "Health alert! Avoid all outdoor activity. Seek medical attention if needed."

def load_pollutants(city):
    file_map = {
        "Delhi": "../data/delhi.csv",
        "Mumbai": "../data/mumbai.csv",
        "Hyderabad": "../data/hyderabad.csv",
        "Bangalore": "../data/bangalore.csv"
    }
    df = pd.read_csv(file_map[city])
    df["Date"] = pd.to_datetime(df["Date"])
    latest = df.sort_values("Date", ascending=False).iloc[0]
    return {
        "PM2.5": latest["PM2.5"],
        "PM10": latest["PM10"],
        "NO2": latest["NO2"],
        "SO2": latest["SO2"],
        "CO": latest["CO"],
        "O3": latest["O3"]
    }

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/predict", methods=["POST"])
def predict():
    req = request.get_json()
    city = req.get("city")
    age_group = req.get("age_group")

    try:
        pollutants = load_pollutants(city)
        aqi = model.predict([list(pollutants.values())])[0]
        severity = get_severity_label(aqi)
        advice = get_health_advice(severity, age_group)

        return jsonify({
            "city": city,
            "pollutants": pollutants,
            "aqi": round(aqi, 2),
            "severity": severity,
            "advice": advice
        })

    except Exception as e:
        return jsonify({ "error": str(e) })

if __name__ == "__main__":
    app.run(debug=True)