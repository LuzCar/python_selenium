from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login(BasePage):
    """Practice Login"""
    __URL = 'https://demoqa.com/login'
    __LOGIN_LOC = (By.ID, 'login')
    __USER_NAME_LOC = (By.ID, 'userName')
    __PASS_LOC = (By.ID , 'password')



    def __init__(self,driver : WebDriver , timeout: int = 5):
        super().__init__(driver,timeout,self.__URL)

    def wait_until_loaded(self):
        """Wait until boton submit is loaded"""
        self._wait.until(EC.presence_of_element_located(self.__LOGIN_LOC))

    def set_user_name(self , value : str):
        """Set user name"""
        self.__set_input_value(self.__USER_NAME_LOC ,value)

    def get_user_name(self) ->str :
        """Get User Name"""
        element = self._wait.until(EC.element_to_be_clickable(self.__USER_NAME_LOC))
        return element.text

    def set_password(self, value: str):
        """Set user name"""
        self.__set_input_value(self.__PASS_LOC, value)

    def get_password(self) ->str :
        """Get User Name"""
        element = self._wait.until(EC.element_to_be_clickable(self.__PASS_LOC))
        return element.text

    def login(self):
        """Login"""
        element = self._wait.until(EC.element_to_be_clickable(self.__LOGIN_LOC))
        element.click()

    def __set_input_value(self, locator, value):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)

    def __get_input_value(self, locator):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        return element.get_attribute('value')




