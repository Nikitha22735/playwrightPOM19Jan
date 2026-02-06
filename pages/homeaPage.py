from playwright.sync_api import Page,expect

class homePage():
    def __init__(self, page:Page):
        self.searchboxLocator = page.get_by_placeholder("Search Amazon.in")
        self.cartBtn = page.locator(".nav-cart-icon.nav-sprite")
        self.accountBtn = page.locator("//span[contains(text(),'Account & Lists')]")
        self.ordersBtn = page.locator("#nav-orders")
        self.amazonlogo= page.get_by_role("link", name="Amazon.in")
        self.signInBtn = page.locator("//span[text()='Sign in']")
        self.searchBtn = page.locator("#nav-search-submit-button")
        


    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchboxLocator).to_be_visible()


    def validateTheVisibilityOfCart(self):
        expect(self.cartBtn).to_be_visible()

    def validateTheVisibilityOfAccountsAndList(self):
         expect(self.accountBtn).to_be_visible()

    def validateTheVisibilityOfOrders(self):
        expect(self.ordersBtn).to_be_visible()

    def clickOnSignInBtn(self):
        self.accountBtn.hover()
        self.signInBtn.click()


    def enterProductToSearch(self,product):
        self.searchboxLocator.fill(product)

    def clickOnSearchBtn(self):
        self.searchBtn.click()


    
        
    