-- ===================================================
-- File: 06_attrition_analysis.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Description: Employee Attrition Analysis
-- ===================================================

USE hr_analytics;

-- ===================================================
-- Business Question 1
-- What is the overall attrition rate?
-- ===================================================

SELECT
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees;

-- ===================================================
-- Business Question 2
-- Which department has the highest attrition rate?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY Department
ORDER BY AttritionRate DESC;

-- ===================================================
-- Business Question 3
-- Which job role has the highest attrition rate?
-- ===================================================

SELECT
    JobRole,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY JobRole
ORDER BY AttritionRate DESC;

-- ===================================================
-- Business Question 4
-- Does overtime affect attrition?
-- ===================================================

SELECT
    OverTime,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY OverTime;

-- ===================================================
-- Business Question 5
-- Does marital status affect attrition?
-- ===================================================

SELECT
    MaritalStatus,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY MaritalStatus
ORDER BY AttritionRate DESC;

-- ===================================================
-- Business Question 6
-- Does gender affect attrition?
-- ===================================================

SELECT
    Gender,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY Gender;

-- ===================================================
-- Business Question 7
-- What is the average salary of employees who stayed vs left?
-- ===================================================

SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome),2) AS AverageMonthlyIncome
FROM employees
GROUP BY Attrition;

-- ===================================================
-- Business Question 8
-- How many years do employees stay before leaving?
-- ===================================================

SELECT
    Attrition,
    ROUND(AVG(YearsAtCompany),2) AS AverageYearsAtCompany
FROM employees
GROUP BY Attrition;

-- ===================================================
-- Business Question 9
-- Does job satisfaction affect attrition?
-- ===================================================

SELECT
    JobSatisfaction,
    COUNT(*) AS TotalEmployees,
    SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS EmployeesLeft,
    ROUND(
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
        COUNT(*),
        2
    ) AS AttritionRate
FROM employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;