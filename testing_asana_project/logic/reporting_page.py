from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class ReportingPage(BasePage):
    CREATE_BUTTON = '//div[@class = "DomainDashboardIndexToolbar"]//div[@aria-haspopup = "menu"]'
    DASHBOARD_BUTTON_IN_CREATE = '//div[@class = "MenuItemA11y"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._create_button = None
        self._dashboard_button = None

    def click_on_create_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON))
        ).click()
        # self._create_button.click()

    def click_on_dashboard_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.DASHBOARD_BUTTON_IN_CREATE))
        ).click()

    def go_to_dashboard_page(self):
        self.click_on_create_button()
        self.click_on_dashboard_button()