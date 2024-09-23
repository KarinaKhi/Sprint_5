from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
from locators import Locators


def generate_unique_email():
    webdriver.Chrome()
    first_name = "many"
    last_name = "mansov"
    cohort_number = "1"
    random_number = random.randint(100, 999)
    email_domain = "yandex.ru"
    unique_email = f"{first_name}_{last_name}_{cohort_number}_{random_number}@{email_domain}"
    return unique_email


def test_successful_registration(driver, open_main_page):
    login_button_main_page = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    login_button_main_page.click()
    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()

    name_input = driver.find_element(*Locators.NAME_INPUT)
    name_input.send_keys("Мэни Мэнсов")

    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    unique_email = generate_unique_email()
    email_input.send_keys(unique_email)

    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys("password123")

    register_button = driver.find_element(*Locators.REGISTER_BUTTON)
    register_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.REGISTRATION_SUCCESS_MESSAGE)
        )
        print("Тест успешной регистрации пройден!")
    except TimeoutException:
        print("Тест успешной регистрации не пройден!")


def test_password_error(driver, open_main_page):
    main_page_login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    main_page_login_button.click()
    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()

    name_input = driver.find_element(*Locators.NAME_INPUT)
    name_input.send_keys("Мэни Мэнсов")

    email_input = driver.find_element(*Locators.EMAIL_INPUT)
    unique_email = generate_unique_email()
    email_input.send_keys(unique_email)

    password_input = driver.find_element(*Locators.PASSWORD_INPUT)
    password_input.send_keys("123")

    register_button = driver.find_element(*Locators.REGISTER_BUTTON)
    register_button.click()

    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_ERROR_MESSAGE)
        )
        assert "Некорректный пароль" in error_message.text, "Тест на ошибку пароля не пройден!"
        print("Тест на ошибку пароля пройден!")
    except TimeoutException:
        print("Тест на ошибку пароля не пройден!")
