# HR Analytics Database Design

## Tables

1. employees
2. departments
3. job_roles
4. education_levels
5. education_fields

## Relationships

- One Department has many Employees.
- One Job Role has many Employees.
- One Education Level has many Employees.
- One Education Field has many Employees.

## Primary Keys

employees:
- EmployeeNumber

departments:
- DepartmentID

job_roles:
- JobRoleID

education_levels:
- EducationID

education_fields:
- EducationFieldID

## Foreign Keys

employees.DepartmentID → departments.DepartmentID

employees.JobRoleID → job_roles.JobRoleID

employees.EducationID → education_levels.EducationID

employees.EducationFieldID → education_fields.EducationFieldID