from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//a[@href="/help/reklamnyi-kabinet"]')


class AdvertisementCabinetHelpHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.find_element(AdvertisementCabinetHelpLocators.TITLE)
        self.attach_screenshot()
