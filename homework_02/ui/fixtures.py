import pytest
import os
import allure
import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from ui.pages.login_page import LoginPage

from utils import creds

def get_driver(config, download_dir=None):
    browser_name = config['browser']
    selenoid = config['selenoid']
    vnc = config['vnc']

    if browser_name == 'chrome':
        options = Options()

        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})

        if selenoid:
            options.add_experimental_option("prefs", {"download.default_directory": '/home/\'Загрузки\'/'})
            capabilities = {
                'browserName': 'chrome',
                'version': '95.0'
            }

            if vnc:
                capabilities['version'] += '_vnc'
                capabilities['enableVNC'] = True

            browser = webdriver.Remote(selenoid, options=options,
                                       desired_capabilities=capabilities)
        else:
            manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
            browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()
    return browser


@pytest.fixture(scope='function')
def driver(config, temp_dir):
    url = config['url']
    with allure.step('Init browser'):
        browser = get_driver(config, download_dir=temp_dir)
        browser.get(url)

    browser = get_driver(config, download_dir=temp_dir)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    config['browser'] = request.param

    browser = get_driver(config)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def credentials():
    email = creds.MY_EMAIL 
    password = creds.MY_PASSWORD

    return email, password

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

@pytest.fixture()
def files_path(repo_root):
    return os.path.join(repo_root, 'files')
