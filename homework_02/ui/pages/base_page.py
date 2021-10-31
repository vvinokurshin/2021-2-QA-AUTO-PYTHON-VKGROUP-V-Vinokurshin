import logging
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec

import time

CLICK_RETRY = 5
DELAY = 10

class PageNotLoadedException(Exception):
    pass

class BasePage(object):

    url = 'https://target.my.com/'

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self, timeout=DELAY):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout}sec for {self.__class__.__name__}.\n'
                                     f'Current url: {self.driver.current_url}.')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = DELAY
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def find_list(self, locator, timeout=None):
        return self.wait(timeout).until(ec.presence_of_all_elements_located(locator))

    def fill_field(self, locator, string):
        field = self.find(locator)
        field.clear()
        field.send_keys(string)

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY-1:
                    raise
