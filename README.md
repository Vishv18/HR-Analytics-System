HR Analytics & Workforce Intelligence System

A data analytics and machine learning project for analyzing employee attrition, workforce patterns, and employee-level attrition risk.

The system combines MySQL, Python, Power BI, Machine Learning, and Streamlit into one workflow.

Project Overview

Employee attrition can affect workforce stability and increase recruitment and training costs. This project analyzes historical HR employee data to identify workforce and attrition patterns and provides a machine-learning-based estimate of attrition risk for individual employees.

The project has four main layers:

MySQL – database storage and SQL analysis

Python – data analysis and machine learning

Power BI – interactive business intelligence dashboards

Streamlit – application interface connecting analytics and ML prediction

Dataset

The project uses an HR employee attrition dataset containing:

1,470 employee records

35 original attributes

Employee demographics

Department and job information

Compensation

Job satisfaction

Work-life balance

Overtime

Business travel

Years at company

Attrition status

The target variable for machine learning is:

Attrition → Yes / No

Project Features

1. HR Database

The dataset is stored in a MySQL database named:

hr_analytics

The database includes lookup tables such as:

departments

job_roles

education_fields

and the main:

employees

The database design is intended to reduce redundancy and maintain consistent employee-related information.

2. SQL Analysis

SQL is used to analyze:

Workforce distribution

Department-wise employee counts

Attrition

Salary patterns

Employee characteristics

Business questions related to workforce retention

3. Power BI Dashboard

The Power BI dashboard provides interactive HR analytics through three main pages:

Executive Overview

Provides a high-level view of:

Total employees

Employees who left

Attrition rate

Workforce and compensation indicators

Attrition Analysis

Explores factors associated with employee attrition, including:

Department

Age

Overtime

Monthly income

Other employee characteristics

HR Insights / Workforce

Provides additional workforce-level analysis and employee insights.

4. Machine Learning – Attrition Prediction

Multiple classification models were trained and evaluated:

Logistic Regression

Decision Tree

Random Forest

Balanced Random Forest

The final prediction pipeline uses a Balanced Random Forest to address the class imbalance between employees who stayed and employees who left.

The model uses 10 employee attributes:

Age

Department

Job Role

Monthly Income

Job Level

Overtime

Job Satisfaction

Work-Life Balance

Years at Company

Business Travel

Model evaluation includes:

Accuracy

Precision

Recall

F1-score

ROC-AUC

Confusion Matrix

Final test-set results:

Metric

Result

Accuracy

80.61%

Precision

41.67%

Recall

53.19%

F1-score

46.73%

ROC-AUC

74.76%

The model produces a model-estimated attrition risk for an employee rather than a guaranteed outcome.

5. Streamlit Application

The Streamlit application brings the project components together.

Current sections:

Overview

Analytics & Power BI

Risk Prediction

Employee Directory

About System

Risk Prediction

Users can enter employee information and receive:

Predicted attrition status

Model-estimated attrition risk

Risk classification

Basic recommendations based on employee characteristics

Employee Directory

An employee can be searched using their Employee ID.

The system displays:

Employee profile information

Actual attrition status

Model-estimated attrition risk

Relevant employee metrics

Machine Learning Workflow

HR Dataset
    ↓
Feature Selection
    ↓
Train / Test Split
    ↓
Data Preprocessing
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Final Balanced Random Forest
    ↓
Saved Model Pipeline
    ↓
Streamlit Prediction

Project Structure

HR-Analytics-System/
│
├── dashboard/
│   └── HR Analytics Dashboard.pbix
│
├── data/
│   └── raw/
│       └── HR-Employee-Attrition.csv
│
├── database/
│
├── notebooks/
│   └── 01_ml_model.ipynb
│
├── python/
│   ├── attrition_model.pkl
│   └── predict.py
│
├── reports/
│
├── screenshots/
│
├── sql/
│   ├── database setup
│   ├── data validation
│   └── analysis queries
│
├── streamlit_app/
│   └── app.py
│
└── README.md

Technologies Used

Technology

Purpose

MySQL

Database management and SQL analysis

Python

Data analysis and ML

Pandas

Data manipulation

Scikit-learn

Machine learning

Joblib

Model saving/loading

Power BI

Interactive dashboards

Streamlit

Web application

Plotly

Interactive visualizations

Git & GitHub

Version control

How to Run

1. Clone the repository

git clone <repository-url>
cd HR-Analytics-System

2. Install dependencies

pip install pandas scikit-learn==1.7.2 joblib streamlit plotly

3. Run the Streamlit application

python -m streamlit run streamlit_app/app.py

The application will open in the browser.

Current Project Status

✅ Project Planning

✅ Dataset Collection

✅ Data Profiling

✅ Data Dictionary

✅ Database Design

✅ Database Created

✅ HR Dataset Imported

✅ Dataset Validation

✅ SQL / HR Analysis

✅ Department Analysis

✅ Attrition Analysis

✅ Salary Analysis

✅ Python Analysis

✅ Power BI Dashboard

✅ Machine Learning Model

✅ Model Evaluation

✅ Streamlit Application

✅ ML Prediction Integration

✅ Employee Directory

⬜ Final Documentation

⬜ Final Testing & Deployment

Future Scope

Possible future improvements include:

Improved model calibration and validation

Additional employee-level analytics

Automated model retraining

More advanced explainability for predictions

Cloud deployment

Role-based access for HR users

Integration with live HR data

Author

Vishv

B.E. Computer Engineering
CHARUSAT