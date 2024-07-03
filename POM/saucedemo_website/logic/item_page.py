from selenium.webdriver.common.by import By
from base_page_app import BasePageApp


class ItemPage(BasePageApp):
    REMOVE_BUTTON = (By.XPATH, '//button[@id = "remove"]')
    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, '//button[@id = "back-to-products"]')

    def __init__(self, driver):
        super().__init__(driver)
        self._remove_button = driver.find_element(self.REMOVE_BUTTON)
        self._back_to_products_button = driver.find_element(self.BACK_TO_PRODUCTS_BUTTON)

    def click_on_remove_button(self):
        self._remove_button.click()

    def click_on_back_to_products_button(self):
        self._back_to_products_button.click()
