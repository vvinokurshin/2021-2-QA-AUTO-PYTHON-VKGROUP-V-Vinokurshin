from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators

class MainPage(BasePage):

    locators = MainPageLocators()

    def logout(self):
        self.click(MainPageLocators.MENU_LOCATOR)
        self.click(MainPageLocators.LOGOUT_LOCATOR)

    def move_to(self, locator):
        self.click(locator)