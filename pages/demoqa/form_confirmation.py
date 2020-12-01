"""from pages.base_page import BasePage"""

from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConfirmationForm(BasePage):
    """Confirmation Page"""
    def __init__(self, driver : WebDriver, timeout : int =5):
        super().__init__(driver, timeout)
