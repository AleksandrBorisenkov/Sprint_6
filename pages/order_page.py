import allure

from urls import URL
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def order_page_url(self):
        return self.get_url(URL.ORDER_URL)

    @allure.step('Берем актуальную страницу')
    def take_current_url(self):
        return self.current_url

    @allure.step('')
    def wait_order_form_name_about_rent(self):
        self.find_element_with_wait(OrderPageLocators.ORDER_FORM_ABOUT_RENT)

    @allure.step('Заполняем форму "Для кого самокат"')
    # (можно разбить на шаги, что бы явно увидеть что оторвало. Но я не стал)
    def fill_order_form_name_for_whom(self, fname, lname, address, telephone):
        self.set_text_to_element(OrderPageLocators.FNAME, fname)
        self.set_text_to_element(OrderPageLocators.LNAME, lname)
        self.set_text_to_element(OrderPageLocators.ADDRESS, address)
        self.click_on_element(OrderPageLocators.METRO_STATIONS)
        self.click_on_element(OrderPageLocators.METRO_STATIONS_LIST)
        self.set_text_to_element(OrderPageLocators.TELEPHONE, telephone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму "Срок аренды"')
    # (можно разбить на шаги, что бы явно увидеть что оторвало. Но я не стал)
    def fill_order_form_name_about_rent(self, date):
        self.set_text_to_element(OrderPageLocators.DDMMYY, date)
        self.send_enter_key(OrderPageLocators.DDMMYY)
        self.click_on_element(OrderPageLocators.DROP_DOWN_MENU_RENT)
        self.find_elements_with_wait(OrderPageLocators.HOW_MUCH_DAYS)
        self.click_on_element(OrderPageLocators.HOW_MUCH_DAYS)
        self.click_on_element(OrderPageLocators.GREY_SCOOTER)
        self.click_on_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step('Оформляем заказ и убедились что форма появилась')
    # убедились что форма с заказом появилась.
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.ORDER_CONFIRM_YES)
        self.find_element_with_wait(OrderPageLocators.SUCCESSFUL_FORM)

    @allure.step('Получаем текст что заказ оформлен')
    def confirm_order_form_text(self):
        return self.get_text_from_element(OrderPageLocators.NUM_ORDER)

    @allure.step('Нажимаем "Посмотреть заказ"')
    # если нужно зашли в созданный заказ
    def go_to_status_order(self):
        self.find_element_with_wait(OrderPageLocators.WATCH_STATUS_ORDER)
        self.click_on_element(OrderPageLocators.WATCH_STATUS_ORDER)

    @allure.step('Проверяем что мы зашли внутрь страницы заказа использую локатор кнопки "отменить заказ"')
    # на странице созданного заказа проверили что страница верная
    # привязавшись к локатору кнопки "отменить заказ"
    def order_status(self):
        return self.get_text_from_element(OrderPageLocators.TRACKER_ORDER)

    @allure.step('Если баннер куки нашелся, нажали принять и забыли про нее.')
    def cookie_finder(self):
        if self.find_element_with_wait(OrderPageLocators.COOKIE_BUTTON):
            return self.click_on_element(OrderPageLocators.COOKIE_BUTTON)
        else:
            pass
