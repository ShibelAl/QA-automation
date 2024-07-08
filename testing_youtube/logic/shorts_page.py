from selenium.webdriver.common.by import By
from infra.utils import Utils
from logic.home_page import HomePage


class ShortsPage(HomePage):
    index = Utils.generate_random_string()
    MORE_OPTIONS_BUTTON = '(//div[@id = "menu-button"])[1]'
    DESCRIPTION_BUTTON = '(//yt-formatted-string[contains(@class, "item-renderer")])[1]'
    DESCRIPTION_TEXT = '(//yt-formatted-string[contains(text(), "תיאור")])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._more_options_button = self._driver.find_element(By.XPATH, self.MORE_OPTIONS_BUTTON)
        self._description_button = None
        self._description_text = None

    def click_on_more_options_button(self):
        self._more_options_button.click()

    def click_on_description_button(self):
        self._description_button = self._driver.find_element(By.XPATH, self.DESCRIPTION_BUTTON)
        self._description_button.click()

    def description_is_displayed(self):
        self._description_text = self._driver.find_element(By.XPATH, self.DESCRIPTION_TEXT)
        return self._description_text.is_displayed()



