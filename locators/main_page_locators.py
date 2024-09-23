from selenium.webdriver.common.by import By


# локаторы главной страницы и страницы Dzen
class MainPageLocators:
    HEADER_MAIN = [By.CLASS_NAME, 'Header_Header__214zg']
    FIRST_PART = [By.CLASS_NAME, 'Home_FirstPart__3g6vG']

    QUESTION_LOCATOR = [By.XPATH, '//*[@id="accordion__heading-{}"]']
    ANSWER_LOCATOR = [By.XPATH, '//*[@id="accordion__panel-{}"]']
    QUESTION_LOCATOR_7 = [By.XPATH, '//*[@id="accordion__heading-7"]']
    QA_FORM = [By.CLASS_NAME, 'Home_FAQ__3uVm4']

    # локаторы 2х кнопок Заказать
    ORDER_BUTTON_TOP = [By.XPATH, '//*/div[2]/button[1][text()="Заказать"]']
    ORDER_BUTTON_MIDDLE = [By.XPATH, '//*/div[5]/button[text()="Заказать"]']

    SAMOKAT_LOGO = [By.XPATH, '//*[@alt="Scooter"]']
    YA_LOGO = [By.XPATH, '//*[@alt="Yandex"]']

    BODY = [By.CSS_SELECTOR, 'body']
    DZEN_PAGE = [By.XPATH, '//*[@id="LayoutContentMicroRoot"]']

    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']
