import time
from selenium.webdriver.common.by import By
from saucedemo_website.logic.base_page_app import BasePageApp


class HomePage(BasePageApp):
    # add to cart button for three products
    ADD_TO_CART_BUTTON_BACKPACK = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BUTTON_BIKE_LIGHT = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    ADD_TO_CART_BUTTON_T_SHIRT = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    # remove button for these three products (appears only when item has been added previously)
    REMOVE_BUTTON_BACKPACK = '//button[@id="remove-sauce-labs-backpack"]'
    REMOVE_BUTTON_BIKE_LIGHT = '//button[@id="remove-sauce-labs-bike-light"]'
    REMOVE_BUTTON_T_SHIRT = '//button[@id="remove-sauce-labs-bolt-t-shirt"]'
    # title and image links of the backpack
    BACKPACK_TITLE_LINK = '//a[@id="item_4_title_link"]'
    BACKPACK_IMAGE_LINK = '//a[@id = "item_4_img_link"]'
    # title and image links of the bike light
    BIKE_LIGHT_TITLE_LINK = '//a[@id="item_0_title_link"]'
    BIKE_LIGHT_IMAGE_LINK = '//a[@id = "item_0_img_link" and @data-test = "item-0-img-link"]'
    # title and image links of the t-shirt
    T_SHIRT_TITLE_LINK = '//a[@id="item_1_title_link"]'
    T_SHIRT_IMAGE_LINK = '//a[@href="#" and @data-test="item-1-img-link"]'

    SORT_DROPDOWN = '//select[@class="product_sort_container"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._sort_dropdown = self._driver.find_element(By.XPATH, self.SORT_DROPDOWN)
        # add to cart button for three products
        self._add_to_cart_button_backpack = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_BACKPACK)
        self._add_to_cart_button_bike_light = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_BIKE_LIGHT)
        self._add_to_cart_button_t_shirt = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_T_SHIRT)
        # remove button for these three products (appears only when item has been added previously)
        self._remove_button_backpack = None
        self._remove_button_bike_light = None
        self._remove_button_t_shirt = None
        # title and image links of the backpack
        self._backpack_title_link = self._driver.find_element(By.XPATH, self.BACKPACK_TITLE_LINK)
        self._backpack_image_link = self._driver.find_element(By.XPATH, self.BACKPACK_IMAGE_LINK)
        # title and image links of the bike light
        self._bike_light_title_link = self._driver.find_element(By.XPATH, self.BIKE_LIGHT_TITLE_LINK)
        self._bike_light_image_link = self._driver.find_element(By.XPATH, self.BIKE_LIGHT_IMAGE_LINK)
        # title and image links of the t-shirt
        self._t_shirt_title_link = self._driver.find_element(By.XPATH, self.T_SHIRT_TITLE_LINK)
        self._t_shirt_image_link = self._driver.find_element(By.XPATH, self.T_SHIRT_IMAGE_LINK)

    def click_on_sort_dropdown(self):
        self._sort_dropdown.click()

    def click_on_add_to_cart_button_backpack(self):
        self._add_to_cart_button_backpack.click()

    def click_on_add_to_cart_button_bike_light(self):
        self._add_to_cart_button_bike_light.click()

    def click_on_add_to_cart_button_t_shirt(self):
        self._add_to_cart_button_t_shirt.click()

    def add_three_items_to_cart(self):
        self._add_to_cart_button_backpack.click()
        self._add_to_cart_button_bike_light.click()
        self._add_to_cart_button_t_shirt.click()

    def add_and_remove_three_items(self):
        self.add_three_items_to_cart()
        time.sleep(3)
        self.click_on_remove_button_backpack()
        self.click_on_remove_button_bike_light()
        self.click_on_remove_button_t_shirt()

    def click_on_backpack_item_title(self):
        self._backpack_title_link.click()

    def click_on_backpack_item_image(self):
        self._backpack_image_link.click()

    def click_on_bike_light_item_title(self):
        self._bike_light_title_link.click()

    def click_on_bike_light_item_image(self):
        self._bike_light_image_link.click()

    def click_on_t_shirt_item_title(self):
        self._t_shirt_title_link.click()

    def click_on_t_shirt_item_image(self):
        self._t_shirt_image_link.click()

    def click_on_remove_button_backpack(self):
        self._remove_button_backpack = self._driver.find_element(By.XPATH, self.REMOVE_BUTTON_BACKPACK)
        self._remove_button_backpack.click()

    def click_on_remove_button_bike_light(self):
        self._remove_button_bike_light = self._driver.find_element(By.XPATH, self.REMOVE_BUTTON_BIKE_LIGHT)
        self._remove_button_bike_light.click()

    def click_on_remove_button_t_shirt(self):
        self._remove_button_t_shirt = self._driver.find_element(By.XPATH, self.REMOVE_BUTTON_T_SHIRT)
        self._remove_button_t_shirt.click()
