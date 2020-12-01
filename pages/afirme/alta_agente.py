"""Alta de agentes por internet"""
from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver,WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AltaAgente(BasePage):
    __URL = 'https://qa.afirmeseguros.com/AltaAgentesNeg/'
    __SUBMIT_LOC = (By.XPATH, "//*[@class='btn btn-primary float-right' and @type='submit']")
    __CONFIG_AVANZADA_LOC = (By.ID ,'details-button')
    __PROCEED_LINK_LOC = (By.ID, 'proceed-link')
    __SECTOR_DROPDWN_LOC ='Sector'

    def __init__(self, driver : WebDriver,timeout: int = 20):
        super().__init__(driver, timeout, self.__URL)


    def wait_until_loaded(self):
        """Wait until buton submit is visibility
        :return: None
        """
        self._wait.until(EC.visibility_of_element_located(self.__SUBMIT_LOC))

    def omit_security(self):
        """Omit the security configuration"""
        element = self._wait.until(EC.visibility_of_element_located(self.__CONFIG_AVANZADA_LOC))
        element.click()
        element = self._wait.until(EC.visibility_of_element_located(self.__PROCEED_LINK_LOC))
        element.click()

    def select_sector(self,value: str):
        #element = Select(self._driver.find_element_by_id(self.__SECTOR_DROPDWN_LOC))
        select_sector =Select(self._driver.find_element_by_id(self.__SECTOR_DROPDWN_LOC))
       # select_sector.select_by_value("01")
        print(select_sector.options)










