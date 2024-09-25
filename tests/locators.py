from selenium.webdriver.common.by import By


class Locators:
    # Регистрация
    NAME_INPUT = (By.XPATH, "//fieldset[1]//input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]//input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]//input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка некорректного пароля
    REGISTRATION_SUCCESS_MESSAGE = (By.XPATH, "//h2[text()='Вход']")  # Сообщение об успешной регистрации
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # переход на страницу регистрации со страницы входа

    # Вход в аккаунт
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка на главной для входа
    LOGIN_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']")  # Кнопка Личный кабинет
    LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//button[text()='Войти']")  # Кнопка в форме регистрации
    LOGIN_BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, "//a[text()='Войти']")  # Кнопка в форме восстановления пароля
    EMAIL_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, "//input[@name='name']")  # Поле ввода email при входе
    PASSWORD_INPUT_LOGIN_MAIN_PAGE = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля при входе
    LOGIN_LINK_ON_REGISTRATION_FORM = (By.XPATH, "//a[@href='/login']")  # Кнопка входа на странице регистрации

    # Личный кабинет
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка Оформления заказа
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Кнопка Профиля в личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Переход в Конструктор
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers

    # Разделы Конструктора
    BURGER_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")  # Эаголовок блока конструктора
    BUN_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']")  # Раздел Булки
    SAUCE_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Раздел Соусы
    FILLING_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Раздел Начинки

    # Локаторы активного раздела после клика
    ACTIVE_BUN_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    ACTIVE_SAUCE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    ACTIVE_FILLING_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")
