from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from infra.base_page import BasePage


class DropdownPage(BasePage):
    SELECT_DROPDOWN = '//select[@id="dropdown"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._select_dropdown = self._driver.find_element(By.XPATH, self.SELECT_DROPDOWN)

    def select_dropdown_by_value(self):
        select = Select(self._select_dropdown)
        select.select_by_value("1")

    def select_dropdown_by_index(self, index):
        select = Select(self._select_dropdown)
        select.select_by_index(index)