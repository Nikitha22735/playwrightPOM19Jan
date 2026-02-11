from playwright.sync_api import expect, Page
from pages.homeaPage import homePage
import pytest

@pytest.mark.single34()
def test_validateUIOfAmazonHomePage(page: Page, loginToAmazon):
    page.wait_for_timeout(20000)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", timeout=30000)
    homePageObj = homePage(page)
    homePageObj.validateTheVisibilityOfSearchBox()
    homePageObj.validateTheVisibilityOfCart()
    homePageObj.validateTheVisibilityOfAccountsAndList()
    homePageObj.validateTheVisibilityOfOrders()


    