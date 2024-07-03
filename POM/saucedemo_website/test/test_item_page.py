import unittest
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.item_page import ItemPage


class TestLoginPage(unittest.TestCase):

    def test_remove_item_button(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/inventory-item.html?id=4")
        item_page = ItemPage(driver)
        item_page.click_on_remove_button()

    def test_back_to_products_button(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/inventory-item.html?id=4")
        item_page = ItemPage(driver)
        item_page.click_on_back_to_products_button()
