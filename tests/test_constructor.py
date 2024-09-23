from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_bun_section_active(driver, open_main_page):
    filling_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.FILLING_SECTION)
    )
    filling_section.click()

    bun_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.BUN_SECTION)
    )

    bun_section.click()

    active_bun_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ACTIVE_BUN_SECTION)
    )
    assert active_bun_section is not None, "Раздел 'Булки' не активен"
    print("Тест на активность раздела 'Булки' пройден успешно!")


def test_sauce_section_active(driver, open_main_page):
    sauce_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.SAUCE_SECTION)
    )
    sauce_section.click()

    active_sauce_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ACTIVE_SAUCE_SECTION)
    )
    assert active_sauce_section is not None, "Раздел 'Соусы' не активен"
    print("Тест на активность раздела 'Соусы' пройден успешно!")


def test_filling_section_active(driver, open_main_page):
    filling_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.FILLING_SECTION)
    )
    filling_section.click()

    active_filling_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ACTIVE_FILLING_SECTION)
    )
    assert active_filling_section is not None, "Раздел 'Начинки' не активен"
    print("Тест на активность раздела 'Начинки' пройден успешно!")
