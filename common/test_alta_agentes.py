"""Run test case for alta de agentes por internet"""

from common.webdriver_factory import create_driver_instance ,ROOT_DIR
from pages.afirme.alta_agente import AltaAgente


driver = create_driver_instance('chrome')

try:
    page = AltaAgente(driver,5)
    page.open()
    page.omit_security()
    page.wait_until_loaded()
    page.select_sector('01')
finally:
    input()
    driver.close()

