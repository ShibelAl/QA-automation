import time
import unittest
from infra.config_provider import ConfigProvider
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.video_page import VideoPage


class TestVideoPage(unittest.TestCase):

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
        time.sleep(4)
        self.login_page.fill_password_input(self.config["password"])
        time.sleep(3)
        self.login_page.click_on_next_button()
        time.sleep(10)
        self.home_page = HomePage(self.driver)

    # After all - Called automatically
    def tearDown(self):
        self.driver.quit()

    def test_like_button_after_pressing_twice(self):

        self.home_page.fill_search_input("mrbeast")
        time.sleep(2)
        self.video_page = VideoPage(self.driver)
        self.video_page.click_on_video_link()
        time.sleep(5)
        self.video_page.click_on_like_button()
        time.sleep(3)
        self.assertTrue(self.video_page.like_emoji_is_displayed())
        time.sleep(2)

