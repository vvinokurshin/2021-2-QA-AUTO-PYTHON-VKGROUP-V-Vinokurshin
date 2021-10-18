from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators

class LoginPage(BasePage):

    locators = LoginPageLocators()

    def login(self, username, password):
        self.click(LoginPageLocators.LOGIN_LOCATOR)

        input = self.find(LoginPageLocators.EMAIL_LOCATOR)
        input.send_keys(username)

        input = self.find(LoginPageLocators.PASSWORD_LOCATOR)
        input.send_keys(password)

        self.click(LoginPageLocators.ENTER_LOGIN_LOCATOR)
