# from playwright.sync_api import 
from pages.homeaPage import homePage
from pages.resultsPage import resultsPage
import pytest

@pytest.mark.single2()
def test_ValdiateTheShoppingCartDetails(page,loginToAmazon):
    homePageObj = homePage(page)
    homePageObj.enterProductToSearch("iphone")
    homePageObj.clickOnSearchBtn()
    resultsPageObj = resultsPage(page)
    resultsPageObj.validateTheVisibilityOfResults() 
    title = "Sponsored Ad - iPhone 15 Plus (512 GB) - Green"
    resultsPageObj.clickOnAddToCartBtn(title)
    page.wait_for_timeout(5000)
    title = "iPhone 17 Pro Max 2 TB: 17.42 cm (6.9″) Display with Promotion, A19 Pro Chip, Best Battery Life in Any iPhone Ever, Pro Fusion Camera System, Center Stage Front Camera; Silver"
    resultsPageObj.clickOnAddToCartBtn(title)
    resultsPageObj.clickOnCartBtn()
    page.wait_for_timeout(5000)
    


