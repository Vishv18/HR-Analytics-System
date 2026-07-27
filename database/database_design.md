# HR Analytics Database Design

## Database Name
hr_analytics

## Tables

### 1. employees
Stores employee information.

Primary Key:
- EmployeeNumber

Foreign Keys:
- DepartmentID
- JobRoleID
- EducationID
- EducationFieldID
- TravelID

---

### 2. departments

Stores department information.

Primary Key:
- DepartmentID

---

### 3. job_roles

Stores employee job roles.

Primary Key:
- JobRoleID

---

### 4. education_levels

Stores employee education levels.

Primary Key:
- EducationID

---

### 5. education_fields

Stores employee education fields.

Primary Key:
- EducationFieldID

---

### 6. business_travel

Stores employee travel frequency.

Primary Key:
- TravelID

---

## Relationships

Department → Employees (1:M)

Job Role → Employees (1:M)

Education Level → Employees (1:M)

Education Field → Employees (1:M)

Business Travel → Employees (1:M)