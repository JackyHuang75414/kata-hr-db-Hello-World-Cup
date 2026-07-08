# Test Plan — HR DB Web Application

**Application**: HR DB (Version 2026.1.0)
**URL**: `https://e.i2.hr.dmerej.info/`
**Test Type**: Manual Exploratory Testing

***

## 1. System Overview

| Module                | Page                                                                                                                                     | Actions                                                             |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Employee CRUD         | `/add_employee`, `/employees`                                                                                                            | Create, List, Edit, Delete employees                                |
| Employee Sub-features | `/employee/{id}/basic_info`, `/employee/{id}/address`, `/employee/{id}/contract`, `/employee/{id}/promote`, `/employee/{id}/add_to_team` | Edit basic info, address, contract, promote to manager, add to team |
| Team CRUD             | `/add_team`, `/teams`                                                                                                                    | Create, List, Delete teams                                          |
| Team Sub-features     | `/team/{id}/members`                                                                                                                     | View team members                                                   |
| Danger Zone           | `/reset_db`                                                                                                                              | Reset entire database                                               |

***

## 2. Test Cases

### 2.1 Teams

| ID   | Test                            | Steps                                                                    | Expected Result                                                     | Actual Result | Status |
| ---- | ------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- | ------------- | ------ |
| T-01 | Create a team (normal)          | 1. Go to `/add_team`2. Enter "Engineering"3. Click Add                   | Team created, redirected to `/teams`, "Engineering" appears in list | correct       | PASS   |
| T-02 | Create team with empty name     | 1. Go to `/add_team`2. Leave Name blank3. Click Add                      | Should show validation error, team not created                      | correct       | pass   |
| T-03 | Create team with duplicate name | 1. Create team "QA"2. Create team "QA" again                             | Should show error (duplicate name)                                  | <br />        | <br /> |
| T-04 | Case-sensitive duplicate name   | 1. Create team "qa"2. Create team "QA"                                   | Verify if case is treated as distinct or duplicate                  | <br />        | <br /> |
| T-05 | Special characters in team name | 1. Enter `<script>alert(1)</script>` as team name                        | Should be escaped or rejected                                       | <br />        | <br /> |
| T-06 | SQL Injection in team name      | 1. Enter `'; DROP TABLE hr_team; --`                                     | Should not execute SQL, must be safely handled                      | <br />        | <br /> |
| T-07 | Delete a team                   | 1. On `/teams`, click Delete for a team2. Confirm deletion               | Team removed from list                                              | <br />        | <br /> |
| T-08 | Delete a team with members      | 1. Create team "DevOps"2. Add an employee to this team3. Delete the team | Observe behavior (should warn or cascade)                           | <br />        | <br /> |
| T-09 | View team members               | 1. Click View members on a team                                          | Shows all members of that team                                      | <br />        | <br /> |

### 2.2 Employees

| ID   | Test                                        | Steps                                                                                                                 | Expected Result                                                | Actual Result | Status |
| ---- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------- | ------ |
| E-01 | Create employee (normal)                    | 1. Go to `/add_employee`2. Fill valid Name, Email, Address Line 1, City, Zip code, Hiring date, Job title3. Click Add | Employee created, appears in `/employees`                      | <br />        | <br /> |
| E-02 | All fields empty                            | 1. Go to `/add_employee`2. Leave all fields blank3. Click Add                                                         | Should show validation errors for required fields              | <br />        | <br /> |
| E-03 | Invalid email format                        | 1. Enter Email: "not-an-email"2. Fill other fields normally3. Click Add                                               | Should show validation error                                   | <br />        | <br /> |
| E-04 | Invalid zip code                            | 1. Enter Zip code: "abc" (non-numeric)2. Click Add                                                                    | Should show validation error                                   | <br />        | <br /> |
| E-05 | Future hiring date                          | 1. Enter a future date as hiring date2. Click Add                                                                     | Should be accepted or warned as unusual                        | <br />        | <br /> |
| E-06 | Very old hiring date (year 1111)            | 1. Enter hiring date "1111-11-11"                                                                                     | Should show warning or reject                                  | <br />        | <br /> |
| E-07 | SQL Injection — Name field                  | 1. Enter `admin'--` as Name                                                                                           | Must not execute SQL (KNOWN: already stored in DB! ⚠️)         | <br />        | <br /> |
| E-08 | SQL Injection — Email field                 | 1. Enter `test@test.com'; DROP TABLE hr_employee; --`                                                                 | Must not execute SQL                                           | <br />        | <br /> |
| E-09 | XSS — Name field                            | 1. Enter `<script>alert('XSS')</script>` as Name                                                                      | HTML should be escaped, no script execution                    | <br />        | <br /> |
| E-10 | XSS — Address/City fields                   | 1. Enter `<img src=x onerror=alert(1)>` in Address or City                                                            | HTML should be escaped                                         | <br />        | <br /> |
| E-11 | Edit employee basic info                    | 1. Click Edit → Update basic info2. Change Name and Email3. Click Update                                              | Changes reflected in employee list                             | <br />        | <br /> |
| E-12 | Edit employee address                       | 1. Click Update address2. Modify address fields3. Click Update                                                        | Changes saved successfully                                     | <br />        | <br /> |
| E-13 | Edit employee contract                      | 1. Click Update contract2. Modify Hiring date and Job title3. Click Update                                            | Changes saved successfully                                     | <br />        | <br /> |
| E-14 | Promote to manager                          | 1. Click Promote as manager                                                                                           | Employee's manager status becomes "yes"                        | <br />        | <br /> |
| E-15 | Demote manager (if possible)                | 1. For a manager employee, check available actions                                                                    | Observe if demotion is possible                                | <br />        | <br /> |
| E-16 | Add employee to team                        | 1. Click Add to team2. Select a team3. Click Add                                                                      | Employee appears in team's member list                         | <br />        | <br /> |
| E-17 | Delete employee                             | 1. Click Delete on an employee2. Confirm deletion                                                                     | Employee removed from list                                     | <br />        | <br /> |
| E-18 | Delete confirmation with SQL injection name | 1. Click Delete on `admin'--` employee2. Observe confirmation page                                                    | Should display correct Name and Email (KNOWN: shows blank! ⚠️) | <br />        | <br /> |
| E-19 | Display of special characters               | 1. Check how special-character names render in `/employees`                                                           | Should be properly escaped                                     | <br />        | <br /> |

### 2.3 Navigation & UI

| ID   | Test                  | Steps                                            | Expected Result                        | Actual Result | Status |
| ---- | --------------------- | ------------------------------------------------ | -------------------------------------- | ------------- | ------ |
| N-01 | Home page links       | Click every link on the Home page                | All links navigate correctly           | <br />        | <br /> |
| N-02 | 404 page              | Visit non-existent URL (e.g., `/employee/99999`) | Should return 404 or appropriate error | <br />        | <br /> |
| N-03 | Post-action redirects | After create/delete, check redirect target       | Should redirect to meaningful page     | <br />        | <br /> |

### 2.4 Reset Database

| ID   | Test                   | Steps                                   | Expected Result                                       | Actual Result | Status |
| ---- | ---------------------- | --------------------------------------- | ----------------------------------------------------- | ------------- | ------ |
| R-01 | Normal reset           | 1. Click Reset database2. Click Proceed | All data cleared, Teams and Employees lists empty     | <br />        | <br /> |
| R-02 | Operations after reset | After reset, create a team and employee | Works normally, ID may reset or continue incrementing | <br />        | <br /> |

***

## 3. Test Environment

| Item     | Value                          |
| -------- | ------------------------------ |
| Browser  | Chrome / Edge                  |
| Test URL | <https://e.i2.hr.dmerej.info/> |
| Database | PostgreSQL (remote)            |
| Group    | i2                             |
| Letter   | e                              |

***

## 4. Risks & Assumptions

- **Risk**: Multiple users share the same database — data may be modified by others
- **Risk**: Reset DB affects all tests sharing this letter
- **Assumption**: Application and database are running and in sync

