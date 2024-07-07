from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class BasePageApp(BasePage):
    LOGO_IMAGE = '//img[@title="ParaBank"]'
    HEADER_HOME_BUTTON = '//a[text() = "home"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._logo_image = self._driver.find_element(By.XPATH, self.LOGO_IMAGE)
        self._header_home_button = self._driver.find_element(By.XPATH, self.HEADER_HOME_BUTTON)

    def logo_is_displayed(self):
        return self._logo_image.is_displayed()

    def click_on_header_home_button(self):
        self._header_home_button.click()
