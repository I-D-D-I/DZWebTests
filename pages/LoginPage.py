from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_SELECT_ENTER = (By.XPATH, '//*[@id="login-687708430"]')
    LOGIN_SELECT_ENTER_BY_QR = (By.XPATH, '//*[@id="qrCode-687708493"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_BUTTON_BY_QR = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[1]/button')
    LOGIN_BUTTON_NOT_ENTER = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[1]/span/button')
    LOGIN_BUTTON_SIGN_IN = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[3]/button')
    LOGIN_BUTTON_BY_VK = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_BUTTON_BY_MAIL = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[2]/i')
    LOGIN_BUTTON_BY_YANDEX = (By.XPATH, '//*[@id="tabpanel-login-687708430"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[3]/i')

class LoginPageHelper(BasePage):
    pass