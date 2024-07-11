from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.utils import Utils


class BlankProjectPage(BasePage):
    PROJECT_NAME_FIELD = '//input[contains(@class, "ProjectNameInput")]'
    CREATE_PROJECT_BUTTON = '//div[text() = "Create project"]'
    # DETERMINE_PROJECT_GOAL_INPUT = '//div[text() = "e.g. Determine project goal"]'
    PROJECT_NAME_HEADER = '//h5[contains(@class, "projectNameHeader")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._project_name_field = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PROJECT_NAME_FIELD))
        )
        self._create_project_button = None
        self._project_name_header = None

    def fill_project_name_field(self):
        self._project_name_field.send_keys(Utils.generate_random_string())

    def project_name_is_displayed(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROJECT_NAME_HEADER))
        ).is_displayed()


    def get_header_project_name_text(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PROJECT_NAME_HEADER))
        ).text

    def click_on_create_project(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_PROJECT_BUTTON))
        ).click()

    def create_project_flow(self):
        self.fill_project_name_field()
        self.click_on_create_project()