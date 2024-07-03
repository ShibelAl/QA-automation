import time

from selenium.webdriver.common.by import By
from katalon_demo_cura_website.logic.base_page_app import BasePageApp


class HomePage(BasePageApp):
    MAKE_APPOINTMENT_BUTTON = "//a[@id='btn-make-appointment']"
    MAIL_BUTTON = "//a[contains(text(), 'info@katalon.com')]"
    FACEBOOK_BUTTON = "//i[@class='fa fa-facebook fa-fw fa-3x']"
    TWITTER_BUTTON = "//i[@class='fa fa-twitter fa-fw fa-3x']"
    DRIBBBLE_BUTTON = "//i[@class='fa fa-dribbble fa-fw fa-3x']"

    def __init__(self,driver):
        super().__init__(driver)
        self._make_appointment_button = self._driver.find_element(By.XPATH, self.MAKE_APPOINTMENT_BUTTON)
        self._mail_button = self._driver.find_element(By.XPATH, self.MAIL_BUTTON)
        self._facebook_button = self._driver.find_element(By.XPATH, self.FACEBOOK_BUTTON)
        self._twitter_button = self._driver.find_element(By.XPATH, self.TWITTER_BUTTON)
        self._dribbble_button = self._driver.find_element(By.XPATH, self.DRIBBBLE_BUTTON)

    def click_on_make_appointment(self):
        self._make_appointment_button.click()
        time.sleep(2)

    def click_on_mail_button(self):
        self._mail_button.click()
        time.sleep(2)

    def click_on_facebook_button(self):
        self._facebook_button.click()
        time.sleep(2)

    def click_on_twitter_button(self):
        self._twitter_button.click()
        time.sleep(2)

    def click_on_dribbble_button(self):
        self._dribbble_button.click()
        time.sleep(2)

    def return_to_home_page(self):
        super()._driver.get("https://katalon-demo-cura.herokuapp.com/#")

