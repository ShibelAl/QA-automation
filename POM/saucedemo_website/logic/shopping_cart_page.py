from selenium.webdriver.common.by import By
from base_page_app import BasePageApp


class ShoppingCart(BasePageApp):
    REMOVE_BACKPACK = (By.XPATH, '//button[@id = "remove-sauce-labs-backpack"]')
    REMOVE_BIKE_LIGHT = (By.XPATH, '//button[@id = "remove-sauce-labs-bike-light"]')
    REMOVE_T_SHIRT = (By.XPATH, '//button[@id = "remove-sauce-labs-bolt-t-shirt"]')
    ITEM_NAME = (By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]')
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//button[@id = "continue-shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@class = "btn btn_action btn_medium checkout_button "]')

    def __init__(self, driver):
        super().__init__(driver)
        self._remove_backpack = self._driver.find_element(self.REMOVE_BACKPACK)
        self._remove_bike_light = self._driver.find_element(self.REMOVE_BIKE_LIGHT)
        self._remove_t_shirt = self._driver.find_element(self.REMOVE_T_SHIRT)
        self._item_name = self._driver.find_element(self.ITEM_NAME)
        self._continue_shopping_button = self._driver.find_element(self.CONTINUE_SHOPPING_BUTTON)
        self._checkout_button = self._driver.find_element(self.CHECKOUT_BUTTON)

    def remove_backpack_from_cart(self):
        self._remove_backpack.click()

    def remove_bike_light_from_cart(self):
        self._remove_bike_light.click()

    def remove_t_shirt_from_cart(self):
        self._remove_t_shirt.click()

    def click_on_item_name_link(self):
        self._item_name.click()

    def click_on_continue_shopping(self):
        self._continue_shopping_button.click()

    def click_on_checkout_button(self):
        self._checkout_button.click()

    def remove_two_items_flow(self):
        self.remove_backpack_from_cart()
        self.remove_bike_light_from_cart()

    def remove_three_items_flow(self):
        self.remove_backpack_from_cart()
        self.remove_bike_light_from_cart()
        self.remove_t_shirt_from_cart()
