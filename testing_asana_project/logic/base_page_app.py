from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class BasePageApp(BasePage):
    CREATE_BUTTON = '//div[@aria-label = "Create"]'
    PROJECT_BUTTON_IN_CREATE = '//div[@class = "MenuItemA11y Omnibutton-menuItem Omnibutton-project"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._create_button = None
        self._project_button_in_create = None

    def click_on_create_button(self):
        self._create_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CREATE_BUTTON))
        )
        self._create_button.click()

    def click_on_project_button_in_create(self):
        self._project_button_in_create = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PROJECT_BUTTON_IN_CREATE))
        )
        self._project_button_in_create.click()

    def open_new_project(self):
        self.click_on_create_button()
        self.click_on_project_button_in_create()
