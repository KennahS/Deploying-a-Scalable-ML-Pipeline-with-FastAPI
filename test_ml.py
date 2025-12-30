import pytest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# TODO: add necessary import
from ml.data import process_data
from ml.model import train_model, compute_model_metrics


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test that process_data returns expected data types
    """
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    data = pd.read_csv("data/census.csv")

    train, _ = train_test_split(
        data,
        test_size=0.2,
        random_state=42,
        stratify=data["salary"],
    )

    X, y, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert X.shape[0] == y.shape[0]

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test that train_model returns the expected model type
    """
    from sklearn.ensemble import RandomForestClassifier

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    data = pd.read_csv("data/census.csv")

    train, _ = train_test_split(
        data,
        test_size=0.2,
        random_state=42,
        stratify=data["salary"],
    )

    X_train, y_train, _, _ = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test that compute_model_metrics returns valid metric values
    """
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)

    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0