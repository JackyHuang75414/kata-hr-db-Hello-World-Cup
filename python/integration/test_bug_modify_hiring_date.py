import httpx
from urllib.parse import urljoin
import psycopg


def test_modify_hiring_date_integration(base_url: str, database_url: str):
    """BUG: Modifying hiring date should persist in the database."""
    # Create an employee
    add_url = urljoin(base_url, "add_employee")
    httpx.post(add_url, follow_redirects=True, data={
        "name": "Date Changer",
        "email": "datechange@test.com",
        "address_line1": "1 Test Road",
        "city": "Paris",
        "zip_code": "75001",
        "hiring_date": "2024-01-01",
        "job_title": "Dev",
    })

    # Get the employee ID from the database
    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT e.id FROM hr_employee e
            JOIN hr_basicinfo b ON e.basic_info_id = b.id
            WHERE b.name = 'Date Changer'
        """).fetchall()
        employee_id = rows[0][0]

    # Update the hiring date to a new value
    contract_url = urljoin(base_url, f"employee/{employee_id}/contract")
    httpx.post(contract_url, follow_redirects=True, data={
        "hiring_date": "2025-06-15",
        "job_title": "Dev",
    })

    # Check that the hiring date was updated
    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT c.hiring_date FROM hr_employee e
            JOIN hr_contract c ON e.contract_id = c.id
            WHERE e.id = %s
        """, (employee_id,)).fetchall()
        assert len(rows) == 1, "Employee not found"
        actual_date = str(rows[0][0])
        assert actual_date == "2025-06-15", (
            f"BUG: Hiring date was not updated in database. "
            f"Expected '2025-06-15', got '{actual_date}'."
        )
