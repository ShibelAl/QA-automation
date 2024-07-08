import time
import unittest
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.menu_page import MenuPage
from logic.login_page import LoginPage


class TestMenuPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["base_url"])
        self.home_page = HomePage(self.driver)
        self.home_page.click_on_login_button()
        self.login_page = LoginPage(self.driver)
        self.login_page.fill_username_input(self.config["email"])
        self.login_page.click_on_next_button()
        time.sleep(3)
        self.login_page.fill_password_input(self.config["password"])
        time.sleep(3)
        self.login_page.click_on_next_button()
        time.sleep(6)

    # After all - Called automatically
    def tearDown(self):
        self.driver.quit()

    def test_sections_numbers_in_menu(self):

        self.menu_page = MenuPage(self.driver)
        self.assertEqual(self.menu_page.count_menu_sections(), 5)
        time.sleep(2)