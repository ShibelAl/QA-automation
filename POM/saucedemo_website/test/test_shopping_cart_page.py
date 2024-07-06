import time
import unittest
from saucedemo_website.infra.config_provider import ConfigProvider
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.login_page import LoginPage
from saucedemo_website.logic.base_page_app import BasePageApp
from saucedemo_website.logic.home_page import HomePage
from saucedemo_website.logic.shopping_cart_page import ShoppingCart


class TestLoginPage(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def test_continue_shopping_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(1)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_continue_shopping()
        time.sleep(1)
        driver.quit()

    def test_continue_shopping_with_multiple_items_in_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.add_three_items_to_cart()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(2)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_continue_shopping()
        time.sleep(3)
        driver.quit()

    def test_checkout_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(1)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_checkout_button()
        time.sleep(1)
        driver.quit()

    # test adding the backpack item to cart and see if it appears in cart
    def test_add_item_and_show_in_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_backpack()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(3)
        driver.quit()

    def test_cart_after_adding_three_items(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.add_three_items_to_cart()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(3)
        driver.quit()

    def test_checkout_with_items_in_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.add_three_items_to_cart()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(2)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_checkout_button()
        time.sleep(3)
        driver.quit()

    def test_removing_item_from_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_backpack()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(2)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.remove_backpack_from_cart()
        time.sleep(2)
        driver.quit()

    def test_removing_multiple_items_from_cart(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.add_three_items_to_cart()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(2)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.remove_three_items()
        time.sleep(2)
        driver.quit()

    def test_clicking_on_item_name_link(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        home_page = HomePage(driver)
        home_page.click_on_add_to_cart_button_backpack()
        time.sleep(1)
        base_page_app = BasePageApp(driver)
        base_page_app.click_on_cart_button()
        time.sleep(1)
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_item_name_link()
        time.sleep(2)
        driver.quit()
