# Sprint 6

Тесты сделаны для браузера FireFox. Там некоторых багов нет в сравнении с хромом.

Что в тестах:
Проверка соответствия ответа на указанный вопрос.
Проверка создания заказа с главной страницы, заходим на страницу созданного заказа и кликаем по лого самоката,
возвращаясь на главную станицу.
Создание заказа со страницы заказа и убеждаемся, что появилась форма с успешным созданием заказа.


Файл requirements.txt содержит необходимые плагины для выполнения тестов.

Запуск всех тестов с генерацией отчетов командой:
python -m pytest --alluredir allure-results

Просмотреть полученные отчеты командой:
allure serve allure-results