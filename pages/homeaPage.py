from playwright.sync_api import Page,expect
import allure
from allureWraper import BasePage

class homePage(BasePage):

    def __init__(self, page: Page):
        # self.page = page
        self.searchboxLocator = page.get_by_placeholder("Search Amazon.in")
        self.cartBtn = page.locator(".nav-cart-icon.nav-sprite")
        self.accountBtn = page.locator("//span[contains(text(),'Account & Lists')]")
        self.ordersBtn = page.locator("#nav-orders")
        self.amazonlogo= page.get_by_role("link", name="Amazon.in")
        self.signInBtn = page.locator("//span[text()='Sign in']")
        self.searchBtn = page.locator("#nav-search-submit-button")
        

    # @allure.step("validating the visibility of serachbox")
    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchboxLocator).to_be_visible()
        # assert self.searchboxLocator.i
        # expect(self.searchboxLocator).to_be_visible()

    # @allure.step("validating the visibility of Cart")
    def validateTheVisibilityOfCart(self):
        expect(self.cartBtn).to_be_visible()
    # @allure.step("validating the visibility of account")
    def validateTheVisibilityOfAccountsAndList(self):
         expect(self.accountBtn).to_be_visible()
    # @allure.step("validating the visibility of order")
    def validateTheVisibilityOfOrders(self):
        expect(self.ordersBtn).to_be_visible()
    # @allure.step("validating the visibility of signin")
    def clickOnSignInBtn(self):
        self.page.wait_for_timeout(3000)
        self.accountBtn.hover()
        self.signInBtn.click()


    def enterProductToSearch(self,product):
        self.searchboxLocator.fill(product)

    def clickOnSearchBtn(self):
        self.searchBtn.click()


    def naviagetToAmazon(self):
        self.page.goto("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=12430018562869442459&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9050507&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")

    
        
    