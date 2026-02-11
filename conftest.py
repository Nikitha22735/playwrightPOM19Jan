import pytest
import json
from playwright.sync_api import expect, Page, sync_playwright

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


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        yield page       #pausing point
        # page.close()



