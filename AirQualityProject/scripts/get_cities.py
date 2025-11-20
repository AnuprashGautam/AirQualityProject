# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 00:05:26 2025

@author: KHUSHI ARORA
"""

import requests

headers = {"X-API-Key": "dc3c7ec8ed56140b1819608be1e635b21d43b5418fc3c9fc70e6172499ead84b"}  # 👈 Replace with your actual key
url = "https://api.openaq.org/v3/cities?country=IN&limit=100"

res = requests.get(url, headers=headers)
data = res.json()

for city in data.get("results", []):
    print(city["city"])