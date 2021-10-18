from ui.pages.base_page import BasePage
from ui.locators.basic_locators import ProfilePageLocators

class ProfilePage(BasePage):

    locators = ProfilePageLocators()

    def edit_info(self, name, phone):
        field = self.find(ProfilePageLocators.NAME_LOCATOR)
        field.clear()
        field.send_keys(name)
        field = self.find(ProfilePageLocators.PHONE_LOCATOR)
        field.clear()
        field.send_keys(phone)
        self.click(ProfilePageLocators.SUBMIT_LOCATOR)