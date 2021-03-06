from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.locators.basic_locators import LoginPageLocators

class LoginPage(BasePage):

    url = 'https://target.my.com/'

    def login(self, email, password, authorize=True):
        self.logger.debug("Startint authorization")
        
        self.click(LoginPageLocators.LOGIN_LOCATOR)
        self.fill_field(LoginPageLocators.EMAIL_LOCATOR, email)
        self.fill_field(LoginPageLocators.PASSWORD_LOCATOR, password)
        self.click(LoginPageLocators.ENTER_LOGIN_LOCATOR)

        self.logger.debug("Authorization data has been successfully entered")
     
        if authorize:
            return CampaignPage(self.driver)
        elif self.driver.current_url.startswith(CampaignPage.url):
            return False
        else:
            return True       
