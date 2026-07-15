class AddTeamPage:
    """Page object for /add_team"""
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[name="name"]')
        self.add_button = page.locator("text='Add'")

    def navigate(self):
        self.page.goto("/add_team")

    def fill_name(self, name):
        self.name_input.fill(name)

    def click_add(self):
        self.add_button.click()

    def create_team(self, name):
        """Complete flow: navigate, fill, submit."""
        self.navigate()
        self.fill_name(name)
        self.click_add()
