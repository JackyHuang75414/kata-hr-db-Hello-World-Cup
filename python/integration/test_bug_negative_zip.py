import httpx
from urllib.parse import urljoin
import psycopg


def test_negative_zip_code_integration(base_url: str, database_url: str):
    """Negative zip codes should be rejected with a validation error."""
    url = urljoin(base_url, "add_employee")
    response = httpx.post(url, follow_redirects=True, data={
        "name": "Bad Zip",
        "email": "badzip@test.com",
        "address_line1": "1 Error Road",
        "city": "Paris",
        "zip_code": "-75001",
        "hiring_date": "2024-06-01",
        "job_title": "Tester",
    })

    with psycopg.connect(database_url) as conn:
        rows = conn.execute("""
            SELECT b.name FROM hr_employee e
            JOIN hr_basicinfo b ON e.basic_info_id = b.id
            WHERE b.name = 'Bad Zip'
        """).fetchall()
        assert len(rows) == 0, (
            "BUG (integration): Negative zip code '-75001' was accepted. "
            "The application does not validate zip code range."
        )
