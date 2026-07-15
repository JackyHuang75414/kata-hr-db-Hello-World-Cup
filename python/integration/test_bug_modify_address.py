import httpx
from urllib.parse import urljoin
import psycopg


def test_modify_address_line2_integration(base_url: str, database_url: str):
    """BUG: Modifying address line 2 should persist in the database."""
    # Create an employee
    add_url = urljoin(base_url, "add_employee")
    httpx.post(add_url, follow_redirects=True, data={
        "name": "Address Tester",
        "email": "addr2@test.com",
        "address_line1": "10 Main St",
        "city": "Lyon",
        "zip_code": "69001",
        "hiring_date": "2024-02-01",
        "job_title": "QA",
    })

    # Get the employee ID
    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT e.id FROM hr_employee e
            JOIN hr_basicinfo b ON e.basic_info_id = b.id
            WHERE b.name = 'Address Tester'
        """).fetchall()
        employee_id = rows[0][0]

    # Update address line 2
    address_url = urljoin(base_url, f"employee/{employee_id}/address")
    httpx.post(address_url, follow_redirects=True, data={
        "address_line1": "10 Main St",
        "address_line2": "Apt 42",
        "city": "Lyon",
        "zip_code": "69001",
    })

    # Check that address_line2 was saved
    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT a.address_line2 FROM hr_employee e
            JOIN hr_address a ON e.address_id = a.id
            WHERE e.id = %s
        """, (employee_id,)).fetchall()
        assert len(rows) == 1, "Employee not found"
        actual_line2 = rows[0][0] or ""
        assert actual_line2 == "Apt 42", (
            f"BUG: Address line 2 was not updated in database. "
            f"Expected 'Apt 42', got '{actual_line2}'."
        )
