import httpx
from urllib.parse import urljoin
import psycopg


def test_team_case_insensitive_duplicate_integration(
    base_url: str, database_url: str
):
    """BUG-006: Team names should be case-insensitive unique."""
    url = urljoin(base_url, "add_team")

    # Create first team
    httpx.post(url, follow_redirects=True, data={"name": "Engineering"})
    # Try to create same name with different case
    httpx.post(url, follow_redirects=True, data={"name": "engineering"})

    with psycopg.connect(database_url) as conn:
        rows = conn.execute(
            "SELECT name FROM hr_team WHERE LOWER(name) = 'engineering'"
        ).fetchall()
        assert len(rows) == 1, (
            f"BUG-006 (integration): Found {len(rows)} teams with name "
            "'engineering' (case-insensitive). Team names should be unique "
            "regardless of case."
        )
