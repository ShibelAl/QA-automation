import time
import unittest
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.shorts_page import ShortsPage


class TestShortsPage(unittest.TestCase):

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
        time.sleep(8)
        self.home_page = HomePage(self.driver)

    # After all - Called automatically
    def tearDown(self):
        self.driver.quit()

    def test_more_options_button(self):

        self.home_page.click_on_shorts_button_full_page()
        time.sleep(4)
        shorts_page = ShortsPage(self.driver)
        shorts_page.click_on_more_options_button()
        time.sleep(2)
        shorts_page.click_on_description_button()
        time.sleep(2)
        self.assertTrue(shorts_page.description_is_displayed())

