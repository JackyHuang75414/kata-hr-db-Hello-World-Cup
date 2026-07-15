class EmployeesListPage:
    """Page object for /employees"""
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/employees")

    def is_employee_visible(self, name):
        return self.page.locator("td").filter(has_text=name).first.is_visible()

    def click_delete(self):
        """Click the first Delete link on the page."""
        self.page.locator("text='Delete'").first.click()
