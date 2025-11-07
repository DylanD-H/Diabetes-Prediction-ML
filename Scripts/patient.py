import requests

url = "http://localhost:9696/predict"

patient = {
    'Age': 49,
    'Gender': 'F',
    'BMI': 24,
    'Chol': 5.29,
    'TG': 1.74,
    'HDL': 4.8,
    'LDL': 4.8,
    'Cr': 52,
    'BUN': 4.07
}
response = requests.post(url, json=patient).json()
print(response)