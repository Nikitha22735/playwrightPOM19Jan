import pytest
import json
from playwright.sync_api import expect, Page, sync_playwright
import allure

from pages.homeaPage import homePage
from pages.loginPage import logInPage
from pages.resultsPage import resultsPage


@pytest.fixture()
def navigateToEmailAddressPage(page):
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    homePageObj.clickOnSignInBtn()
    yield
    # yield page



@pytest.fixture(scope="module")
def loginToAmazon(page:Page):
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    logInPageObj = logInPage(page)
    page.wait_for_timeout(3000)
    homePageObj.clickOnSignInBtn()
    with open("testData/credentials.json") as data:
        testData = json.load(data)
    # logInPageObj.enterEmailAddress("trainingplaywright@gmail.com")
    logInPageObj.enterEmailAddress(testData["positiveCredentials"]["username"])
    logInPageObj.clickOnContinueBtn()
    logInPageObj.enterPassword(testData["positiveCredentials"]["password"])
    logInPageObj.clickOnSignInbtn()

#  homePageObj = homePage(page)
@pytest.fixture()
def homePageObj(page):
    homePageObj = homePage(page)
    return homePageObj


@pytest.fixture()
def resultsPageObj(page):
    resultsPageObj = resultsPage(page)
    return resultsPageObj


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page       #pausing point
        # page.close()




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )



