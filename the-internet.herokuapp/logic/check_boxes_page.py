from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class CheckBoxesPage(BasePage):
    FIRST_CHECKBOX = '//input[@type="checkbox"][1]'
    SECOND_CHECKBOX = '//input[@type="checkbox"][2]'

    def __init__(self, driver):
        super().__init__(driver)
        self._first_checkbox = self._driver.find_element(By.XPATH, self.FIRST_CHECKBOX)
        self._second_checkbox = self._driver.find_element(By.XPATH, self.SECOND_CHECKBOX)

    def click_on_first_checkbox(self):
        if self._first_checkbox.is_selected():
            self._first_checkbox.click()
            return
        self._first_checkbox.click()

    def click_on_second_checkbox(self):
        if self._second_checkbox.is_selected():
            self._second_checkbox.click()
            return
        self._second_checkbox.click()

    def click_on_all_checkboxes(self):
        self._first_checkbox.click()
        self._second_checkbox.click()