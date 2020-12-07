from common.webdriver_factory import create_driver_instance
from pages.demoqa.book_store import BookStore


try:
    driver = create_driver_instance('chrome')
    page = BookStore(driver)
    page.open()
    page.wait_until_loaded()
    page.search('Learning')
    info = page.get_table_info()
finally:
    input()
    driver.close()