import httpx
from urllib.parse import urljoin
import psycopg


def test_invalid_hiring_date_integration(base_url: str, database_url: str):
    """BUG-005: Unreasonable hiring dates should be rejected."""
    url = urljoin(base_url, "add_employee")
    response = httpx.post(url, follow_redirects=True, data={
        "name": "Medieval Worker",
        "email": "medieval@test.com",
        "address_line1": "1 Old Road",
        "city": "Constantinople",
        "zip_code": "00001",
        "hiring_date": "1111-11-11",
        "job_title": "Blacksmith",
    })

    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT b.name FROM hr_employee e
            JOIN hr_basicinfo b ON e.basic_info_id = b.id
            WHERE b.name = 'Medieval Worker'
        """).fetchall()
        assert len(rows) == 0, (
            "BUG-005 (integration): Employee with hiring date year 1111 "
            "was stored in database. Date validation is missing."
        )
