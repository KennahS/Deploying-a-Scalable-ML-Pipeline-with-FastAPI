import pytest
from unittest.mock import patch
import requests

# Sample data for POST request
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

# Mock GET request
def test_get_root():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "Welcome to the Census Income Classifier API!"}

        response = requests.get("http://127.0.0.1:8000/")
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the Census Income Classifier API!"

# Mock POST request
def test_post_inference():
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": "<=50K"}

        response = requests.post("http://127.0.0.1:8000/data/", json=sample_data)
        assert response.status_code == 200
        assert response.json()["result"] in ("<=50K", ">50K")
