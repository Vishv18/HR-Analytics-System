-- ===================================================
-- File: 02_create_tables.sql
-- Project: HR Analytics & Employee Attrition Prediction
-- Description: Creates Employees Table
-- ===================================================

USE hr_analytics;

CREATE TABLE employees (

EmployeeNumber INT PRIMARY KEY,

Age INT,

Attrition VARCHAR(5),

BusinessTravel VARCHAR(30),

DailyRate INT,

Department VARCHAR(50),

DistanceFromHome INT,

Education INT,

EducationField VARCHAR(50),

EmployeeCount INT,

EnvironmentSatisfaction INT,

Gender VARCHAR(10),

HourlyRate INT,

JobInvolvement INT,

JobLevel INT,

JobRole VARCHAR(100),

JobSatisfaction INT,

MaritalStatus VARCHAR(20),

MonthlyIncome INT,

MonthlyRate INT,

NumCompaniesWorked INT,

Over18 VARCHAR(5),

OverTime VARCHAR(5),

PercentSalaryHike INT,

PerformanceRating INT,

RelationshipSatisfaction INT,

StandardHours INT,

StockOptionLevel INT,

TotalWorkingYears INT,

TrainingTimesLastYear INT,

WorkLifeBalance INT,

YearsAtCompany INT,

YearsInCurrentRole INT,

YearsSinceLastPromotion INT,

YearsWithCurrManager INT

);