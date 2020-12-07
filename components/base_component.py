from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BaseComponent:
    """Represent a web component in a web  page"""
    def __init__(self, driver: WebDriver,root_locator: str, timeout: int =10):
        self._driver = driver
        self._timeout = timeout
        self._wait = WebDriverWait(self._driver, self._timeout)
        self._root_locator = root_locator

    def wait_until_loaded(self):
        """wait until locator the element is present in the page"""
        tmp_loc = (By.XPATH,self._root_locator)
        self._wait.until(EC.presence_of_element_located(tmp_loc))

    def set_default_timeout(self, timeout : int):
        """Set default time out for explicit waits"""
        if(timeout) == int:
            self._timeout = timeout
            self._wait = WebDriverWait(self._driver, self._timeout)
        else:
            raise ValueError(f'Invalid value for timeout:{timeout}')

    def get_default_timeout(self) -> int:
        """Get default time out for explicit waits
        :return: Timeout in seconds
        """
        return self._timeout

    def get_root_element(self) -> WebElement:
        """Get root element"""
        tmp_loc = (By.XPATH, self._root_locator)
        return self._wait.until(EC.presence_of_element_located(tmp_loc))

    def get_descendant_element(self,xpath) -> WebElement:
        """ Find descendant in component
        :param xpath:
        :return:
        """
        tmp_xpath = self._chain_xpath(xpath)
        tmp_loc = (By.XPATH,tmp_xpath)
        return self._wait.until(EC.visibility_of_element_located(tmp_loc))

    def get_descendant_elements (self, xpath) -> list:
        """Find descendants in component
        :param xpath: Descendant xpath relative to root
        :return: Element
        """
        tmp_xpath = self._chain_xpath(xpath)
        tmp_loc = (By.XPATH, tmp_xpath)
        return self._wait.until(EC.visibility_of_all_elements_located(tmp_loc))

    def _chain_xpath(self,xpath) -> str:
        """ Concat two xpath
        :param xpath:
        :return:
        """
        return self._root_locator + xpath




