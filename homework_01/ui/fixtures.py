import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.profile_page import ProfilePage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver=driver)

@pytest.fixture(scope='function')
def driver(config):

    browser = config['browser']
    url = config['url']

    if browser == 'chrome':
        browser = webdriver.Chrome(executable_path='/home/valeriy/drivers/chromedriver')
    else:
        raise RuntimeError(f'Unsupported browser: {browser}')

    browser.maximize_window()
    browser.get(url)

    yield browser

    browser.close()