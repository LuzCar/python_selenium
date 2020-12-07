"""represent stay form from expedia"""

from components.base_component import BaseComponent
from selenium import webdriver
from components.expedia.input import Input

class Stay(BaseComponent):
    """Represent stay form from expedia"""
    __DESTINATION_XPATH = "//*[@data-testid='location-field-destination-container']"

    def __init__(self,driver: webdriver, root_locator:str, timeout: int =10):
        super().__init__(driver,root_locator,timeout)
        self.destination = Input(self._driver,self.__DESTINATION_XPATH)
