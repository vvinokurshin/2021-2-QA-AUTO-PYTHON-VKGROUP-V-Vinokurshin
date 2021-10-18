from selenium.webdriver.common.by import By

class LoginPageLocators: 
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    ENTER_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

class MainPageLocators:
    MENU_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
    LOGOUT_LOCATOR = (By.LINK_TEXT, "ВЫЙТИ")
    PROFILE_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-profile')]")
    TOOLS_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-tools')]")

class ProfilePageLocators:
    NAME_LOCATOR = (By.XPATH, "//div[@data-name='fio']//input[@type='text']")
    PHONE_LOCATOR = (By.XPATH, "//div[@data-name='phone']//input[@type='text']")
    SUBMIT_LOCATOR = (By.XPATH, "//button[@class='button button_submit']")