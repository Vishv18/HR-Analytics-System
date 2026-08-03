-- ===================================================
-- File: 05_department_analysis.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Author: Vishv Undavia
-- Description: Department-wise Workforce Analysis
-- ===================================================

USE hr_analytics;

-- ===================================================
-- Business Question 1
-- How many employees are in each department?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS TotalEmployees
FROM employees
GROUP BY Department
ORDER BY TotalEmployees DESC;

-- ===================================================
-- Business Question 2
-- What is the average monthly income in each department?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 3
-- What is the average age in each department?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(Age),2) AS AverageAge
FROM employees
GROUP BY Department;

-- ===================================================
-- Business Question 4
-- What is the average experience (YearsAtCompany)?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(YearsAtCompany),2) AS AverageYearsAtCompany
FROM employees
GROUP BY Department
ORDER BY AverageYearsAtCompany DESC;

-- ===================================================
-- Business Question 5
-- What is the average job satisfaction?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(JobSatisfaction),2) AS AverageJobSatisfaction
FROM employees
GROUP BY Department
ORDER BY AverageJobSatisfaction DESC;

-- ===================================================
-- Business Question 6
-- How many employees work overtime in each department?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS EmployeesWorkingOvertime
FROM employees
WHERE OverTime = 'Yes'
GROUP BY Department
ORDER BY EmployeesWorkingOvertime DESC;

-- ===================================================
-- Business Question 7
-- How many employees left each department?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS EmployeesLeft
FROM employees
WHERE Attrition = 'Yes'
GROUP BY Department
ORDER BY EmployeesLeft DESC;

-- ===================================================
-- Business Question 8
-- What is the attrition rate in each department?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY Department
ORDER BY AttritionRate DESC;