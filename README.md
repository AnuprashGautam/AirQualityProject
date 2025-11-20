# ✅ **How to Run the Air Quality Prediction Model**

Follow these steps to set up and run the project on your machine.

---

## **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

---

## **2. Create a Virtual Environment**

**Note:** Navigate to `AirQualityProject` first and then create the virtual environment.


### **Windows:**

```bash
python -m venv venv
```

### **Linux / macOS:**

```bash
python3 -m venv venv
```

---

## **3. Activate the Virtual Environment**

### **Windows:**

```bash
venv\Scripts\activate
```

### **Linux / macOS:**

```bash
source venv/bin/activate
```

---

## **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

This installs Flask, scikit-learn, pandas, joblib, etc.

---

## **5. Run the Flask API**

```bash
python app/predict_api.py
```

You will see:

```
Running on http://127.0.0.1:5000/
```

---

## **6. Open the UI in Browser**

Visit:

```
http://127.0.0.1:5000/
```

Enter your input → click **Predict AQI** → see the result.
