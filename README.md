# HR Analytics & Workforce Intelligence System

A data analytics and machine learning project for analyzing employee attrition, workforce patterns, and employee-level attrition risk.

The system combines **MySQL, Python, Power BI, Machine Learning, and Streamlit** into one end-to-end HR analytics workflow.

---

## 📌 Project Overview

Employee attrition can affect workforce stability and increase recruitment and training costs.

This project analyzes historical HR employee data to identify workforce and attrition patterns and provides a **machine-learning-based estimate of attrition risk for individual employees**.

The project is organized into four main layers:

* **MySQL** — database storage and SQL analysis
* **Python** — data analysis and machine learning
* **Power BI** — interactive business intelligence dashboards
* **Streamlit** — application interface connecting analytics and ML prediction

### Project Workflow

```text
HR Employee Dataset
        │
        ▼
     MySQL
        │
        ├──────────────► SQL Analysis
        │
        ▼
     Python
        │
        ├──────────────► Exploratory Data Analysis
        │
        └──────────────► Machine Learning
                              │
                              ▼
                    Attrition Prediction Model
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
             Power BI                  Streamlit
          HR Analytics              Interactive App
```

---

# 📊 Dataset

The project uses an HR employee attrition dataset containing:

* **1,470 employee records**
* **35 original attributes**
* Employee demographics
* Department and job information
* Compensation
* Job satisfaction
* Work-life balance
* Overtime
* Business travel
* Years at company
* Attrition status

The target variable for machine learning is:

```text
Attrition → Yes / No
```

Where:

* **Yes** = Employee left the organization
* **No** = Employee stayed with the organization

---

# 🎯 Project Objectives

The main objectives of the project are to:

1. Store and manage HR employee data using a structured MySQL database.
2. Analyze workforce distribution and employee attrition using SQL.
3. Identify important workforce and attrition patterns through exploratory analysis.
4. Build interactive HR dashboards using Power BI.
5. Train and evaluate machine learning models for employee attrition prediction.
6. Provide employee-level model-estimated attrition risk through a Streamlit application.
7. Bring the analytics and prediction components together into one system.

---

# 🗄️ 1. HR Database

The HR dataset is stored in a MySQL database named:

```text
hr_analytics
```

The database includes lookup tables such as:

* `departments`
* `job_roles`
* `education_fields`

and the main:

* `employees`

The database design is intended to reduce redundancy and maintain consistent employee-related information.

---

# 🔎 2. SQL Analysis

SQL is used to analyze workforce and employee-level patterns.

The analysis covers areas such as:

* Workforce distribution
* Department-wise employee counts
* Employee attrition
* Salary patterns
* Employee characteristics
* Workforce retention questions
* Department and job-related patterns

The SQL analysis provides the foundation for understanding the dataset before moving into visualization and machine learning.

---

# 📈 3. Power BI Dashboard

The Power BI dashboard provides interactive HR analytics through three main pages.

### Executive Overview

Provides a high-level view of:

* Total employees
* Employees who left
* Attrition rate
* Workforce indicators
* Compensation indicators

### Attrition Analysis

Explores factors associated with employee attrition, including:

* Department
* Age
* Overtime
* Monthly income
* Other employee characteristics

### HR Insights / Workforce

Provides additional workforce-level analysis and employee insights.

Power BI is primarily used for **historical and descriptive HR analytics**, while the machine learning component focuses on employee-level attrition prediction.

---

# 🤖 4. Machine Learning — Attrition Prediction

The machine learning component treats employee attrition prediction as a **binary classification problem**.

Multiple classification models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Balanced Random Forest

The final prediction pipeline uses a **Balanced Random Forest** to address the class imbalance between employees who stayed and employees who left.

## Selected Features

The final model uses 10 employee attributes:

1. Age
2. Department
3. Job Role
4. Monthly Income
5. Job Level
6. Overtime
7. Job Satisfaction
8. Work-Life Balance
9. Years at Company
10. Business Travel

---

## ⚙️ Machine Learning Workflow

```text
HR Dataset
     │
     ▼
Feature Selection
     │
     ▼
Train / Test Split
     │
     ▼
Data Preprocessing
     │
     ▼
Model Training
     │
     ├── Logistic Regression
     ├── Decision Tree
     ├── Random Forest
     └── Balanced Random Forest
     │
     ▼
Model Evaluation
     │
     ▼
Final Balanced Random Forest
     │
     ▼
Saved Model Pipeline
     │
     ▼
Streamlit Prediction
```

---

## 📏 Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion Matrix

### Final Test-Set Results

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 80.61% |
| Precision | 41.67% |
| Recall    | 53.19% |
| F1-score  | 46.73% |
| ROC-AUC   | 74.76% |

These results represent the performance of the final model on the held-out test set.

The model produces a **model-estimated attrition risk**, not a guaranteed prediction of an employee's future behavior.

---

# 🖥️ 5. Streamlit Application

The Streamlit application brings the project's analytics and machine learning components together into an interactive interface.

### Current Sections

* **Overview**
* **Analytics & Power BI**
* **Risk Prediction**
* **Employee Directory**
* **About System**

---

## 🔮 Risk Prediction

Users can enter employee information and receive:

* Predicted attrition status
* Model-estimated attrition risk
* Risk classification
* Basic recommendations based on employee characteristics

The prediction is generated using the final trained machine learning pipeline.

---

## 👤 Employee Directory

An employee can be searched using their Employee ID.

The system displays information such as:

* Employee profile information
* Actual attrition status
* Model-estimated attrition risk
* Relevant employee metrics

---

# 🧩 Technology Stack

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| **MySQL**        | Database management and SQL analysis |
| **Python**       | Data analysis and machine learning   |
| **Pandas**       | Data manipulation                    |
| **NumPy**        | Numerical operations                 |
| **Scikit-learn** | Machine learning                     |
| **Joblib**       | Model saving and loading             |
| **Power BI**     | Interactive HR dashboards            |
| **Streamlit**    | Interactive web application          |
| **Plotly**       | Interactive visualizations           |
| **Matplotlib**   | Data visualization                   |
| **Seaborn**      | Statistical visualization            |
| **Git & GitHub** | Version control                      |

---

# 📁 Project Structure

```text
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
│   └── ...
│
├── notebooks/
│   └── 01_ml_model.ipynb
│
├── python/
│   ├── attrition_model.pkl
│   └── predict.py
│
├── reports/
│   └── ...
│
├── screenshots/
│   └── ...
│
├── sql/
│   ├── database setup
│   ├── data validation
│   └── analysis queries
│
├── streamlit_app/
│   └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone <repository-url>
cd HR-Analytics-System
```

Replace `<repository-url>` with the URL of your GitHub repository.

---

## 2. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

## 3. Run the Streamlit Application

From the project root:

```bash
python -m streamlit run streamlit_app/app.py
```

The application will open in your browser.

If it does not open automatically, use the local URL shown in the terminal, normally:

```text
http://localhost:8501
```

---

# 🧪 Project Status

### Completed

* ✅ Project Planning
* ✅ Dataset Collection
* ✅ Data Profiling
* ✅ Data Dictionary
* ✅ Database Design
* ✅ Database Creation
* ✅ HR Dataset Import
* ✅ Dataset Validation
* ✅ SQL / HR Analysis
* ✅ Department Analysis
* ✅ Attrition Analysis
* ✅ Salary Analysis
* ✅ Python Analysis
* ✅ Power BI Dashboard
* ✅ Machine Learning Model
* ✅ Model Evaluation
* ✅ Streamlit Application
* ✅ ML Prediction Integration
* ✅ Employee Directory
* ✅ Final ML Notebook
* ✅ Project Dependencies
* ✅ Git Repository Cleanup

### Remaining

* ⬜ Final Documentation Review
* ⬜ Final Testing
* ⬜ Deployment

---

# ⚠️ Limitations

The current system has several limitations:

* The model is trained on a historical HR dataset and may not generalize to other organizations.
* Model-estimated risk should not be treated as a guaranteed outcome.
* The current dataset represents a fixed historical snapshot rather than continuously updated HR data.
* Model performance may change when applied to a different workforce or organizational environment.
* Further model calibration and validation could improve the reliability of predicted probabilities.

The prediction system should therefore be used as an **analytical support tool**, not as an automated decision-making system for employees.

---

# 🔮 Future Scope

Possible future improvements include:

* Improved model calibration and validation
* Additional employee-level analytics
* Automated model retraining
* More advanced model explainability
* Cloud deployment
* Role-based access for HR users
* Integration with live HR data
* Continuous monitoring of model performance

---

# 👨‍💻 Author

**Vishv Undavia**

Aspiring Data Analyst

---

## 📌 Key Takeaway

This project demonstrates an end-to-end data analytics workflow that combines:

```text
Database
   ↓
SQL Analysis
   ↓
Exploratory Data Analysis
   ↓
Power BI
   ↓
Machine Learning
   ↓
Streamlit Application
```

The goal is to demonstrate how HR data can be transformed from raw employee records into **business insights and model-estimated employee attrition risk** through a complete analytics workflow.
