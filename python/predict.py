import joblib
import pandas as pd


# Load the trained ML pipeline
model = joblib.load("python/attrition_model.pkl")


def predict_attrition(employee_data):
    """
    Predict attrition risk for one employee.
    """

    # Convert employee information into a DataFrame
    employee_df = pd.DataFrame([employee_data])

    # Get probability of Attrition = Yes
    probability = model.predict_proba(employee_df)[0][1]

    # Apply the selected threshold
    prediction = "Yes" if probability >= 0.50 else "No"

    return prediction, probability