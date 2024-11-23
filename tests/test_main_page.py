import allure

from pages.main_page import MainPage

@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Сдать анализы' в хедере")
def test_catalog_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Сдать анализы'"):
        main_page.check_catalog_from_header()

@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Выезд на дом' в хедере")
def test_ms_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Выезд на дом'"):
        main_page.check_ms_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Запись к врачу' в хедере")
def test_appointment_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Запись к врачу'"):
        main_page.check_appointment_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Скидки и акции' в хедере")
def test_promo_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Скидки и акции'"):
        main_page.check_promo_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Адреса Центров Хеликс' в хедере")
def test_centers_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Адреса Центров Хеликс'"):
        main_page.check_centers_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Helixbook' в хедере")
def test_kb_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Helixbook'"):
        main_page.check_kb_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Сервисы' в хедере")
def test_services_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Сервисы'"):
        main_page.check_services_from_header()


@allure.feature("Главная страница")
@allure.story("Наличие вкладки 'Еще' в хедере")
def test_info_from_header(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить наличие вкладки 'Еще'"):
        main_page.check_info_from_header()

@allure.feature("Главная страница")
@allure.story("Смена города")
def test_change_city(browser_driver):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage()
        main_page.open_page_with_confirm("")
    with allure.step("Проверить смену города на Москву"):
        main_page.check_change_city()