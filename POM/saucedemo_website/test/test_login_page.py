import unittest
from saucedemo_website.infra.browser_wrapper import BrowserWrapper
from saucedemo_website.logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    def test_username_input(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.fill_user_name_input("standard_user")

    def test_password_input(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.fill_password_input("secret_sauce")

    def test_correct_login_flow(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")

    def test_wrong_login_flow(self):
        driver = BrowserWrapper().getDriver("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login_flow("shibel", "wrong_password")


    # def test_add_to_cart_button(self):
    #     driver = BrowserWrapper().get_driver("https://www.saucedemo.com/inventory.html")
    #     home_page = HomePage(driver)
    #     home_page.click_on_add_to_cart_button_backpack()
