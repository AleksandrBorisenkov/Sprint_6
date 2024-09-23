from selenium.webdriver.common.by import By

# Много локаторов для страницы заказа и её форм. Да, я так вижу.
class OrderPageLocators:
    HEADER_MAIN = [By.CLASS_NAME, 'Header_Header__214zg']
    FIRST_PART = [By.CLASS_NAME, 'Home_FirstPart__3g6vG']

    ORDER_FORM_FOR_WHOM = By.XPATH, '//*[text() = "Для кого самокат"]'
    ORDER_FORM_ABOUT_RENT = [By.XPATH, '//*[@class="Order_Header__BZXOb" and (text() = "Про аренду")]']
    ORDER_FORM = [By.CLASS_NAME, 'Order_Form__17u6u']
    NEXT_BUTTON = [By.XPATH, '//button[text()="Далее"]']
    ORDER_BUTTON = [By.XPATH, '//button[text()="Заказать"]']

    FNAME = [By.XPATH, '//input[@placeholder="* Имя"]']
    LNAME = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    TELEPHONE = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    METRO_STATIONS = [By.CLASS_NAME, 'select-search__input']
    METRO_STATIONS_LIST = [By.XPATH, '//*[@class="Order_Text__2broi" and (text()="Сокольники")]']

    DDMMYY = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    MONTH_CALENDAR = [By.CLASS_NAME, 'react-datepicker__month-container']
    DROP_DOWN_MENU_RENT = [By.XPATH, '//*[@class="Dropdown-placeholder" and (text()="* Срок аренды")]']
    HOW_MUCH_DAYS = [By.XPATH, '//*[@class="Dropdown-option" and (text()="двое суток")]']
    FINAL_ORDER_BUTTON = [By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Заказать")]']

    BLACK_SCOOTER = [By.ID, 'black']
    GREY_SCOOTER = [By.ID, 'grey']

    ORDER_CONFIRM_YES = [By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Да")]']
    ORDER_CONFIRM_NO = [By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i" and (text()="Нет")]']
    WATCH_STATUS_ORDER = [By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Посмотреть статус")]']
    ORDER_CANCEL = [By.XPATH, '//button[text()="Отменить заказ"]']
    SUCCESSFUL_FORM = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    NUM_ORDER= [By.XPATH,'//*[text()="Номер заказа: "]']
    TRACKER_ORDER = [By.XPATH, '//*[text() = "Отменить заказ"]']

    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']
    