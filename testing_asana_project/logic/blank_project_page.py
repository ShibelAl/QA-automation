from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.utils import Utils


class BlankProjectPage(BasePage):
    PROJECT_NAME_FIELD = '//input[contains(@class, "ProjectNameInput")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._project_name_field = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.PROJECT_NAME_FIELD))
        )

    def fill_project_name_field(self):
        self._project_name_field.send_keys(Utils.generate_random_string())






