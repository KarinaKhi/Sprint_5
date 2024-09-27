from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_CREDENTIALS


def test_login_main_page(driver, open_main_page):
    login_button_main_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN_PAGE)
    )
    login_button_main_page.click()
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()
    order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button is not None, "Не удалось войти через главную страницу."


def test_login_personal_account(driver, open_main_page):
    login_button_personal_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    )
    login_button_personal_account.click()
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()
    order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button is not None, "Не удалось войти через кнопку 'личный кабинет'."


def test_login_from_registration_form(driver, open_main_page):
    main_page_login_button = driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE)
    main_page_login_button.click()
    register_link = driver.find_element(*Locators.REGISTER_LINK)
    register_link.click()
    login_link_on_registration_form = driver.find_element(*Locators.LOGIN_LINK_ON_REGISTRATION_FORM)
    login_link_on_registration_form.click()
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()
    order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button is not None, "Не удалось войти через страницу регистрации."


def test_login_from_password_recovery_form(driver, open_forgot_password_page):
    login_button = driver.find_element(*Locators.LOGIN_BUTTON_PASSWORD_RECOVERY_FORM)
    login_button.click()
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()
    order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button is not None, "Не удалось войти через форму восстановления пароля."
