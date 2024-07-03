import unittest
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.shopping_cart_page import ShoppingCart


class TestLoginPage(unittest.TestCase):

    def test_removing_backpack_from_cart(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.remove_backpack_from_cart()

    def test_removing_bike_from_cart(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.remove_bike_light_from_cart()

    def test_removing_t_shirt_from_cart(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.remove_t_shirt_from_cart()

    def test_clicking_on_item_name_link(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_item_name_link()

    def test_clicking_on_continue_shopping(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_continue_shopping()

    def test_clicking_on_checkout_shopping(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/cart.html")
        shopping_cart = ShoppingCart(driver)
        shopping_cart.click_on_checkout_button()
