import joblib
import pandas as pd

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / ".." / "data" / "raw" / "HR-Employee-Attrition.csv"
MODEL_PATH = BASE_DIR / "attrition_model.pkl"


# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print("Shape:", df.shape)

features = [
    "Age",
    "Department",
    "JobRole",
    "MonthlyIncome",
    "JobLevel",
    "OverTime",
    "JobSatisfaction",
    "WorkLifeBalance",
    "YearsAtCompany",
    "BusinessTravel"
]

X = df[features]
y = df["Attrition"]

print("Features selected:", len(features))
print("Target:", "Attrition")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)