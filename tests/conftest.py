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
