from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class HomePage(BasePage):
    LOGIN_BUTTON = '(//yt-button-shape//a)[1]'
    SEARCH_INPUT = '//input[@id = "search"]'
    SHORTS_BUTTON_FULL_PAGE = '//a[@title = "Shorts" and contains(@class, "ytd-guide-entry-renderer")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._search_input = None
        self._shorts_button_full_page = self._driver.find_element(By.XPATH, self.SHORTS_BUTTON_FULL_PAGE)
        WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def click_on_login_button(self):
        self._login_button.click()

    def fill_search_input(self, search):
        self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self._search_input.send_keys(search)
        self._search_input.send_keys(Keys.RETURN)

    def click_on_shorts_button_full_page(self):
        self._shorts_button_full_page.click()