from components.base_component import BaseComponent
from selenium import webdriver

class Calendario(BaseComponent):
    """"""
    def __init__(self, driver: webdriver, root_locator: str, timeout: int = 10):
        super().__init__(driver, root_locator, timeout)

