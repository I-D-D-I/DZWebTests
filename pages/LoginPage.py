from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_SELECT_ENTER = (By.XPATH, '//*[@title="Вход"]')
    LOGIN_SELECT_ENTER_BY_QR = (By.XPATH, '//*[@title="QR-код"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_BUTTON_BY_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    LOGIN_BUTTON_NOT_ENTER = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    LOGIN_BUTTON_SIGN_IN = (
        By.XPATH, '//*[@class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"]')
    LOGIN_BUTTON_BY_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_BUTTON_BY_MAIL = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_BUTTON_BY_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')


class LoginPageHelper(BasePage):
    pass
