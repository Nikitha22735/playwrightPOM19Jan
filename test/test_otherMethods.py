from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/#")
    page.wait_for_timeout(5000)
    # page.locator("//button[text()='Point Me']").hover()
   
    # page.locator("//button[@ondblclick='myFunction1()']").dblclick()
    page.locator("#name").click()
    page.keyboard.down("Shift")
    page.keyboard.type("Nikitha")
    page.keyboard.up("Shift")
    # page.keyboard.press("Control+A")
    # page.keyboard.press("Control+C")
    # page.keyboard.press("Tab")
    # page.keyboard.press("Control+V")
    page.wait_for_timeout(5000)