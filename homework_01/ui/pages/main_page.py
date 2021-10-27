from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators

class MainPage(BasePage):

    locators = MainPageLocators()

    def logout(self):            
        import time
        time.sleep(3)
        self.click(MainPageLocators.MENU_LOCATOR)
        time.sleep(3)
        self.click(MainPageLocators.LOGOUT_LOCATOR)
        time.sleep(3)
            
    def move_to(self, locator):
        self.click(locator)
        