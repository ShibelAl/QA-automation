import time
from selenium.webdriver.common.by import By
from saucedemo_website.infra.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def fill_user_name_input(self, username):
        self._user_name_input.clear()
        self._user_name_input.send_keys(username)
        time.sleep(1)

    def fill_password_input(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)
        time.sleep(1)

    def click_submit_button(self):
        self._login_button.click()
        time.sleep(1)

    def login_flow(self, username, password):
        self._user_name_input.clear()
        self._password_input.clear()

        self.fill_user_name_input(username)
        time.sleep(1)
        self.fill_password_input(password)
        time.sleep(1)
        self.click_submit_button()
        time.sleep(1)
