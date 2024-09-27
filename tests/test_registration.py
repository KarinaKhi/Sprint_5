from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_DATA_FOR_REGISTRATION


def test_successful_registration(driver, open_main_page, unique_email):
    login_button_main_page = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    login_button_main_page.click()
    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()
    name_input = driver.find_element(*Locators.NAME_INPUT)
    name_input.send_keys(USER_DATA_FOR_REGISTRATION['full_name'])
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    email_input.send_keys(unique_email)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys(USER_DATA_FOR_REGISTRATION['password'])
    register_button = driver.find_element(*Locators.REGISTER_BUTTON)
    register_button.click()
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.REGISTRATION_SUCCESS_MESSAGE)
    )
    assert success_message, "Регистрация не удалась"


def test_password_error(driver, open_main_page, unique_email):
    main_page_login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    main_page_login_button.click()
    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()
    name_input = driver.find_element(*Locators.NAME_INPUT)
    name_input.send_keys(USER_DATA_FOR_REGISTRATION['full_name'])
    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    email_input.send_keys(unique_email)
    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys(USER_DATA_FOR_REGISTRATION['wrong_password'])
    register_button = driver.find_element(*Locators.REGISTER_BUTTON)
    register_button.click()
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)
    )
    assert "Некорректный пароль" in error_message.text, "Неверный текст ошибки пароля"
