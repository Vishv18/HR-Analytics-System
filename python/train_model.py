import joblib
import pandas as pd

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

print("Model training completed.")

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

# Numerical features
numeric_features = [
    "Age",
    "MonthlyIncome",
    "JobLevel",
    "JobSatisfaction",
    "WorkLifeBalance",
    "YearsAtCompany"
]

# Categorical features
categorical_features = [
    "Department",
    "JobRole",
    "OverTime",
    "BusinessTravel"
]
# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Final Balanced Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    class_weight="balanced",
    random_state=42
)

# Complete ML pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Train the final pipeline
pipeline.fit(X_train, y_train)

print("Model training completed.")

# Evaluate the final model
test_probabilities = pipeline.predict_proba(X_test)[:, 1]

test_predictions = [
    "Yes" if probability >= 0.50 else "No"
    for probability in test_probabilities
]

accuracy = accuracy_score(y_test, test_predictions)
precision = precision_score(y_test, test_predictions, pos_label="Yes")
recall = recall_score(y_test, test_predictions, pos_label="Yes")
f1 = f1_score(y_test, test_predictions, pos_label="Yes")
roc_auc = roc_auc_score(
    y_test,
    pipeline.predict_proba(X_test)[:, 1]
)

cm = confusion_matrix(y_test, test_predictions, labels=["No", "Yes"])

print("\nFinal Model Evaluation")
print("----------------------")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")
print(f"ROC-AUC:   {roc_auc:.4f}")
print("\nConfusion Matrix:")
print(cm)

# Save the trained pipeline
joblib.dump(pipeline, MODEL_PATH)

print(f"\nModel saved successfully to: {MODEL_PATH}")