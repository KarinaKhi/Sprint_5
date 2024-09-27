from locators import Locators


def test_bun_section_active(driver, open_main_page):
    driver.find_element(*Locators.FILLING_SECTION).click()
    driver.find_element(*Locators.BUN_SECTION).click()
    active_bun_section = driver.find_element(*Locators.ACTIVE_BUN_SECTION)
    assert active_bun_section is not None, "Раздел 'Булки' не активен"


def test_sauce_section_active(driver, open_main_page):
    driver.find_element(*Locators.SAUCE_SECTION).click()
    active_sauce_section = driver.find_element(*Locators.ACTIVE_SAUCE_SECTION)
    assert active_sauce_section is not None, "Раздел 'Соусы' не активен"


def test_filling_section_active(driver, open_main_page):
    driver.find_element(*Locators.FILLING_SECTION).click()
    active_filling_section = driver.find_element(*Locators.ACTIVE_FILLING_SECTION)
    assert active_filling_section is not None, "Раздел 'Начинки' не активен"
