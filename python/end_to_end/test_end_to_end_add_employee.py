from pages import AddEmployeePage, EmployeesListPage


def test_create_employee(page):
    add_employee = AddEmployeePage(page)
    employees_list = EmployeesListPage(page)

    add_employee.create_employee(
        name="Alice",
        email="alice@example.com",
        address="1 Rue de Paris",
        city="Paris",
        zip_code="75001",
        hiring_date="2024-06-01",
        job_title="Engineer",
    )
    employees_list.navigate()
    assert employees_list.is_employee_visible("Alice")
