from flask import Flask, request, jsonify, send_from_directory
import joblib, pandas as pd, os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__, static_folder='templates')
CORS(app)

# Correct model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'model', 'aqi_pipeline_joblib.pkl')

pipeline = joblib.load(MODEL_PATH)

def prepare_input(data):
    df = pd.DataFrame([data])

    # Convert Date → dayofyear
    if 'Date' in df.columns and pd.notnull(df.at[0, 'Date']):
        d = pd.to_datetime(df.at[0, 'Date'], errors='coerce')
        df['dayofyear'] = d.dayofyear if pd.notnull(d) else 0
    else:
        df['dayofyear'] = 0

    # Ensure all numeric columns exist
    for col in ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']:
        if col not in df.columns:
            df[col] = 0.0

    df = df[['City', 'dayofyear', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']]
    return df

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json(force=True)
    X = prepare_input(payload)
    pred = pipeline.predict(X)[0]
    return jsonify({'predicted_AQI': float(pred)})

@app.route('/')
def serve_ui():
    return send_from_directory('templates', 'index.html')

@app.route('/templates/<path:path>')
def serve_css(path):
    return send_from_directory('templates', path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
