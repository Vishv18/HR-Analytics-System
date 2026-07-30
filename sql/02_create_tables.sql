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