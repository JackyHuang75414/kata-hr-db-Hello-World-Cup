class TeamsListPage:
    """Page object for /teams"""
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/teams")

    def is_team_visible(self, name):
        return self.page.locator("td").filter(has_text=name).first.is_visible()

    def count_teams_containing(self, text):
        """Count how many teams contain the given text (case-sensitive)."""
        return self.page.locator("td").filter(has_text=text).count()

    def click_delete_for_team(self, name):
        row = self.page.locator(f"tr:has(td:has-text('{name}'))")
        row.locator("text='Delete'").click()
