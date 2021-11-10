from ui.locators.basic_locators import AudiencesPageLocators
from ui.pages.base_page import BasePage

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from utils import utils

class AudiencesPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'

    locators = AudiencesPageLocators()

    def create_segment(self, files_path):
        self.logger.debug('Start creating segment')

        try:
            self.click(AudiencesPageLocators.ADD_SEGMENT_LOCATOR)
        except TimeoutException:
            self.click(AudiencesPageLocators.SUBMIT_LOCATOR)

        self.click(AudiencesPageLocators.APP_LOCATOR)    
        self.click(AudiencesPageLocators.CHECKBOX_LOCATOR)
        self.click(AudiencesPageLocators.CREATE_SEGMENT_LOCATOR)

        with open(utils.get_full_name(files_path, 'segment.txt')) as f:
            name = f.readline().strip()

        self.fill_field(AudiencesPageLocators.NAME_SEGMENT_LOCATOR, name)

        self.click(AudiencesPageLocators.SUBMIT_LOCATOR)

        self.logger.debug('Segment successfully created')

        return name

    def remove_segment(self, name):
        self.logger.debug('Start removing segment')

        segments = self.find_list(AudiencesPageLocators.SEGMENTS_LOCATOR)

        for i in range(len(segments)):
            try: 
                segments[i].find_element(By.XPATH, f'.//a[@title="{name}"]')
                index = i
                break

            except NoSuchElementException:
                if (i == len(segments) - 1):
                    raise

        checkboxes = self.find_list(AudiencesPageLocators.CHECKBOXES_LOCATOR)
        checkboxes[index + 1].click()

        self.click(AudiencesPageLocators.ACTIONS_LOCATOR)
        self.click(AudiencesPageLocators.DELETE_SEGMENT_LOCATOR)

        self.logger.debug('Segment successfully removed')