-- ===================================================
-- File: 07_salary_analysis.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Author: Vishv Undavia
-- Description: Salary Analysis
-- ===================================================

USE hr_analytics;

-- ===================================================
-- Business Question 1
-- What is the average salary in each department?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 2
-- Which departments pay above the company average salary?
-- ===================================================

SELECT
    Department,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY Department
HAVING AVG(MonthlyIncome) >
(
    SELECT AVG(MonthlyIncome)
    FROM employees
)
ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 3
-- Which job roles have the highest average salary?
-- ===================================================

SELECT
    JobRole,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY JobRole
ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 4
-- Does education level affect salary?
-- ===================================================

SELECT
    Education,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY Education
ORDER BY Education;

-- ===================================================
-- Business Question 5
-- Does experience affect salary?
-- ===================================================

SELECT
    YearsAtCompany,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary
FROM employees
GROUP BY YearsAtCompany
ORDER BY YearsAtCompany;

-- ===================================================
-- Business Question 6
-- Top 10 Highest Paid Employees
-- ===================================================

SELECT
    EmployeeNumber,
    JobRole,
    Department,
    MonthlyIncome
FROM employees
ORDER BY MonthlyIncome DESC
LIMIT 10;