import allure
import pytest

from urls import URL
from data_help import AnswerText

class TestMainPage:

    @pytest.mark.parametrize(
        'num,expected_result',
        [
            (0, AnswerText.ANSWER_1),
            (1, AnswerText.ANSWER_2),
            (2, AnswerText.ANSWER_3),
            (3, AnswerText.ANSWER_4),
            (4, AnswerText.ANSWER_5),
            (5, AnswerText.ANSWER_6),
            (6, AnswerText.ANSWER_7),
            (7, AnswerText.ANSWER_8)
        ]
    )

    @allure.title('Методом клика на вопрос получяем и сравниваем текст каждого ответа по порядку используя параметризацию')
    def test_check_qa_text(self, main_page, num, expected_result):
        main_page.cookie_finder()
        main_page.find_qa_form()
        main_page.scroll_to_qa()
        result = main_page.click_to_question_and_answer_text(num)
        assert result == expected_result

    @allure.title('С главной страницы через лого Яндекс делаем переход на новую вкладку страницы DZEN и сверяем полученный URL')
    def test_change_page(self, main_page):
        main_page.cookie_finder()
        dzen = main_page.go_dzen()
        assert dzen == URL.DZEN_URL
