import httpx
from urllib.parse import urljoin
import psycopg


def test_duplicate_employee_integration(base_url: str, database_url: str):
    """Creating an employee with the same info should be rejected."""
    url = urljoin(base_url, "add_employee")
    data = {
        "name": "John Smith",
        "email": "john@test.com",
        "address_line1": "1 Main St",
        "city": "Paris",
        "zip_code": "75001",
        "hiring_date": "2024-03-15",
        "job_title": "Analyst",
    }

    # Create the employee twice
    httpx.post(url, follow_redirects=True, data=data)
    httpx.post(url, follow_redirects=True, data=data)

    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT b.name FROM hr_employee e
            JOIN hr_basicinfo b ON e.basic_info_id = b.id
            WHERE b.name = 'John Smith'
        """).fetchall()
        assert len(rows) == 1, (
            f"BUG (integration): Found {len(rows)} employees with name "
            "'John Smith'. Duplicate employees should be rejected."
        )
