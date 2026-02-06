from playwright.sync_api import expect, Page
from pages.homeaPage import homePage

def test_validateUIOfAmazonHomePage(page: Page):
    page.goto("https://www.amazon.in/")
    # page.wait_for_timeout(20000)
    titleText = page.title()
    print("Hello")
    print(titleText)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", timeout=30000)
    homePageObj = homePage(page)
    homePageObj.validateTheVisibilityOfSearchBox()
    homePageObj.validateTheVisibilityOfCart()
    homePageObj.validateTheVisibilityOfAccountsAndList()
    homePageObj.validateTheVisibilityOfOrders()
    