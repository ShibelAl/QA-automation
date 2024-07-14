import logging
import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from infra.logging_setup import LoggingSetup


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        """
        Sets up the testing environment, opens the browser on the login page.
        Works automatically.
        """
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.secret = ConfigProvider.load_secret_json()
        self.driver = self.browser.get_driver(self.config["base_url"])

    def tearDown(self):
        """
        Closes the browser after completing the test.
        Works automatically.
        """
        self.driver.quit()

    def test_correct_login_flow(self):
        """
        This function tests if after inserting a correct email and password
        the main page of the website appears.
        """
        logging.info("Test correct login flow - Test started")
        # Arrange
        login_page = LoginPage(self.driver)
        # Act
        login_page.login_flow(self.config["email"], self.secret["password"])
        WebDriverWait(self.driver, 5).until(EC.url_to_be("https://app.asana.com/0/home/1207765960679158"))
        # Assert
        self.assertEqual(self.driver.current_url, "https://app.asana.com/0/home/1207765960679158")

    def test_wrong_password_in_login(self):
        """
        This function tests if when inserting a correct email and wrong password,
        then the login page prevents entering the website, as it should.
        """
        logging.info("Test wrong password in login - test started")
        # Arrange
        login_page = LoginPage(self.driver)
        # Act
        login_page.login_flow(self.config["email"], self.secret["wrong_password"])
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be("https://app.asana.com/0/home/1207765960679158"))
        except TimeoutException:
            # Assert
            self.assertNotEqual(self.driver.current_url, "https://app.asana.com/0/home/1207765960679158")

    def test_wrong_email_in_login(self):
        """
        This function tests if when inserting a wrong email, then
        the login page prevents entering the website, as it should.
        """
        logging.info("Test wrong email in login - test started")
        # Arrange
        login_page = LoginPage(self.driver)
        # Act
        login_page.fill_email_input(self.config["wrong_email"])
        login_page.click_on_continue_button()
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be("https://app.asana.com/0/home/1207765960679158"))
        except TimeoutException:
            # Assert
            self.assertNotEqual(self.driver.current_url, "https://app.asana.com/0/home/1207765960679158")
