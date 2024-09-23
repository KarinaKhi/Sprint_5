from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators


def test_login_main_page(driver, open_main_page):
    login_button_main_page = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    login_button_main_page.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )
        print("Вход через главную страницу успешен!")
    except TimeoutException:
        print("Не удалось войти через главную страницу.")


def test_login_personal_account(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )
        print("Вход через кнопку 'личный кабинет' успешен!")
    except TimeoutException:
        print("Не удалось войти через кнопку 'личный кабинет'.")


def test_login_from_registration_form(driver, open_main_page):
    main_page_login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    main_page_login_button.click()

    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()

    login_link_on_registration_form = driver.find_element(*Locators.LOGIN_LINK_ON_REGISTRATION_FORM)
    login_link_on_registration_form.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")

    login_button_registration_form = driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM)
    login_button_registration_form.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )
        print("Вход через страницу регистрации успешен!")
    except TimeoutException:
        print("Не удалось войти через кнопку страницу регистрации.")


# в этом тесте я решила запустить проверку со страницы восстановления пароля
def test_login_from_password_recovery_form():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://stellarburgers.nomoreparties.site/forgot-password")

        login_button = driver.find_element(*Locators.LOGIN_BUTTON_PASSWORD_RECOVERY_FORM)
        login_button.click()

        driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")

        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.ORDER_BUTTON)
            )
            print("Вход через форму восстановления пароля успешен!")
        except TimeoutException:
            print("Не удалось войти через форму восстановления пароля.")
    finally:
        driver.quit()
