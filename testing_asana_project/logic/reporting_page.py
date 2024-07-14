import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.logging_setup import LoggingSetup


class ReportingPage(BasePage):
    CREATE_BUTTON = '//div[@class = "DomainDashboardIndexToolbar"]//div[@aria-haspopup = "menu"]'
    DASHBOARD_BUTTON_IN_CREATE = '//div[@class = "MenuItemA11y"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_create_button(self):
        """
        Clicks on "Create" button to create a new dashboard.
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON))
        ).click()

    def click_on_dashboard_button(self):
        """
        Clicks on "Dashboard" button. This button appears after pressing on "Create".
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DASHBOARD_BUTTON_IN_CREATE))
        ).click()

    def go_to_dashboard_page(self):
        """
        Goes to dashboard page, the page that contains all the charts the user have picked.
        First it clicks on "Create" and then it clicks on "Dashboard".
        """
        self.click_on_create_button()
        self.click_on_dashboard_button()
        logging.info("In dashboard page")