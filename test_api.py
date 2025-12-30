import requests
import json

# URL of your running FastAPI app
base_url = "http://127.0.0.1:8000"

# Send a GET request to the root endpoint
r = requests.get(f"{base_url}/")
print("GET request:")
print("Status Code:", r.status_code)
print("Response:", r.json())
print("\n")

# Sample data for the POST request
sample_data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST request to the /data/ endpoint
r = requests.post(f"{base_url}/data/", json=sample_data)
print("POST request:")
print("Status Code:", r.status_code)
print("Response:", r.json())