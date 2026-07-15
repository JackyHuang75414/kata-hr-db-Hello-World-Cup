from pages import AddEmployeePage, EmployeesListPage


def test_negative_zip_code_rejected(page):
    """Negative zip codes should be rejected with a validation error."""
    add_employee = AddEmployeePage(page)
    employees_list = EmployeesListPage(page)

    add_employee.create_employee(
        name="Bad Zip Worker",
        email="badzip@test.com",
        address="1 Error Road",
        city="Paris",
        zip_code="-75001",
        hiring_date="2024-06-01",
        job_title="Tester",
    )

    employees_list.navigate()
    assert not employees_list.is_employee_visible("Bad Zip Worker"), (
        "BUG: Negative zip code '-75001' was accepted. "
        "The application does not validate zip code range."
    )
