from selenium.webdriver.common.by import By
from saucedemo_website.infra.base_page import BasePage


class BasePageApp(BasePage):
    HEADER_TEXT = '//div[@class="app_logo"]'
    # cart button in the top right
    CART_BUTTON = '//a[@class="shopping_cart_link"]'
    # menu button in the top left, and it's inner buttons
    MENU_BUTTON = '//button[@id= "react-burger-menu-btn"]'
    ALL_ITEMS_IN_MENU = '//a[@id= "inventory_sidebar_link"]'
    ABOUT_BUTTON_IN_MENU = '//a[@id= "about_sidebar_link"]'
    LOGOUT_BUTTON_IN_MENU = '//a[@id= "logout_sidebar_link"]'
    RESET_BUTTON_IN_MENU = '//a[@id= "reset_sidebar_link"]'
    # footer social media buttons
    TWITTER_BUTTON = '//a[@data-test="social-twitter"]'
    FACEBOOK_BUTTON = '//a[@data-test="social-facebook"]'
    LINKEDIN_BUTTON = '//a[@data-test="social-linkedin"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._header_text = self._driver.find_element(By.XPATH, self.HEADER_TEXT)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
        self._all_items_in_menu = self._driver.find_element(By.XPATH, self.ALL_ITEMS_IN_MENU)
        self._about_button_in_menu = self._driver.find_element(By.XPATH, self.ABOUT_BUTTON_IN_MENU)
        self._logout_button_in_menu = self._driver.find_element(By.XPATH, self.LOGOUT_BUTTON_IN_MENU)
        self._reset_button_in_menu = self._driver.find_element(By.XPATH, self.RESET_BUTTON_IN_MENU)
        self._twitter_button = self._driver.find_element(By.XPATH, self.TWITTER_BUTTON)
        self._facebook_button = self._driver.find_element(By.XPATH, self.FACEBOOK_BUTTON)
        self._linkedin_button = self._driver.find_element(By.XPATH, self.LINKEDIN_BUTTON)

    def get_header_text(self):
        return self._header_text.text

    def click_on_cart_button(self):
        self._cart_button.click()

    def click_on_menu_button(self):
        self._menu_button.click()

    def click_on_all_items_button_in_menu(self):
        self._all_items_in_menu.click()

    def click_on_about_button_in_menu(self):
        self._about_button_in_menu.click()

    def click_on_logout_button_in_menu(self):
        self._logout_button_in_menu.click()

    def click_on_reset_button_in_menu(self):
        self._reset_button_in_menu.click()

    def click_on_twitter_button(self):
        self._twitter_button.click()

    def click_on_facebook_button(self):
        self._facebook_button.click()

    def click_on_linkedin_button(self):
        self._linkedin_button.click()
