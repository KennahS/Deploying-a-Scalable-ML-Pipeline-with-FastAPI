import requests

# URL of your running FastAPI app
base_url = "http://127.0.0.1:8000"

# Example input matching your Data model
def test_root():
    """Test the root endpoint"""
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    assert "Welcome" in response.json().get("message", "")

def test_post_data():
    """Test the prediction endpoint"""
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
    response = requests.post(f"{base_url}/data/", json=sample_data)
    assert response.status_code == 200
    assert response.json().get("result")[0] in ["<=50K", ">50K"]