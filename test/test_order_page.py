import allure
import pytest

from URLS import URL


class TestOrderPage:

    @allure.step('Через главную страницу создали заказ и вернулись на главную через лого самоката')
    def test_crate_order_from_main_page_top_button(self, main_page, order_page, f_name_generator, l_name_generator, address_generator, phone_generator):
        main_page.cookie_finder()
        main_page.click_order_button_top()
        order_page.fill_order_form_name_for_whom(f_name_generator, l_name_generator, address_generator, phone_generator)
        order_page.fill_order_form_name_about_rent('28.12.2035')
        order_page.confirm_order()
        text_form = order_page.confirm_order_form_text()
        assert "Номер заказа:" in text_form
        order_page.go_to_status_order()
        text = order_page.order_status()
        assert text == "Отменить заказ"
        order_page.return_to_main_page()
        check_url = main_page.current_url()
        assert check_url == URL.MAIN_URL

    @allure.step('Создание заказа со страницы заказать и ожидание появление формы с номером заказа')
    def test_crate_order_from_order_page(self, order_page, f_name_generator, l_name_generator, address_generator, phone_generator):
        order_page.cookie_finder()
        order_page.fill_order_form_name_for_whom(f_name_generator, l_name_generator, address_generator, phone_generator)
        order_page.fill_order_form_name_about_rent('28.12.2034')
        order_page.confirm_order()
        text_form = order_page.confirm_order_form_text()
        assert "Номер заказа:" in text_form
