from playwright.sync_api import Playwright, sync_playwright, expect
import random,time


def run(playwright: Playwright, user, password) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:5000/login?next=%2F")
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill(user)
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    while True:
        num = random.randint(1,5)
        user = "testuser" + str(num)
        if random.random() > 0.1:
            password = "password"
        else:
            password = "pass"
        run(playwright,user,password)
        time.sleep(1)