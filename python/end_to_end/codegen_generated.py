import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.i2.hr.dmerej.info/")
    page.get_by_role("link", name="List employees").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("A")
    page.get_by_role("textbox", name="Name").press("CapsLock")
    page.get_by_role("textbox", name="Name").fill("Alice")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("alice@xample.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("1 ")
    page.locator("html").click()
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("1 Rue de Paris")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").press("CapsLock")
    page.get_by_role("textbox", name="City").fill("P")
    page.get_by_role("textbox", name="City").press("CapsLock")
    page.get_by_role("textbox", name="City").fill("Paris")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("75001")
    page.get_by_role("textbox", name="Hiring date").press("ArrowRight")
    page.get_by_role("textbox", name="Hiring date").fill("2024-06-04")
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").press("CapsLock")
    page.get_by_role("textbox", name="Job title").fill("E")
    page.get_by_role("textbox", name="Job title").press("CapsLock")
    page.get_by_role("textbox", name="Job title").fill("Engineer")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
