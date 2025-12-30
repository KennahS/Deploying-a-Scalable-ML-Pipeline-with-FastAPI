import pytest
from sklearn.ensemble import RandomForestRegressor
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test that the dataset loads correctly and is not empty
    """
    assert data is not None
    assert len(data) > 0


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test that the trained model is a RandomForestRegressor
    """
    assert isinstance(model, RandomForestRegressor)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test that the model can generate predictions
    and that the output length matches the input
    """
    predictions = model.predict(X_test)
    assert predictions is not None
    assert len(predictions) == len(X_test)