from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators


def test_navigation_click_on_constructor_button(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()
    constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
    constructor_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BURGER_HEADING)
        )
        print("Кнопка 'КОНСТРУКТОР' привела на главную страницу")
    except TimeoutException:
        print("Кнопка 'КОНСТРУКТОР' не привела на главную страницу")


def test_navigation_click_on_logo(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()

    logo_button = driver.find_element(*Locators.LOGO_BUTTON)
    logo_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ORDER_BUTTON)
        )
        print("Клик по логотипу привел на главную страницу")
    except TimeoutException:
        print("Клик по логотипу не привел на главную страницу")
