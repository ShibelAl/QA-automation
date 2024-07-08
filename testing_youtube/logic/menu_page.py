from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium.common.exceptions import *


class MenuPage(BasePageApp):
    MENU_SECTIONS = '//ytd-guide-section-renderer[@class = "style-scope ytd-guide-renderer"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._menu_sections = self._driver.find_elements(By.XPATH, self.MENU_SECTIONS)
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def count_menu_sections(self):
        return len(self._menu_sections)
