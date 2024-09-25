from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import USER_CREDENTIALS


def test_navigation_to_personal_account_for_authorized_user(driver, open_main_page):
    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    driver.find_element(*Locators.EMAIL_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["email"])
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_MAIN_PAGE).send_keys(USER_CREDENTIALS["password"])

    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_FORM).click()

    login_button_personal_account = driver.find_element(*Locators.LOGIN_BUTTON_PERSONAL_ACCOUNT)
    login_button_personal_account.click()

    profile_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PROFILE_LINK)
    )
    assert profile_link is not None, "Кнопка 'личный кабинет' не привела на страницу пользователя"
