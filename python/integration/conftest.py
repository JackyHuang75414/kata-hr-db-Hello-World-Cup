import pytest
import httpx
from urllib.parse import urljoin


@pytest.fixture(autouse=True)
def clean_database(base_url):
    """Reset the database before each integration test using the app's API."""
    url = urljoin(base_url, "reset_db")
    response = httpx.post(url, follow_redirects=True)
    response.raise_for_status()
