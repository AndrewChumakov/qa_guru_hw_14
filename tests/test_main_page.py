import allure

from pages.main_page import MainPage


def test_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page("")

