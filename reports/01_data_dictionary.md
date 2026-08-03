# Data Dictionary

## Project
**HR Analytics and Employee Attrition Prediction System**

---

## Purpose

This document describes the attributes (columns) present in the IBM HR Analytics dataset. It provides the meaning, data type, category, and whether each attribute will be used in the project.

---

| Column Name | Description | Data Type | Category | Status |
|--------------|-------------|-----------|----------|--------|
| Age | Age of the employee | INT | Numerical | Keep |
| Attrition | Whether the employee left the company (Yes/No) | VARCHAR | Target Variable | Keep |
| BusinessTravel | Frequency of business travel | VARCHAR | Categorical | Keep |
| DailyRate | Daily salary rate | INT | Numerical | Keep |
| Department | Employee's department | VARCHAR | Categorical | Keep |
| DistanceFromHome | Distance between home and workplace | INT | Numerical | Keep |
| Education | Education level (1–5) | INT | Ordinal | Keep |
| EducationField | Employee's education field | VARCHAR | Categorical | Keep |
| EmployeeCount | Constant value (1) | INT | Constant | Remove |
| EmployeeNumber | Unique employee identifier | INT | Identifier | Keep |
| EnvironmentSatisfaction | Satisfaction with work environment (1–4) | INT | Ordinal | Keep |
| Gender | Gender of employee | VARCHAR | Categorical | Keep |
| HourlyRate | Hourly salary rate | INT | Numerical | Keep |
| JobInvolvement | Employee involvement level (1–4) | INT | Ordinal | Keep |
| JobLevel | Job level | INT | Ordinal | Keep |
| JobRole | Employee job role | VARCHAR | Categorical | Keep |
| JobSatisfaction | Job satisfaction level (1–4) | INT | Ordinal | Keep |
| MaritalStatus | Marital status | VARCHAR | Categorical | Keep |
| MonthlyIncome | Monthly salary | INT | Numerical | Keep |
| MonthlyRate | Monthly salary rate | INT | Numerical | Keep |
| NumCompaniesWorked | Number of companies worked | INT | Numerical | Keep |
| Over18 | Indicates whether employee is over 18 (Always "Y") | VARCHAR | Constant | Remove |
| OverTime | Whether employee works overtime | VARCHAR | Categorical | Keep |
| PercentSalaryHike | Percentage salary increase | INT | Numerical | Keep |
| PerformanceRating | Employee performance rating | INT | Ordinal | Keep |
| RelationshipSatisfaction | Satisfaction with coworkers | INT | Ordinal | Keep |
| StandardHours | Standard working hours (Always 80) | INT | Constant | Remove |
| StockOptionLevel | Employee stock option level | INT | Ordinal | Keep |
| TotalWorkingYears | Total years of work experience | INT | Numerical | Keep |
| TrainingTimesLastYear | Number of training sessions attended | INT | Numerical | Keep |
| WorkLifeBalance | Work-life balance rating | INT | Ordinal | Keep |
| YearsAtCompany | Years worked in current company | INT | Numerical | Keep |
| YearsInCurrentRole | Years in current role | INT | Numerical | Keep |
| YearsSinceLastPromotion | Years since last promotion | INT | Numerical | Keep |
| YearsWithCurrManager | Years with current manager | INT | Numerical | Keep |

---

## Summary

- Total Columns: **35**
- Useful Columns: **32**
- Constant Columns Removed:
  - EmployeeCount
  - Over18
  - StandardHours

These three columns contain the same value for every employee and therefore do not contribute to data analysis or predictive modeling.