import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    with (allure.step(f'Открываем страницу {BASE_URL}')):
        BasePage = BasePageHelper(browser)
        BasePage.get_url(BASE_URL)
        BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    with allure.step('Запоминаем ID текущей вкладки'):
        current_window_id = LoginPage.get_window_id(0)
    with (allure.step(f'Нажимаем кнопку экосистемы VK')):
        LoginPage.click_vk_ecosystem()
    with allure.step('Нажимаем кнопку экосистемы VK'):
        LoginPage.click_more_button()
    with allure.step('Получаем ID новой вкладки'):
        new_window_id = LoginPage.get_window_id(1)
    with (allure.step(f'Переходим на вкладку экосистемы VK')):
        LoginPage.switch_window(new_window_id)
    VKEcosystemPage = VKEcosystemPageHelper(browser)
    with allure.step(f'Возвращаемся обратно на основную вкладку'):
        VKEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)
