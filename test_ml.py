import pytest
# TODO: add necessary import
from fastapi.testclient import TestClient
from main import app

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test the root endpoint returns a welcome message
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Census Income Classifier API!"}

client = TestClient(app)


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test /data/ endpoint with a valid sample input
    """
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
        "native-country": "United-States"
    }
    response = client.post("/data/", json=sample_data)
    assert response.status_code == 200
    assert "result" in response.json()


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test /data/ endpoint with invalid input (missing 'age')
    """
    sample_data = {
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
        "native-country": "United-States"
    }
    response = client.post("/data/", json=sample_data)
    assert response.status_code == 422
