import allure
import pytest

from urls import URL
import data_help


class TestOrderPage:

    @allure.title('Полный путь от создания заказа с главной страницы и до возврата на главную через лого самоката')
    def test_crate_order_from_main_page_top_button(self, main_page, order_page):
        main_page.cookie_finder()
        main_page.click_order_button_top()
        order_page.fill_order_form_name_for_whom(data_help.f_name_generator(), data_help.l_name_generator(), data_help.address_generator(), data_help.phone_generator())
        order_page.fill_order_form_name_about_rent('28.12.2035')
        order_page.confirm_order()
        text_form = order_page.confirm_order_form_text()
        assert "Номер заказа:" in text_form
        order_page.go_to_status_order()
        text = order_page.order_status()
        assert text == "Отменить заказ"
        main_page.return_to_main_page()
        check_url = main_page.current_url()
        assert check_url == URL.MAIN_URL

    @allure.title('Со страницы заказа оформляем новый заказ и ожидаем появления формы с номером заказа')
    def test_crate_order_from_order_page(self, order_page):
        order_page.cookie_finder()
        order_page.fill_order_form_name_for_whom(data_help.f_name_generator(), data_help.l_name_generator(), data_help.address_generator(), data_help.phone_generator())
        order_page.fill_order_form_name_about_rent('28.12.2034')
        order_page.confirm_order()
        text_form = order_page.confirm_order_form_text()
        assert "Номер заказа:" in text_form
