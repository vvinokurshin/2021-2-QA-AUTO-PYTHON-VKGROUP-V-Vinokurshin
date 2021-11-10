from selenium.webdriver.common.by import By

class LoginPageLocators: 
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    ENTER_LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")

class CampaignPageLocators:
    ADD_CAMPAIGN_LOCATOR_1 = (By.XPATH, "//a[contains(@href, '/campaign/new')]")
    ADD_CAMPAIGN_LOCATOR_2 = (By.XPATH, "//div[contains(@class, 'button-module-button')]")
    
    TRAFFIC_LOCATOR = (By.XPATH, "//div[contains(@class, 'column-list-item _traffic')]")
    URL_LOCATOR = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput')]")
    
    NAME_CAMPAIGN_LOCATOR = (By.XPATH, "//div[@class='input input_campaign-name input_with-close']//input[@type='text']")

    DELETE_REGION_LOCATOR = (By.XPATH, "//span[contains(@class, 'selectedRegions-module-itemClose')]")
    GEOGRAFY_LOCATOR = (By.XPATH, "//li[contains(@data-name, 'geo')]")
    REGION_LOCATOR = (By.XPATH, ".//input[contains(@class, 'suggester-module-searchInput')]")
    ADD_REGION_LOCATOR = (By.XPATH, "//div[contains(@class, 'button-module-transparentTextWrapper')]")

    BANNER_LOCATOR = (By.ID, "patterns_banner_4")
    IMAGE_INPUT_LOCATOR = (By.XPATH, '//input[@data-test="image_240x400"]')
    IMAGE_SUBMIT_LOCATOR = (By.XPATH, "//input[contains(@class, 'image-cropper__save js-save')]")
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]")

    CAMPAINGS_LOCATOR = (By.XPATH, "//div[contains(@class, 'main-module-CellFirst')]")
    CHECKBOX_LOCATOR = (By.XPATH, ".//input[@type='checkbox']")
    ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'tableControls-module-selectItem')]")
    DELETE_CAMPAIGN_LOCATOR = (By.XPATH, "//li[@data-id='8']")

    AUDIENCES_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-segments')]")

class AudiencesPageLocators():
    ADD_SEGMENT_LOCATOR = (By.XPATH, "//a[contains(@href, '/segments/segments_list/new/')]")

    APP_LOCATOR = (By.XPATH, "//div[contains(@class, 'adding-segments-item')]")
    CHECKBOX_LOCATOR = (By.XPATH, "//input[contains(@class,'adding-segments-source__checkbox js-main-source-checkbox')]")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[@class='adding-segments-modal__btn-wrap js-add-button']//button[@class='button button_submit']")

    NAME_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class,'input input_create-segment-form')]//input[contains(@type,'text')]")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@class, 'button_submit')]")

    SEGMENTS_LOCATOR = (By.XPATH, "//div[contains(@class, 'cells-module-nameCell')]")
    CHECKBOXES_LOCATOR = (By.XPATH, "//input[@type='checkbox']")

    ACTIONS_LOCATOR = (By.XPATH, "//div[contains(@class, 'segmentsTable-module-selectItem')]")
    DELETE_SEGMENT_LOCATOR = (By.XPATH, "//li[@data-id='remove']")
