import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@title="Вход"]')
    QR_TAB = (By.XPATH, '//*[@title="QR-код"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//button[@label="Войти"]')
    LOGIN_BUTTON_BY_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    LOGIN_BUTTON_NOT_ENTER = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    BUTTON_SIGN_IN = (By.XPATH, '//div[@class="LoginFormMain-module__bottom___YLtCo"]//span[@class="vkuiButton__in"]')
    BUTTON_SIGN_IN_BY_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    BUTTON_SIGN_IN_BY_MAIL = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    BUTTON_SIGN_IN_BY_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="LoginForm-module__error___1xmAD vkuiCaption__sizeYNone vkuiCaption__level1 vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')
    RESTORE_LINK = (By.XPATH, '//span[text()="Восстановить"]')
    BUTTON_CANCEL = (By.XPATH, '//button[.//span[text()="Отмена"]]')

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # вызов функции делаем в конструктор, чтобы делалось автоматически
    # паттерн pageObject, когда каждая страница является отдельным объектом, под нее заводится класс, описываются все элементы,
    # которые есть конректно на этой странице, описываются все функции, действия, которые делаются на этой странице
    # (кликнуть, заполнить поле, др.). Каждый экран - это новая страница. PageObject - страница-объект, все разделено.
    # Одна страница - один класс.Не смешиваем страницы. На каждой странице свои локаторы. Каждая страница считается отдельным объектом.
    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы входа'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_BY_QR)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_NOT_ENTER)
        self.find_element(LoginPageLocators.BUTTON_SIGN_IN)
        self.find_element(LoginPageLocators.BUTTON_SIGN_IN_BY_VK)
        self.find_element(LoginPageLocators.BUTTON_SIGN_IN_BY_MAIL)
        self.find_element(LoginPageLocators.BUTTON_SIGN_IN_BY_YANDEX)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        # self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
    #     click() - отдельный класс webelement-а, которому доступны различные свойства (кликнуть, очистить, получить атрибут который в DOM-е есть, отправить текст, др.)

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text
    # без скобок, возвращаем просто текст

    @allure.step('Заполняем поле логин')
    def type_login(self, login: str):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def type_password(self, password: str):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_LINK).click()

    @allure.step('Переходим на страницу регистрации')
    def click_registration(self):
        self.driver.get("https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone")
