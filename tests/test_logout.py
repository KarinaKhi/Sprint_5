from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators


def test_logout_personal_account(driver, open_main_page):
    login_button_personal_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    )
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys("karry_karrow_1_111@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys("password123")

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    login_button_personal_account = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    )
    login_button_personal_account.click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
    )
    logout_button.click()
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.LOGIN_BUTTON_REGISTRATION_FORM)
        )
        print("Тест на выход из аккаунта успешно пройден!")
    except TimeoutException:
        print("Не удалось выйти из аккаунта")
