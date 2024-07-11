import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.login_page import LoginPage
from logic.base_page_app import BasePageApp


class TestBasePageApp(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.config["password"])

    def tearDown(self):
        self.driver.quit()

    def test_create_button(self):
        base_page_app = BasePageApp(self.driver)
        base_page_app.click_on_create_button()

    def test_opening_new_project_window(self):
        base_page_app = BasePageApp(self.driver)
        base_page_app.open_new_project()
        time.sleep(5)
