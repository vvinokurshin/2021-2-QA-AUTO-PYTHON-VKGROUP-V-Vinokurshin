import pytest
from base import BaseCase
from ui.locators import basic_locators
from ui.url import url
from utils import utils

@pytest.mark.usefixtures('login')
@pytest.mark.UI
class Test_UI(BaseCase):
    def test_login(self):
        assert self.driver.current_url.startswith(url.DASHBOARD_URL)

    def test_logout(self):
        self.main_page.logout()
        assert self.driver.current_url.startswith(url.MAIN_PAGE_URL)

    @pytest.mark.parametrize(
        'locator_field, url', 
        [
            pytest.param(
                basic_locators.MainPageLocators.PROFILE_LOCATOR, url.PROFILE_URL
            )
            ,
            pytest.param(
                basic_locators.MainPageLocators.TOOLS_LOCATOR, url.TOOLS_URL
            )
        ]
    )
    def test_move_to(self, locator_field, url):
        self.main_page.move_to(locator_field)
        assert self.driver.current_url.startswith(url)

    def test_edit_info(self):
        self.main_page.move_to(basic_locators.MainPageLocators.PROFILE_LOCATOR)

        name = utils.get_random_name()
        phone_number = utils.get_random_number()

        self.profile_page.edit_info(name, phone_number)
        self.driver.refresh()

        res_name = self.profile_page.find(basic_locators.ProfilePageLocators.NAME_LOCATOR)
        assert res_name.get_attribute('value') == name

        res_number = self.profile_page.find(basic_locators.ProfilePageLocators.PHONE_LOCATOR)
        assert res_number.get_attribute('value') == phone_number
