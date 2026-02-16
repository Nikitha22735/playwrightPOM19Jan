from playwright.sync_api import Page, expect
from allureWraper import BasePage
class logInPage(BasePage):
    def __init__(self,page:Page):
        self.emailTextBox = page.locator("#ap_email_login")
        self.continueBtn = page.locator('//*[@aria-labelledby="continue-announce"]')
        self.passwordTextBox = page.locator("#ap_password")
        self.signInBtn = page.locator('//*[@aria-labelledby="auth-signin-button-announce"]')
        self.passwordErrorMessage = page.locator("//*[contains(text(),'Your password is incorrect')]")




    def enterEmailAddress(self,username):
        self.emailTextBox.fill(username)

    def clickOnContinueBtn(self):
        self.continueBtn.click()

    def enterPassword(self,password):
        self.passwordTextBox.fill(password)

    def clickOnSignInbtn(self):
        self.signInBtn.click()

    def validateTheVisibilityOfErrorMessage(self):
        expect(self.passwordErrorMessage).to_be_visible()


