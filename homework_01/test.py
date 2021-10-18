import pytest
from base import BaseCase
from ui.locators import basic_locators
from ui.url import url
from utils import creds
from utils import utils

class Test_UI(BaseCase):

    def test_title(self):
        assert "myTarget" in self.driver.title

    def test_login_correct(self):
        self.login_page.login(creds.MY_EMAIL, creds.MY_PASSWORD)
        assert self.driver.current_url == url.DASHBOARD_URL
    
    @pytest.mark.parametrize(
        'email, password', 
        [
            pytest.param(
                'valera_valera03@mail.ru', 'hello'
            ),
            pytest.param(
                'hello', 'vktesters'
            )
        ]
    )
    def test_login_incorrect(self, email, password):
        self.login_page.login(email, password)
        assert self.driver.current_url != url.DASHBOARD_URL

    def test_logout(self):
        self.login_page.login(creds.MY_EMAIL, creds.MY_PASSWORD)
        self.main_page.logout()
        assert self.driver.current_url == url.MAIN_PAGE_URL

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
        self.login_page.login(creds.MY_EMAIL, creds.MY_PASSWORD)
        self.main_page.move_to(locator_field)
        assert url in self.driver.current_url

    def test_edit_info(self):
        self.login_page.login(creds.MY_EMAIL, creds.MY_PASSWORD)
        self.main_page.move_to(basic_locators.MainPageLocators.PROFILE_LOCATOR)

        name = utils.get_random_name()
        phone_number = utils.get_random_number()

        self.profile_page.edit_info(name, phone_number)
        self.driver.refresh()

        res_name = self.profile_page.find(basic_locators.ProfilePageLocators.NAME_LOCATOR)
        assert res_name.get_attribute('value') == name

        res_number = self.profile_page.find(basic_locators.ProfilePageLocators.PHONE_LOCATOR)
        assert res_number.get_attribute('value') == phone_number
