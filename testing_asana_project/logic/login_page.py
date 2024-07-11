import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class LoginPage(BasePage):
    ASANA_GMAIL_INPUT = ('//input[@class = "TextInputBase SizedTextInput SizedTextInput--medium TextInput TextInput-'
                         '-medium LoginEmailForm-emailInput"]')
    ASANA_CONTINUE_BUTTON = '//div[text() = "Continue"]'
    ASANA_PASSWORD_INPUT = '//input[@autocomplete = "current-password"]'
    ASANA_LOGIN_BUTTON = '//div[text() = "Log in"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._asana_gmail_input = self._driver.find_element(By.XPATH, self.ASANA_GMAIL_INPUT)
        self._asana_continue_button = self._driver.find_element(By.XPATH, self.ASANA_CONTINUE_BUTTON)
        self._asana_password_input = None
        self._asana_login_button = None

    def fill_email_input(self, email):
        self._asana_gmail_input.send_keys(email)

    def click_on_continue_button(self):
        self._asana_continue_button.click()

    def fill_password_input(self, password):
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ASANA_PASSWORD_INPUT))
        ).send_keys(password)
        # self._asana_password_input.send_keys(password)

    def click_on_login_button(self):
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ASANA_LOGIN_BUTTON))
        ).click()

    def login_flow(self, email, password):
        self.fill_email_input(email)
        self.click_on_continue_button()
        self.fill_password_input(password)
        self.click_on_login_button()

