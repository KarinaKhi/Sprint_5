from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_CREDENTIALS


def test_navigation_click_on_constructor_button(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

    burger_heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.BURGER_HEADING)
    )
    assert burger_heading is not None, "Кнопка 'КОНСТРУКТОР' не привела на главную страницу"


def test_navigation_click_on_logo(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT).click()

    driver.find_element(*Locators.LOGO_BUTTON).click()

    order_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ORDER_BUTTON)
    )
    assert order_button is not None, "Клик по логотипу не привел на главную страницу"
