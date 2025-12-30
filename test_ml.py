import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
# TODO: add necessary import
from ml.data import process_data
from ml.model import train_model, inference

# DO NOT MODIFY (same as training script)
CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test that the dataset loads correctly and is not empty
    """
    data = pd.read_csv("data/census.csv")

    assert data is not None
    assert len(data) > 0

# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test that the trained model is a RandomForestRegressor
    """
     data = pd.read_csv("data/census.csv")
    train, _ = train_test_split(
        data,
        test_size=0.20,
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
    # Test that the model can generate predictions
    and that the output length matches the input
    """
    data = pd.read_csv("data/census.csv")
    train, test = train_test_split(
        data,
        test_size=0.20,
        random_state=42,
        stratify=data["salary"],
    )

    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    X_test, _, _, _ = process_data(
        test,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    model = train_model(X_train, y_train)
    preds = inference(model, X_test)

    assert preds is not None
    assert len(preds) == len(X_test)
