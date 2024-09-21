import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.window_handles = None
        self.driver = driver

    @allure.step('Открываем страницу по ссылке')
    def get_url(self, URL):
        self.driver.get(URL)

    @allure.step('Возвращаем текущий URL страницы')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Скролл до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ищем 1 элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ищем много элементов')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Ищем элемент для клика')
    def find_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Берем текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Имитируем нажатие кнопки ENTER')
    def send_enter_key(self, locator):
        element = self.find_element_with_wait(locator)
        return element.send_keys(Keys.ENTER)

    @allure.step('Имитируем переключение на вкладку')
    def send_tab_key(self, num):
        new_tab = self.driver.window_handles
        return self.driver.switch_to.window(new_tab[num])

    @allure.step('Устанавливаем какой-то текст в инпут')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def formating_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return method, locator
