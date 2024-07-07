from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from logic.login_page import LoginPage


class RegisterPage(LoginPage):
    REGISTER_BUTTON = '(//input[@type="submit"])[2]'
    FIRST_NAME_FIELD = '//input[@id="customer.firstName"]'
    LAST_NAME_FIELD = '//input[@id="customer.lastName"]'
    ADDRESS_FIELD = '//input[@id="customer.address.street"]'
    CITY_FIELD = '//input[@id="customer.address.city"]'
    STATE_FIELD = '//input[@id="customer.address.state"]'
    ZIP_CODE_FIELD = '//input[@id="customer.address.zipCode"]'
    PHONE_FIELD = '//input[@id="customer.phoneNumber"]'
    SSN_FIELD = '//input[@id="customer.ssn"]'
    USERNAME_FIELD = '//input[@id="customer.username"]'
    PASSWORD_FIELD = '//input[@id="customer.password"]'
    CONFIRM_FIELD = '//input[@id="repeatedPassword"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)
            self._first_name_field = self._driver.find_element(By.XPATH, self.FIRST_NAME_FIELD)
            self._last_name_field = self._driver.find_element(By.XPATH, self.LAST_NAME_FIELD)
            self._address_field = self._driver.find_element(By.XPATH, self.ADDRESS_FIELD)
            self._city_field = self._driver.find_element(By.XPATH, self.CITY_FIELD)
            self._state_field = self._driver.find_element(By.XPATH, self.STATE_FIELD)
            self._zip_code_field = self._driver.find_element(By.XPATH, self.ZIP_CODE_FIELD)
            self._phone_field = self._driver.find_element(By.XPATH, self.PHONE_FIELD)
            self._ssn_field = self._driver.find_element(By.XPATH, self.SSN_FIELD)
            self._username_field = self._driver.find_element(By.XPATH, self.USERNAME_FIELD)
            self._password_field = self._driver.find_element(By.XPATH, self.PASSWORD_FIELD)
            self._confirm_field = self._driver.find_element(By.XPATH, self.CONFIRM_FIELD)

        except NoSuchElementException as e:
            print("Element not found", e)

    def click_on_register_button(self):
        self._register_button.click()

    def fill_first_name_field(self, first_name):
        self._first_name_field.send_keys(first_name)

    def fill_last_name_field(self, last_name):
        self._last_name_field.send_keys(last_name)

    def fill_address_field(self, address):
        self._address_field.send_keys(address)

    def fill_city_field(self, city):
        self._city_field.send_keys(city)

    def fill_state_field(self, state):
        self._state_field.send_keys(state)

    def fill_zip_code_field(self, zip_code):
        self._zip_code_field.send_keys(zip_code)

    def fill_phone_field(self, phone):
        self._phone_field.send_keys(phone)

    def fill_ssn_field(self, ssn):
        self._ssn_field.send_keys(ssn)

    def fill_username_field(self, username):
        self._username_field.send_keys(username)

    def fill_password_field(self, password):
        self._password_field.send_keys(password)

    def fill_confirm_field(self, confirm):
        self._confirm_field.send_keys(confirm)

    def fill_all_inputs_flow(self, first_name, last_name, address, city, state,
                             zip_code, phone, ssn, username, password, confirm):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.fill_city_field(city)
        self.fill_state_field(state)
        self.fill_zip_code_field(zip_code)
        self.fill_phone_field(phone)
        self.fill_ssn_field(ssn)
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.fill_confirm_field(confirm)