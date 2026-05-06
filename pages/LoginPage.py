from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@title="Вход"]')
    QR_TAB = (By.XPATH, '//*[@title="QR-код"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_BUTTON_BY_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    LOGIN_BUTTON_NOT_ENTER = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    BUTTON_SIGN_IN = (By.XPATH, '//div[@class="LoginFormMain-module__bottom___YLtCo"]//span[@class="vkuiButton__in"]')
    BUTTON_SIGN_IN_BY_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    BUTTON_SIGN_IN_BY_MAIL = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    BUTTON_SIGN_IN_BY_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="LoginForm-module__error___1xmAD vkuiCaption__sizeYNone vkuiCaption__level1 vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def get_error_password(self, login_value: str):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login_value)
