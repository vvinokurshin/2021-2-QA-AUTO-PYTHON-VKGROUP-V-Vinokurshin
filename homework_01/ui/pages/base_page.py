from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec

CLICK_RETRY = 5
DELAY = 30

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = WebDriverWait(self.driver, DELAY).until(ec.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                elem = WebDriverWait(self.driver, DELAY).until(ec.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
