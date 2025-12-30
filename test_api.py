import requests

# URL of your running FastAPI app
url = "http://127.0.0.1:8000/data/"

# Example input matching your Data model
sample_data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 9,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}

response = requests.post(url, json=sample_data)

print(response.status_code)
print(response.json())
