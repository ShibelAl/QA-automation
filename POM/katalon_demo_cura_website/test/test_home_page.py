import unittest
from katalon_demo_cura_website.infra.browserwrapper import BrowserWrapper
from katalon_demo_cura_website.logic.home_page import HomePage


class TestHomePage(unittest.TestCase):

    def test_make_appointment_button(self):
        driver = BrowserWrapper().getDriver("https://katalon-demo-cura.herokuapp.com/#")
        home_page = HomePage(driver)
        home_page.click_on_make_appointment()

    # def test_mail_button(self):
    #     home_page = HomePage()
    #     home_page.return_to_home_page()
    #     home_page.click_on_mail_button()
