-- ===================================================
-- File: 03_data_validation.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Description: Initial dataset validation
-- ===================================================

USE hr_analytics;

-- Total Employees
SELECT COUNT(*) AS TotalEmployees
FROM employees;

-- View first 10 records
SELECT *
FROM employees
LIMIT 10;

-- Check Attrition values
SELECT DISTINCT Attrition
FROM employees;

-- Check Departments
SELECT DISTINCT Department
FROM employees;

-- Check Job Roles
SELECT DISTINCT JobRole
FROM employees;

-- Check Gender
SELECT DISTINCT Gender
FROM employees;

-- Check Marital Status
SELECT DISTINCT MaritalStatus
FROM employees;

-- Check Business Travel
SELECT DISTINCT BusinessTravel
FROM employees;

-- Check Education Field
SELECT DISTINCT EducationField
FROM employees;