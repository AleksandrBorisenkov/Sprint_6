import random
import pytest

from selenium import webdriver

from URLS import URL
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

@pytest.fixture
def phone_generator():
    telephone = random.randint(11111111111, 99999999999)
    return telephone

# сгенерировали имя
@pytest.fixture
def f_name_generator():
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    frs_name = ''.join(random.choice(letters) for i in range(10))
    return frs_name

# сгенерировали фамилию
@pytest.fixture
def l_name_generator():
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    lst_name = ''.join(random.choice(letters) for i in range(10))
    return lst_name

# предзаполнение адреса
@pytest.fixture
def address_generator():
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    address = ''.join(random.choice(letters) for i in range(10))
    numbs = random.randint(111, 999)
    return f"{address} {numbs}"
