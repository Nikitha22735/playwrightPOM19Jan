from playwright.sync_api import Page, expect
class resultsPage:
    def __init__(self,page: Page):
        self.resultsText = page.locator("//h2[text()='Results']")


    def validateTheVisibilityOfResults(self):
        expect(self.resultsText).to_be_visible()
