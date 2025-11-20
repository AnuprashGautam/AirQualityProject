import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "city": "Delhi",
    "age_group": "adult"
}

res = requests.post(url, json=data)
print(res.json())