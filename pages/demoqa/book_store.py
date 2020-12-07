
"""Logic to interact with de book store page"""
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BookStore(BasePage):

    __URL = 'https://demoqa.com/books'
    __INPUT_LOC = (By.ID,'searchBox')
    __TABLE_ROW_LOC =(By.XPATH, "//*[@class ='rt-tbody']//*[@class='rt-tr-group']")

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver, timeout, self.__URL)


    def wait_until_loaded(self):
        """Wait until boton submit is loaded"""
        self._wait.until(EC.presence_of_element_located(self.__INPUT_LOC))

    def search(self, value : str):
        """Search entry"""
        element = self._wait.until(EC.visibility_of_element_located(self.__INPUT_LOC))
        element.clear()
        element.send_keys(value)

    def get_table_info(self) -> dict:
        """Get table information"""
        rows = self._wait.until(EC.visibility_of_all_elements_located(self.__TABLE_ROW_LOC))
        info = {}
        for index, row in enumerate(rows):
            cells = row.findelemets_by_xpath(".//*[@role='gridcell']")
            title = cells[1].text
            author = cells[2].text
            publisher = cells[3].text
            info[index] = {'tile':title , 'author':author,'publisher' : publisher}
        return info




