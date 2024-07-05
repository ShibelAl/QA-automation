import time
import unittest
from saucedemo_website.infra.config_provider import ConfigProvider
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.login_page import LoginPage
from saucedemo_website.logic.home_page import HomePage
from saucedemo_website.logic.item_page import ItemPage


class TestLoginPage(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def test_add_item_to_cart_in_item_page(self):
        """
        This function tests adding an item to cart from the item page
        """
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_title()
        time.sleep(1)
        item_page = ItemPage(driver)
        item_page.click_on_add_to_cart_button()
        time.sleep(1)
        driver.quit()

    def test_add_and_remove_from_cart_flow(self):
        """
        This function tests adding an item to cart and then removing it.
        and this happens in the item page.
        """
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_title()
        time.sleep(1)
        item_page = ItemPage(driver)
        item_page.click_on_add_to_cart_button()
        time.sleep(1)
        item_page.click_on_remove_button()
        time.sleep(1)
        driver.quit()

    def test_back_to_products_button(self):
        """
        This function tests back to products button in the item page
        """
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_title()
        time.sleep(1)
        item_page = ItemPage(driver)
        item_page.click_on_back_to_products_button()
        time.sleep(1)
        driver.quit()

    def test_adding_and_removing_item_flow(self):
        """
        This function tests the process of pressing on a product (item) to enter the
        item page, and then adding the item to cart, removing it, and then pressing
        on the back to products button.
        """
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_backpack_item_title()
        time.sleep(1)
        item_page = ItemPage(driver)
        item_page.click_on_add_to_cart_button()
        time.sleep(1)
        item_page.click_on_remove_button()
        time.sleep(1)
        item_page.click_on_back_to_products_button()
        time.sleep(1)
        driver.quit()
