import time
import unittest
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.login_page import LoginPage
from saucedemo_website.logic.home_page import HomePage


class TestHomePage(unittest.TestCase):

    def test_backpack_add_button(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/")
        time.sleep(3)
        home_page = HomePage(driver)
        # home_page.login_flow("standard_user", "secret_sauce")
        home_page.click_on_add_to_cart_button_backpack()

    def test_bike_add_button(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/inventory.html")
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_bike_light()

    def test_t_shirt_add_button(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/inventory.html")
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_t_shirt()

