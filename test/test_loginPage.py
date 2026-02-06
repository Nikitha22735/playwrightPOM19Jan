from playwright.sync_api import Page
from pages.homeaPage import homePage
from pages.loginPage import logInPage
import pytest




def test_lognUsingValidCredentials(page, navigateToEmailAddressPage):
    homePageObj = homePage(page)
    logInPageObj = logInPage(page)
    logInPageObj.enterEmailAddress("trainingplaywright@gmail.com")
    logInPageObj.clickOnContinueBtn()
    logInPageObj.enterPassword("Welcome@04")
    logInPageObj.clickOnSignInbtn()



def test_lognUsingInValidCredentials(page, navigateToEmailAddressPage):
    homePageObj = homePage(page)
    logInPageObj = logInPage(page)

    logInPageObj.enterEmailAddress("trainingplaywright@gmail.com")
    logInPageObj.clickOnContinueBtn()
    logInPageObj.enterPassword("Welcome@04123")
    logInPageObj.clickOnSignInbtn()
    logInPageObj.validateTheVisibilityOfErrorMessage()
