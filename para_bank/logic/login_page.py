from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium.common.exceptions import *


class LoginPage(BasePageApp):
    USERNAME_FIELD = '//input[@name="username"]'
    PASSWORD_FIELD = '//input[@name="password"]'
    SUBMIT_BUTTON = '//button[@id="submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._username_field = self._driver.find_element(By.XPATH, self.USERNAME_FIELD)
            self._password_field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
            self._submit_button = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        except NoSuchElementException as e:
            print("Element not found", e)

    def fill_user_name_input(self, username):
        self._username_field.send_keys(username)

    def fill_password_input(self, password):
        self._password_field.send_keys(password)

    def click_on_login_button(self):
        self._submit_button.click()