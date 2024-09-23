import pytest

from selenium import webdriver
from urls import URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


# настройка драйвера браузера для FireFox
# настройки инкогнито
@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--incognito")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.get_url(URL.MAIN_URL)
    return page

@pytest.fixture(scope='function')
def order_page(driver):
    page = OrderPage(driver)
    page.get_url(URL.ORDER_URL)
    return page
