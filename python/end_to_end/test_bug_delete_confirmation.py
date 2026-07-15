from pages import (
    AddEmployeePage, EmployeesListPage, DeleteConfirmationPage
)


def test_delete_confirmation_shows_correct_info(page):
    """BUG-004: Delete confirmation page should show correct info for
    employees with special characters in their name."""
    add_employee = AddEmployeePage(page)
    employees_list = EmployeesListPage(page)
    delete_page = DeleteConfirmationPage(page)

    add_employee.create_employee(
        name="O'Brien",
        email="obrien@test.com",
        address="1 Irish Road",
        city="Dublin",
        zip_code="12345",
        hiring_date="2024-03-17",
        job_title="Developer",
    )

    employees_list.navigate()
    employees_list.click_delete()

    assert delete_page.is_text_visible("O'Brien"), (
        "BUG-004: Delete confirmation page does not display employee name "
        "correctly. Name 'O'Brien' (containing a single quote) is not visible "
        "on the confirmation page. This indicates improper escaping of special "
        "characters in HTML output."
    )
