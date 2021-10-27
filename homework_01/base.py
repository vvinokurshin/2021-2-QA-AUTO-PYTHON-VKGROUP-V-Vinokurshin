import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.profile_page import ProfilePage

class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.profile_page: ProfilePage = request.getfixturevalue('profile_page') 

    @pytest.fixture()
    def login(self, login_page):
        self.login_page.click(login_page.locators.LOGIN_LOCATOR)
        self.login_page.fill_field(login_page.locators.EMAIL_LOCATOR, login_page.creds.get('email'))
        self.login_page.fill_field(login_page.locators.PASSWORD_LOCATOR, login_page.creds.get('password'))
        self.login_page.click(login_page.locators.ENTER_LOGIN_LOCATOR)