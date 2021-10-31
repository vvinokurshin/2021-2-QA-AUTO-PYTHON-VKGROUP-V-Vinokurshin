import os

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def object_exist(page, name, exist=None):
    xpath = f'//a[@title="{name}"]'
    
    try:
        page.find((By.XPATH, xpath))
        return True
    except TimeoutException:
        return False

def get_full_name(files_path, filename):
    return os.path.join(files_path, filename)

