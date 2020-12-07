"""Run test case for login"""
from pages.demoqa.practice_login import Login
from common.webdriver_factory import create_driver_instance

driver  = create_driver_instance('chrome')

try:
    page = Login(driver, 5)
    page.open()
    page.wait_until_loaded()
    page.set_user_name('luz.carrillo')
    print(page.get_user_name())
    page.set_password('123456')
    print(page.get_password())
    page.login()
finally:
    input()
    page.close()
