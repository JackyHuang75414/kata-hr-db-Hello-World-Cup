# Bug Tracker — HR DB Web Application

**Application**: HR DB (Version 2026.1.0)
**URL**: `https://e.i2.hr.dmerej.info/`

---

## Bug Summary

| ID | Severity | Category | Title | Status |
|----|----------|----------|-------|--------|
| BUG-001 | Critical | Security | SQL Injection — Employee Name field accepts raw SQL payload | Open |
| BUG-002 | Critical | Security | SQL Injection — Other input fields may have the same vulnerability | Open |
| BUG-003 | High | Security | XSS — Name field may not escape HTML (to be verified) | Open |
| BUG-004 | High | Functional | Delete employee confirmation page shows blank Name/Email for SQL-injected records | Open |
| BUG-005 | Medium | Validation | Hiring Date accepts unreasonable years (e.g. year 1111) | Open |
| BUG-006 | Medium | Functional | Team name case-insensitive duplicate — "a" and "A" both exist | Open |
| BUG-007 | Medium | Validation | Blank team name may be accepted (to be verified) | Open |
| BUG-008 | Low | Functional | Edit Employee address page may be missing Address Line 2 field | Open |

---

## Detailed Descriptions

### BUG-001 — SQL Injection in Employee Name

- **Severity**: Critical
- **Category**: Security
- **Steps to Reproduce**:
  1. Go to `/add_employee`
  2. Enter `admin'--` in the Name field
  3. Fill other fields with any valid data
  4. Click Add
- **Expected Result**: Input should be rejected or escaped; raw SQL payload should never be stored
- **Actual Result**: Successfully written to database. Employees named `admin'--` and `'; DROP TABLE users; --` are visible in the employee list
- **Impact**: Attacker can execute arbitrary SQL commands — potential data leak, modification, or deletion
- **Status**: Open

### BUG-002 — SQL Injection in Other Fields

- **Severity**: Critical
- **Category**: Security
- **Steps to Reproduce**: Test SQL injection payloads in all text input fields (Email, Address, City, Job Title, Team Name)
- **Expected Result**: All fields should be protected against SQL injection
- **Actual Result**: Name field confirmed vulnerable; other fields pending testing
- **Status**: Open

### BUG-003 — XSS in Name Field

- **Severity**: High
- **Category**: Security
- **Steps to Reproduce**:
  1. Go to `/add_employee`
  2. Enter `<script>alert('XSS')</script>` in the Name field
  3. After creation, check the `/employees` listing
- **Expected Result**: HTML tags should be escaped, displayed as plain text
- **Actual Result**: Pending testing
- **Status**: Open

### BUG-004 — Delete Confirmation Shows Empty Info

- **Severity**: High
- **Category**: Functional / Display
- **Steps to Reproduce**:
  1. Go to `/employees`
  2. Click Delete on the employee named `admin'--`
  3. Observe the confirmation page
- **Expected Result**: The employee's Name and Email should be displayed
- **Actual Result**: Name and Email fields appear blank
- **Likely Cause**: The single quote in the SQL injection payload breaks HTML rendering
- **Status**: Open

### BUG-005 — Invalid Hiring Date Accepted

- **Severity**: Medium
- **Category**: Validation
- **Steps to Reproduce**:
  1. Go to `/add_employee`
  2. Enter `1111-11-11` as the hiring date
  3. Click Add
- **Expected Result**: Unreasonable year should be rejected with a validation message
- **Actual Result**: Successfully stored, detail page shows "Hired on Nov. 11, 1111"
- **Status**: Open

### BUG-006 — Team Name Case Sensitivity Issue

- **Severity**: Medium
- **Category**: Functional
- **Steps to Reproduce**:
  1. Create a team named "a"
  2. Create another team named "A"
- **Expected Result**: Team names should be case-insensitive unique; second creation should fail
- **Actual Result**: Both "a" and "A" exist simultaneously
- **Status**: Open

### BUG-007 — Blank Team Name Accepted

- **Severity**: Medium
- **Category**: Validation
- **Steps to Reproduce**:
  1. Go to `/add_team`
  2. Leave the Name field blank
  3. Click Add
- **Expected Result**: Validation error message should appear
- **Actual Result**: Pending testing
- **Status**: Open

### BUG-008 — Missing Address Line 2 in Edit

- **Severity**: Low
- **Category**: Functional
- **Steps to Reproduce**:
  1. Edit an employee's address
  2. Observe the form fields
- **Expected Result**: Should include Address Line 2 field (matching `address_line2` in database schema)
- **Actual Result**: Pending testing
- **Status**: Open
