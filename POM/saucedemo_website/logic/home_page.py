import time
from selenium.webdriver.common.by import By
from saucedemo_website.logic.base_page_app import BasePageApp
from saucedemo_website.logic.login_page import LoginPage
from saucedemo_website.infra.browser_wrapper import BrowserWrapper


class HomePage(BasePageApp):
    ADD_TO_CART_BUTTON_BACKPACK = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    ADD_TO_CART_BUTTON_BIKE_LIGHT = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    ADD_TO_CART_BUTTON_T_SHIRT = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

    # ITEM_NAME_BUTTON = (By.XPATH, '//div[contains(text(), "Sauce Labs Backpack"]')
    # IMAGE_CLICK = (By.XPATH, '//a[@id="item_4_img_link"]//img')

    BACKPACK_ITEM_BUTTON = (By.XPATH, '//a[@id="item_4_title_link"]')
    BIKE_LIGHT_ITEM_BUTTON = (By.XPATH, '//a[@id="item_0_title_link"]')
    T_SHIRT_ITEM_BUTTON = (By.XPATH, '//a[@id="item_1_title_link"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button_backpack = self._driver.find_element(self.ADD_TO_CART_BUTTON_BACKPACK)
        self._add_to_cart_button_bike_light = self._driver.find_element(self.ADD_TO_CART_BUTTON_BIKE_LIGHT)
        self._add_to_cart_button_t_shirt = self._driver.find_element(self.ADD_TO_CART_BUTTON_T_SHIRT)
        self._backpack_item_button = self._driver.find_element(self.BACKPACK_ITEM_BUTTON)
        self._bike_light_item_button = self._driver.find_element(self.BIKE_LIGHT_ITEM_BUTTON)
        self._t_shirt_item_button = self._driver.find_element(self.T_SHIRT_ITEM_BUTTON)

    def click_on_add_to_cart_button_backpack(self):
        self._add_to_cart_button_backpack.click()
        time.sleep(1)

    def click_on_add_to_cart_button_bike_light(self):
        self._add_to_cart_button_bike_light.click()

    def click_on_add_to_cart_button_t_shirt(self):
        self._add_to_cart_button_t_shirt.click()

    def click_on_backpack_item_button(self):
        self._backpack_item_button.click()

    def click_on_bike_light_item_button(self):
        self._bike_light_item_button.click()

    def click_on_t_shirt_item_button(self):
        self._t_shirt_item_button.click()