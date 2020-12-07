from common.webdriver_factory import create_driver_instance
from pages.afirme.alta_agente import AltaAgente

try:

    driver = create_driver_instance('chrome')
    page = AltaAgente(driver, 5)
    page.open()
    page.omit_security()
    page.wait_until_loaded()
    page.select_sector(1)
finally:
    input()
    page.close()
