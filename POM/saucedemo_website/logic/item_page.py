from selenium.webdriver.common.by import By
from saucedemo_website.logic.base_page_app import BasePageApp


class ItemPage(BasePageApp):
    ADD_TO_CART_BUTTON = '//button[@id="add-to-cart"]'
    REMOVE_BUTTON = '//button[@id = "remove"]'
    BACK_TO_PRODUCTS_BUTTON = '//button[@id = "back-to-products"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON)
        self._remove_button = None
        self._back_to_products_button = None

    def click_on_add_to_cart_button(self):
        self._add_to_cart_button.click()

    def click_on_remove_button(self):
        self._remove_button = self._driver.find_element(By.XPATH, self.REMOVE_BUTTON)
        self._remove_button.click()

    def click_on_back_to_products_button(self):
        self._back_to_products_button = self._driver.find_element(By.XPATH, self.BACK_TO_PRODUCTS_BUTTON)
        self._back_to_products_button.click()
