import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from ml.model import train_model, compute_model_metrics
from ml.data import process_data

# TODO: implement the first test. Change the function name and input as needed

# load small portiom for unit tests
df = pd.read_csv('data/census.csv').sample(n=100, random_state=42)
cat_features = [
    "workclass", "education", "marital-status", "occupation", 
    "relationship", "race", "sex", "native-country"
]
X, y, encoder, lb = process_data(df, categorical_features=cat_features, label="salary", training=True)
model = train_model(X, y)

def test_one():
    """
    # A test that the trained model is not None
    """
    # Your code here
    assert model is not None


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Testing that model predictions match input length
    """
    # Your code here
    preds = model.predict(X)
    assert len(preds) == len(X)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Tests that computed metrics are floats betwee 0 and 1.
    """
    # Your code here
    preds = model.predict(X)
    p, r, f1 = compute_model_metrics(y, preds)
    assert all(isinstance(m, float) for m in (p, r, f1))
    assert all(0 <=  m <= 1 for m in (p, r, f1))
