from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from utils import creds

class LoginPage(BasePage):

    locators = LoginPageLocators()
    creds = {'email' : creds.MY_EMAIL, 'password' : creds.MY_PASSWORD} 
