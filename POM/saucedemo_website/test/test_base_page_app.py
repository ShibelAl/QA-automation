import time
import unittest
from saucedemo_website.infra.config_provider import ConfigProvider
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.base_page_app import BasePageApp
from saucedemo_website.logic.login_page import LoginPage


class TestBasePageApp(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def test_cart_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(1)
        driver.quit()

    def test_the_menu_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_menu_button()
        time.sleep(1)
        driver.quit()

    def test_all_items_button_in_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_menu_button()
        time.sleep(1)
        base_page_app.click_on_all_items_button_in_menu()
        time.sleep(1)
        driver.quit()

    def test_about_button_in_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_menu_button()
        time.sleep(1)
        base_page_app.click_on_about_button_in_menu()
        time.sleep(1)
        driver.quit()

    def test_logout_button_in_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_menu_button()
        time.sleep(1)
        base_page_app.click_on_logout_button_in_menu()
        time.sleep(1)
        driver.quit()

    def test_reset_button_in_menu(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_menu_button()
        time.sleep(1)
        base_page_app.click_on_reset_button_in_menu()
        time.sleep(1)
        driver.quit()

    def test_twitter_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_twitter_button()
        time.sleep(5)
        driver.quit()

    def test_facebook_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_facebook_button()
        time.sleep(5)
        driver.quit()

    def test_linkedin_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_linkedin_button()
        time.sleep(5)
        driver.quit()

    def test_header_text(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        assert base_page_app.get_header_text() == "Swag Labs"
        time.sleep(3)
        driver.quit()
