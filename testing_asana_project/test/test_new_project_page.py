import time
import unittest
from logic.login_page import LoginPage
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.base_page_app import BasePageApp
from logic.new_project_page import NewProjectPage


class TestNewProjectPage(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.secret = ConfigProvider.load_secret_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email"], self.secret["password"])
        self.base_page_app = BasePageApp(self.driver)
        self.base_page_app.open_new_project()

    def tearDown(self):
        self.driver.quit()

    def test_blank_project_button(self):
        new_project_page = NewProjectPage(self.driver)
        new_project_page.click_on_blank_project_button()
        self.assertEqual(self.driver.current_url, "https://app.asana.com/0/projects/new/blank")

