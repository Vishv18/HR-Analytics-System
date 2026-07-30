-- =========================================================
-- File: 02_create_tables.sql
-- Project: HR Analytics & Employee Attrition Prediction System
-- Description: Creates all lookup tables
-- =========================================================

USE hr_analytics;

-- ======================================
-- Table: departments
-- ======================================

CREATE TABLE departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(50) NOT NULL UNIQUE
);

-- ======================================
-- Table: job_roles
-- ======================================

CREATE TABLE job_roles (
    JobRoleID INT AUTO_INCREMENT PRIMARY KEY,
    JobRoleName VARCHAR(100) NOT NULL UNIQUE
);

-- ======================================
-- Table: education_fields
-- ======================================

CREATE TABLE education_fields (
    EducationFieldID INT AUTO_INCREMENT PRIMARY KEY,
    EducationFieldName VARCHAR(100) NOT NULL UNIQUE
);

-- ======================================
-- Table: employees
-- ======================================

CREATE TABLE employees (

    EmployeeNumber INT PRIMARY KEY,

    Age TINYINT UNSIGNED NOT NULL,

    Attrition VARCHAR(3),

    BusinessTravel VARCHAR(30),

    DailyRate INT,

    DepartmentID INT,

    DistanceFromHome TINYINT UNSIGNED,

    Education TINYINT UNSIGNED,

    EducationFieldID INT,

    EnvironmentSatisfaction TINYINT UNSIGNED,

    Gender VARCHAR(10),

    HourlyRate INT,

    JobInvolvement TINYINT UNSIGNED,

    JobLevel TINYINT UNSIGNED,

    JobRoleID INT,

    JobSatisfaction TINYINT UNSIGNED,

    MaritalStatus VARCHAR(20),

    MonthlyIncome INT,

    MonthlyRate INT,

    NumCompaniesWorked TINYINT UNSIGNED,

    OverTime VARCHAR(5),

    PercentSalaryHike TINYINT UNSIGNED,

    PerformanceRating TINYINT UNSIGNED,

    RelationshipSatisfaction TINYINT UNSIGNED,

    StockOptionLevel TINYINT UNSIGNED,

    TotalWorkingYears TINYINT UNSIGNED,

    TrainingTimesLastYear TINYINT UNSIGNED,

    WorkLifeBalance TINYINT UNSIGNED,

    YearsAtCompany TINYINT UNSIGNED,

    YearsInCurrentRole TINYINT UNSIGNED,

    YearsSinceLastPromotion TINYINT UNSIGNED,

    YearsWithCurrManager TINYINT UNSIGNED,

    FOREIGN KEY (DepartmentID)
        REFERENCES departments(DepartmentID),

    FOREIGN KEY (JobRoleID)
        REFERENCES job_roles(JobRoleID),

    FOREIGN KEY (EducationFieldID)
        REFERENCES education_fields(EducationFieldID)

);