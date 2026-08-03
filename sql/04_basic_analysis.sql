-- ===================================================
-- File: 04_basic_analysis.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Author: Vishv Undavia
-- Description: Basic Workforce Analysis
-- ===================================================

USE hr_analytics;

-- ===================================================
-- Business Question 1
-- How many employees are there?
-- ===================================================

SELECT
COUNT(*) AS TotalEmployees
FROM employees;

-- ===================================================
-- Business Question 2
-- What is the average age of employees?
-- ===================================================

SELECT
ROUND(AVG(Age),2) AS AverageAge
FROM employees;

-- ===================================================
-- Business Question 3
-- What is the youngest and oldest employee age?
-- ===================================================

SELECT
MIN(Age) AS YoungestEmployee,
MAX(Age) AS OldestEmployee
FROM employees;

-- ===================================================
-- Business Question 4
-- What is the average monthly income?
-- ===================================================

SELECT
ROUND(AVG(MonthlyIncome),2) AS AverageMonthlyIncome
FROM employees;

-- ===================================================
-- Business Question 5
-- What is the minimum and maximum salary?
-- ===================================================

SELECT
MIN(MonthlyIncome) AS LowestSalary,
MAX(MonthlyIncome) AS HighestSalary
FROM employees;

-- ===================================================
-- Business Question 6
-- How many employees are there in each department?
-- ===================================================

SELECT
Department,
COUNT(*) AS TotalEmployees
FROM employees
GROUP BY Department
ORDER BY TotalEmployees DESC;

-- ===================================================
-- Business Question 7
-- How many employees belong to each job role?
-- ===================================================

SELECT
JobRole,
COUNT(*) AS TotalEmployees
FROM employees
GROUP BY JobRole
ORDER BY TotalEmployees DESC;

-- ===================================================
-- Business Question 8
-- What is the average years at company?
-- ===================================================

SELECT
ROUND(AVG(YearsAtCompany),2) AS AverageYearsAtCompany
FROM employees;

-- ===================================================
-- Business Question 9
-- How many employees work overtime?
-- ===================================================

SELECT
OverTime,
COUNT(*) AS TotalEmployees
FROM employees
GROUP BY OverTime;

-- ===================================================
-- Business Question 10
-- How many employees travel for business?
-- ===================================================

SELECT
BusinessTravel,
COUNT(*) AS TotalEmployees
FROM employees
GROUP BY BusinessTravel
ORDER BY TotalEmployees DESC;