class AddEmployeePage:
    """Page object for /add_employee"""
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/add_employee")

    def fill_form(self, name, email, address, city, zip_code,
                  hiring_date, job_title):
        self.page.locator('input[name="name"]').fill(name)
        self.page.locator('input[name="email"]').fill(email)
        self.page.locator('input[name="address_line1"]').fill(address)
        self.page.locator('input[name="city"]').fill(city)
        self.page.locator('input[name="zip_code"]').fill(zip_code)
        self.page.locator('input[name="hiring_date"]').fill(hiring_date)
        self.page.locator('input[name="job_title"]').fill(job_title)

    def click_add(self):
        self.page.locator("text='Add'").click()

    def create_employee(self, name, email, address, city, zip_code,
                        hiring_date, job_title):
        """Complete flow: navigate, fill, submit."""
        self.navigate()
        self.fill_form(name, email, address, city, zip_code,
                       hiring_date, job_title)
        self.click_add()
