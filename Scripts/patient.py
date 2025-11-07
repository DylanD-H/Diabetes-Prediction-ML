import requests

url = "http://localhost:9696/predict"

patient = {
    'Age': 50,
    'Gender': 'M',
    'BMI': 32,
    'Chol': 3.6,
    'TG': 1.6,
    'HDL': 1.4,
    'LDL': 3.0,
    'Cr': 72,
    'BUN': 5
}
response = requests.post(url, json=patient).json()
print(response)