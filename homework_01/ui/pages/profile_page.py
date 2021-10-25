from ui.pages.base_page import BasePage
from ui.locators.basic_locators import ProfilePageLocators

class ProfilePage(BasePage):

    locators = ProfilePageLocators()

    def edit_info(self, name, phone):
        self.fill_field(ProfilePageLocators.NAME_LOCATOR, name)
        self.fill_field(ProfilePageLocators.PHONE_LOCATOR, phone)
        self.click(ProfilePageLocators.SUBMIT_LOCATOR)