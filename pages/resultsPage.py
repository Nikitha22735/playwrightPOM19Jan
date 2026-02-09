from playwright.sync_api import Page, expect
class resultsPage:
    def __init__(self,page: Page):
        self.page = page
        self.resultsText = page.locator("//h2[text()='Results']")
        self.addToCart = lambda title: page.locator(f"//h2[@aria-label='{title}']//ancestor::div[@data-cy='title-recipe']//following-sibling::div[@class='puisg-row puis-desktop-list-row']//button[text()='Add to cart']")
        self.cart = page.locator("#nav-cart-count-container")


    def validateTheVisibilityOfResults(self):
        expect(self.resultsText).to_be_visible()

    def clickOnAddToCartBtn(self,title):
        self.page.wait_for_timeout(3000)
        self.addToCart(title).click()

    def clickOnCartBtn(self):
        self.cart.click()



