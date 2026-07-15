from pages import AddEmployeePage, EmployeesListPage


def test_invalid_hiring_date_rejected(page):
    """BUG-005: Unreasonable hiring dates should be rejected."""
    add_employee = AddEmployeePage(page)
    employees_list = EmployeesListPage(page)

    add_employee.create_employee(
        name="Medieval Worker",
        email="medieval@test.com",
        address="1 Old Road",
        city="Constantinople",
        zip_code="00001",
        hiring_date="1111-11-11",
        job_title="Blacksmith",
    )

    employees_list.navigate()
    assert not employees_list.is_employee_visible("Medieval Worker"), (
        "BUG-005: Hiring date '1111-11-11' (year 1111) was accepted. "
        "The application does not validate that hiring dates are within "
        "a reasonable range."
    )
