import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "rainfall": 120,
    "temperature": 32,
    "humidity": 75,
    "soil_type": "loam",
    "crop_type": "rice",
    "acres": 2.0
}

response = requests.post(url, json=data)
print("Response:", response.json())
