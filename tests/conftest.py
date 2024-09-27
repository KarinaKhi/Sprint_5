import random
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def open_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver


@pytest.fixture
def open_forgot_password_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    return driver


@pytest.fixture()
def unique_email():
    first_name = "many"
    last_name = "mansov"
    cohort_number = "14"
    random_number = random.randint(100, 999)
    email_domain = "yandex.ru"
    return f"{first_name}_{last_name}_{cohort_number}_{random_number}@{email_domain}"
