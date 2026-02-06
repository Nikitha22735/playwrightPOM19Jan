from playwright.sync_api import Page
from pages.homeaPage import homePage
from pages.loginPage import logInPage
from pages.resultsPage import resultsPage
import pytest


@pytest.mark.single()
def test_validateTheResults(page: Page, loginToAmazon):
    homePageObj = homePage(page)
    resultsPageObj = resultsPage(page)
    homePageObj.enterProductToSearch("iphone")
    homePageObj.clickOnSearchBtn()
    resultsPageObj.validateTheVisibilityOfResults()

