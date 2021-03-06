from ui.pages.audiences_page import AudiencesPage
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import AudiencesPageLocators, CampaignPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from selenium.webdriver.common.by import By

from utils import utils

class CampaignPage(BasePage):
    url = 'https://target.my.com/dashboard'

    locators = CampaignPageLocators()

    def move_to_audiences(self, locator):
        self.click(locator)

        self.logger.debug('Mooving to audiences page')

        return AudiencesPage(self.driver)

    def upload_picture(self, locator, filename):
        object = self.find(locator)
        object.send_keys(filename)

    def create_campaign(self, filename, files_path):
        self.logger.debug('Start creating campaign')

        try:
            self.click(CampaignPageLocators.ADD_CAMPAIGN_LOCATOR_1)
        except TimeoutException:
            self.click(CampaignPageLocators.ADD_CAMPAIGN_LOCATOR_2)

        self.click(CampaignPageLocators.TRAFFIC_LOCATOR)

        with open(utils.get_full_name(files_path, 'campaign.txt')) as f:
            url = f.readline().strip()
            name = f.readline().strip()
            region = f.readline().strip()

        f.close()

        self.fill_field(CampaignPageLocators.URL_LOCATOR, url)
    
        name_field = self.wait(5).until(ec.element_to_be_clickable(CampaignPageLocators.NAME_CAMPAIGN_LOCATOR))
        name_field.clear()
        name_field.send_keys(name)

        self.click(CampaignPageLocators.DELETE_REGION_LOCATOR)
        self.find_by_parent(CampaignPageLocators.GEOGRAFY_LOCATOR, CampaignPageLocators.REGION_LOCATOR).send_keys(region)
        self.click(CampaignPageLocators.ADD_REGION_LOCATOR)

        self.click(CampaignPageLocators.BANNER_LOCATOR)
        self.upload_picture(CampaignPageLocators.IMAGE_INPUT_LOCATOR, filename)
        self.click(CampaignPageLocators.IMAGE_SUBMIT_LOCATOR)

        self.click(CampaignPageLocators.CREATE_CAMPAIGN_LOCATOR)

        self.logger.debug('Campaign successfully created')

        return name

    def remove_campaign(self, name):
        self.logger.debug('Start removing campaign')

        campaings = self.find_list(CampaignPageLocators.CAMPAINGS_LOCATOR)

        for i in range(len(campaings)):
            try: 
                campaings[i].find_element(By.XPATH, f'.//a[@title="{name}"]')
                campaings[i].find_element(*CampaignPageLocators.CHECKBOX_LOCATOR).click()
                break

            except NoSuchElementException:
                if (i == len(campaings) - 1):
                    raise

        self.click(CampaignPageLocators.ACTIONS_LOCATOR)
        self.click(CampaignPageLocators.DELETE_CAMPAIGN_LOCATOR)

        self.logger.debug('Campaign successfully removed')
     