from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_CREDENTIALS


def test_logout_personal_account(driver, open_main_page):
    login_button_personal_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    )
    login_button_personal_account.click()
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()
    login_button_personal_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    )
    login_button_personal_account.click()
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
    )
    logout_button.click()
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.LOGIN_BUTTON_REGISTRATION_FORM)
    )
    assert login_button is not None, "Не удалось выйти из аккаунта."
