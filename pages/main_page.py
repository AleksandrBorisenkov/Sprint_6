import allure

from urls import URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def main_page_url(self):
        return self.get_url(URL.MAIN_URL)

    @allure.step('Берем актуальную страницу')
    def take_current_url(self):
        return self.current_url

    def find_qa_form(self):
        self.find_elements_with_wait(MainPageLocators.QA_FORM)

    def wait_order_button_midle(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)

    def click_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_midle(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Скроллим до 8 вопроса, что == самый низ страницы')
    def scroll_to_qa(self):
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_7)

    @allure.step('Если баннер куки нашелся, нажали принять и забыли про нее.')
    def cookie_finder(self):
        if self.find_element_with_wait(MainPageLocators.COOKIE_BUTTON):
            return self.click_on_element(MainPageLocators.COOKIE_BUTTON)
        else:
            pass

    @allure.step('Щелкаем по вопросу')
    def click_on_question(self, num):
        q_locator = self.formating_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(q_locator)

    @allure.step('Получаем текст ответа')
    def get_text_from_answer(self, num):
        a_locator = self.formating_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(a_locator)

    @allure.step('Кликнули по вопросу и получили ответ')
    def click_to_question_and_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_from_answer(num)

    @allure.step('Находим лого Яндекс и переходим на новую вкладку')
    def go_dzen(self):
        self.find_element_with_wait(MainPageLocators.YA_LOGO)
        self.click_on_element(MainPageLocators.YA_LOGO)
        self.send_tab_key(1)
        self.find_elements_with_wait(MainPageLocators.DZEN_PAGE)
        return self.current_url()

    def return_to_main_page(self):
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO)