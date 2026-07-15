# HR Manager Web Application

# Part 1 - exploratory testing

Go to `https://<letter>.<group>.hr.dmerej.info`.

## Step 1.1

Do some manual, exploratory testing first.

Create a test plan and run it manually - try to find as many issues as possible - and try to find different _kinds_ of issues.

Put all the bugs you found into the bug tracker

Deliveries:

- A test plan (steps, outcome, and so on) > `test_plan.md`
- The bug tracker itself > `bug_tracker.md`

## Step 1.2

There's been an update !

- Re-run the whole test plan for the new version
- Adapt the bug tracker accordingly

> Same files: `test_plan.md`, `bug_tracker.md`

# Part 2 - end to end testing with Playwright

## Step 2.1

- Choose a programming language
- Follow the instruction in the matching folder
- Make sure you can run the **end to end** test.

> `python/end_to_end/test_end_to_end_add_team.py`

## Step 2.2

Use the `playwright codegen` command to generate _one_ test and add it to the repository in a new file next to the existing add-team test.

(see details instructions in each subfolder)

> `python/end_to_end/codegen_generated.py`

## Step 2.3

- Add a test for one of the bugs you fond during the first session - but _without using codegen_ this time.
- Refactor so that you use a test fixture between each test to reset the database

> `python/end_to_end/test_bug_negative_zip.py`
> `python/end_to_end/conftest.py` (DB reset fixture)

## Step 2.4

Add more tests for some of the bugs you found - make sure they are failing for the right reason, with good error messages. Stop when you have 3 or 4 different tests

> `python/end_to_end/test_bug_negative_zip.py`
> `python/end_to_end/test_bug_delete_confirmation.py`
> `python/end_to_end/test_bug_hiring_date.py`
> `python/end_to_end/test_bug_team_duplicate.py`

## Step 2.5

Refactor using the [Page object model](https://playwright.dev/python/docs/pom) design pattern

> `python/end_to_end/pages/`
>   - `add_employee_page.py`
>   - `add_team_page.py`
>   - `delete_confirmation_page.py`
>   - `employees_list_page.py`
>   - `teams_list_page.py`

## Step 2.6

Compare the code written using the Page Object Model with the one playwright automatically generated.

> POM: `python/end_to_end/pages/`
> Codegen: `python/end_to_end/codegen_generated.py`

# Part 3 - integration tests

## Part 3.2

- Make sure you can run the **integration** test

You'll see it only works when the database contains no other team.

In other words, it passes the first time you run it, then it fails because the back-end returns a 400 HTTP status.

> `python/integration/test_integration_add_team.py`

## Step 3.3

Find a strategy to handle clean separation between tests while still
using the database.

> `python/integration/conftest.py` (TRUNCATE CASCADE before each test)

## Step 3.4

Once your done, rewrite the tests from part 1 and 2 using raw HTTP requests
and SQL queries.

Some clues:

 * Use DBeaver or a similar solution to see the content of the PostgreSQL database (you can get the 
database URL in the test logs)
* Use your browser dev extensions to look at the payload of the POST requests

The tables used by the backend code can be created and dropped using the `up` and `down` sql scripts respectively.

> `python/integration/test_integration_add_team.py`
> `python/integration/test_bug_sql_injection.py`
> `python/integration/test_bug_hiring_date.py`
> `python/integration/test_bug_team_duplicate.py`

# Part 4

If you did everything right, you may realized you basically did the same test 3 times:

- once by hand
- once with playwright
- once with integration tests

And we could imagine you could add a unit test.

So, basically, the same bug would covered by 4 different kind of tests.

What do you think ?

> `part4_reflection.md`
