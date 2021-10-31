import pytest
import allure
from base import BaseCase
from ui.pages.base_page import PageNotLoadedException
from ui.pages.login_page import LoginPage
from ui.pages.audiences_page import AudiencesPage
from ui.pages.campaign_page import CampaignPage
from ui.locators.basic_locators import CampaignPageLocators

from utils import utils

@pytest.mark.UI
@allure.story('Negative login tests')
class TestNegative(BaseCase):
    authorize = False

    # @pytest.mark.skip("DONE")
    @pytest.mark.parametrize(
        'email, password', 
        [
            pytest.param(
                'test@mail.ru', 'vktesters'
            )
            ,
            pytest.param(
                'valera_valera03@mail.ru', 'test'
            )
        ]
    )
    def test_login_failed(self, email, password):
        login_page = LoginPage(self.driver)

        try:
            login_page.login(email, password)
        except PageNotLoadedException:
            pass

@pytest.mark.UI
class TestPositive(BaseCase):

    # @pytest.mark.skip("DONE")
    @allure.story('Creating campaign')
    def test_create_campaign(self, files_path):
        campaign_page = CampaignPage(self.driver)
        name = campaign_page.create_campaign(utils.get_full_name(files_path, 'example.png'), files_path)

        assert utils.object_exist(campaign_page, name)

    # @pytest.mark.skip("DONE")
    @allure.story('Removing campaign')
    def test_remove_campaign(self, files_path):
        campaign_page = CampaignPage(self.driver)

        with open(utils.get_full_name(files_path, 'campaign.txt')) as f:
            lines = f.readlines()[1:2]
            name = lines[0].strip()

        campaign_page.remove_campaign(name)
        self.driver.refresh()

        assert not utils.object_exist(campaign_page, name)

    # @pytest.mark.skip("DONE")
    @allure.story('Adding segment')
    def test_add_segment(self, files_path):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to_audiences(CampaignPageLocators.AUDIENCES_LOCATOR)
        audiences_page = AudiencesPage(self.driver)

        name = audiences_page.create_segment(files_path)

        assert utils.object_exist(audiences_page, name)

    # @pytest.mark.skip("DONE")
    @allure.story('Removing segment')
    def test_remove_segment(self, files_path):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to_audiences(CampaignPageLocators.AUDIENCES_LOCATOR)
        audiences_page = AudiencesPage(self.driver)

        with open(utils.get_full_name(files_path, 'segment.txt')) as f:
            name = f.readline().strip()
            
        audiences_page.remove_segment(name)
        self.driver.refresh()

        assert not utils.object_exist(audiences_page, name)
