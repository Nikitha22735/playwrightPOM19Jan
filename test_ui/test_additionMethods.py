from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)


    # ##mouse actions???    hover, dblclikc, drag and drop
    # page.locator("//button[text()='Point Me']").hover()
    # page.locator("//button[text()='Copy Text']").dblclick()
    # page.drag_and_drop("div#draggable", "div#droppable")

    ###keyboardEvents

    # page.locator("#name").fill('Nikitha')
    # page.keyboard.press("Control+A")
    # page.keyboard.press("Control+C")
    # page.keyboard.press("Tab")
    # page.keyboard.down("Tab")
    # page.keyboard.up("Tab")
    # page.keyboard.press("Control+V")


    ##handling Alerts

    # def handlingAlert(dialog):
    #     page.wait_for_timeout(3000)
    #     dialog.accept("Tetsing automatiom")
    #     # page.wait_for_timeout(3000)
    #     # dialog.dismiss()
    # page.on("dialog", handlingAlert)
    # # page.locator("button#alertBtn").click()
    # # page.locator("//button[@onclick='myFunctionConfirm()']").click()
    # page.locator("//button[@onclick='myFunctionPrompt()']").click()
    # page.wait_for_timeout(3000)

    with page.expect_popup() as childTab:
         page.locator("//button[text()='New Tab']").click()

    with page.expect_popup() as childTab2:
         page.locator("//button[text()='New Tab']").click()

    page2 = childTab.value
    page3 = childTab2.value
    page2.locator("//a[text()='Online Training']").click()
    page.wait_for_timeout(3000)

   