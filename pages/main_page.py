from selene import browser, have, be


class MainPage:
    def open_page(self, page):
        browser.open(page)

    def confirm_city(self):
        browser.element("//button[@data-testid='confirm-city-button']").click()

    def open_page_with_confirm(self, page):
        self.open_page(page)
        self.confirm_city()

    def check_catalog_from_header(self):
        browser.element("//a[@data-testid='header-nav-catalog']").should(have.text("Сдать анализы"))

    def check_ms_from_header(self):
        browser.element("//a[@data-testid='header-nav-ms']").should(have.text("Выезд на дом"))

    def check_appointment_from_header(self):
        browser.element("//a[@data-testid='header-nav-practitioner-appointment']").should(have.text("Запись к врачу"))

    def check_promo_from_header(self):
        browser.element("//a[@data-testid='header-nav-promo']").should(have.text("Скидки и акции"))

    def check_centers_from_header(self):
        browser.element("//a[@data-testid='header-nav-centers']").should(have.text("Адреса Центров Хеликс"))

    def check_kb_from_header(self):
        browser.element("//a[@data-testid='header-nav-kb']").should(have.text("Helixbook"))

    def check_services_from_header(self):
        browser.element("//div[@data-testid='header-nav-services']/span").should(have.text("Сервисы"))

    def check_info_from_header(self):
        browser.element("//div[@data-testid='header-nav-info']/span").should(have.text("Еще"))

    def check_change_city(self):
        browser.element("//span[@data-testid='current-city']").click()
        browser.element("//span[@data-testid='important-city-0']").click()
        browser.element("//span[@data-testid='current-city']").should(have.text("Москва"))

