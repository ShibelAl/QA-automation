import time
import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.secret = ConfigProvider.load_secret_json()
        self.driver = self.browser.get_driver(self.config["base_url"])

    def tearDown(self):
        self.driver.quit()

    def test_login_flow(self):
        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config["email"], self.secret["password"])
        self.assertTrue(self.driver.current_url, "https://app.asana.com/0/1207765960679171/list")
