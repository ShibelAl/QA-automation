from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class BasePageApp(BasePage):
    MENU_BUTTON = '//yt-icon-button[@id = "guide-button"]//yt-icon[@class = "style-scope ytd-masthead"]'
    SEARCH_INPUT = '//input[@id = "search"]'
    PROFILE_BUTTON = '//button[@id = "avatar-btn"]'
    NOTIFICATION_BUTTON = '//button//div[contains(@class, "type-notification")]'
    PRODUCE_BUTTON = '//yt-icon-button[contains(@class, "menu-button-renderer")]'
    VOICE_SEARCH_BUTTON = '//button[contains(@class, "text yt-spec-button-shape-next--overlay")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
        self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self._profile_button = self._driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        self._notification_button = self._driver.find_element(By.XPATH, self.NOTIFICATION_BUTTON)
        self._produce_button = self._driver.find_element(By.XPATH, self.PRODUCE_BUTTON)
        self._voice_search_button = self._driver.find_element(By.XPATH, self.VOICE_SEARCH_BUTTON)

    def click_on_menu_button(self):
        self._menu_button.click()

    def click_on_profile_button(self):
        self._profile_button.click()

    def click_on_notification_button(self):
        self._notification_button.click()

    def click_on_produce_button(self):
        self._produce_button.click()

    def click_on_voice_search_button(self):
        self._voice_search_button.click()

    def enter_search_text(self, text):
        self._search_input.clear()  # Clear any existing text
        self._search_input.send_keys(text)