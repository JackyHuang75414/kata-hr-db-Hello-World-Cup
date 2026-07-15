import pytest


@pytest.fixture(autouse=True)
def reset_db(page):
    """Reset the database before each E2E test to ensure clean state."""
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()
