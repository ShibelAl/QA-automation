import time
import unittest
from saucedemo_website.infra.config_provider import ConfigProvider
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.login_page import LoginPage
from saucedemo_website.logic.home_page import HomePage


class TestHomePage(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def test_add_backpack_to_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_backpack()
        time.sleep(1)
        driver.quit()

    def test_add_bike_to_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_bike_light()
        time.sleep(1)
        driver.quit()

    def test_add_t_shirt_to_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_t_shirt()
        time.sleep(1)
        driver.quit()

    def test_backpack_title_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_title()
        time.sleep(1)
        driver.quit()

    def test_backpack_image_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_image()
        time.sleep(1)
        driver.quit()

    def test_bike_light_title_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_bike_light_item_title()
        time.sleep(1)
        driver.quit()

    def test_bike_light_image_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_bike_light_item_image()
        time.sleep(1)
        driver.quit()

    def test_black_t_shirt_title_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_t_shirt_item_title()
        time.sleep(1)
        driver.quit()

    def test_black_t_shirt_image_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_t_shirt_item_image()
        time.sleep(1)
        driver.quit()