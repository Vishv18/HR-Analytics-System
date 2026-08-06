-- ===================================================
-- File: 07_salary_analysis.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Description: Salary Analysis
-- ===================================================

USE hr_analytics;

-- ===================================================
-- Business Question 1
-- What is the average salary by department?
-- ===================================================

SELECT
    Department,
    COUNT(*) AS TotalEmployees,
    ROUND(AVG(MonthlyIncome),2) AS AverageSalary,
    MIN(MonthlyIncome) AS MinimumSalary,
    MAX(MonthlyIncome) AS MaximumSalary
FROM employees
GROUP BY Department
ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 2
-- Which departments pay above the company average?
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
-- Rank job roles based on average salary
-- ===================================================

SELECT
    JobRole,

    ROUND(AVG(MonthlyIncome),2) AS AverageSalary,

    RANK() OVER
    (
        ORDER BY AVG(MonthlyIncome) DESC
    ) AS SalaryRank

FROM employees

GROUP BY JobRole;

-- ===================================================
-- Business Question 4
-- Rank employees based on salary
-- ===================================================

SELECT

EmployeeNumber,

Department,

JobRole,

MonthlyIncome,

RANK() OVER
(
ORDER BY MonthlyIncome DESC
) AS SalaryRank

FROM employees;

-- ===================================================
-- Business Question 5
-- Top 10 Highest Paid Employees
-- ===================================================

WITH SalaryRanking AS
(
SELECT

EmployeeNumber,

Department,

JobRole,

MonthlyIncome,

RANK() OVER
(
ORDER BY MonthlyIncome DESC
) AS SalaryRank

FROM employees
)

SELECT *

FROM SalaryRanking

WHERE SalaryRank<=10;

-- ===================================================
-- Business Question 6
-- Salary Comparison using CTE
-- ===================================================

WITH DepartmentSalary AS
(
SELECT

Department,

ROUND(AVG(MonthlyIncome),2) AS AverageSalary

FROM employees

GROUP BY Department
)

SELECT *

FROM DepartmentSalary

ORDER BY AverageSalary DESC;

-- ===================================================
-- Business Question 7
-- Salary by Education Level
-- ===================================================

SELECT

Education,

COUNT(*) AS Employees,

ROUND(AVG(MonthlyIncome),2) AS AverageSalary

FROM employees

GROUP BY Education

ORDER BY Education;

-- ===================================================
-- Business Question 8
-- Salary by Years at Company
-- ===================================================

SELECT

YearsAtCompany,

COUNT(*) AS Employees,

ROUND(AVG(MonthlyIncome),2) AS AverageSalary

FROM employees

GROUP BY YearsAtCompany

ORDER BY YearsAtCompany;

-- ===================================================
-- Business Question 9
-- Highest Paid Employee in each Department
-- ===================================================

WITH DepartmentRanking AS
(
SELECT

EmployeeNumber,

Department,

JobRole,

MonthlyIncome,

ROW_NUMBER() OVER
(
PARTITION BY Department
ORDER BY MonthlyIncome DESC
) AS RankInDepartment

FROM employees
)

SELECT *

FROM DepartmentRanking

WHERE RankInDepartment=1;

-- ===================================================
-- Business Question 10
-- Salary Distribution
-- ===================================================

SELECT

CASE

WHEN MonthlyIncome<5000 THEN 'Low Salary'

WHEN MonthlyIncome BETWEEN 5000 AND 9999
THEN 'Medium Salary'

WHEN MonthlyIncome BETWEEN 10000 AND 14999
THEN 'High Salary'

ELSE 'Very High Salary'

END AS SalaryBand,

COUNT(*) AS Employees,

ROUND(AVG(MonthlyIncome),2) AS AverageSalary

FROM employees

GROUP BY SalaryBand

ORDER BY AverageSalary;