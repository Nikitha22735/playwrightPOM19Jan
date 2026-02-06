import pytest
from playwright.sync_api import expect, Page, sync_playwright

from pages.homeaPage import homePage
from pages.loginPage import logInPage
from pages.resultsPage import resultsPage


@pytest.fixture(scope="session")
def navigateToEmailAddressPage(page):
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    homePageObj.clickOnSignInBtn()
    yield
    # yield page

@pytest.fixture()
def loginToAmazon(page:Page):
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    logInPageObj = logInPage(page)
    page.wait_for_timeout(3000)
    homePageObj.clickOnSignInBtn()
    logInPageObj.enterEmailAddress("trainingplaywright@gmail.com")
    logInPageObj.clickOnContinueBtn()
    logInPageObj.enterPassword("Welcome@04")
    logInPageObj.clickOnSignInbtn()
