from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class NewProjectPage(BasePage):
    BLANK_PROJECT_BUTTON = '//div[@class = "DashedTile DashedTile--large FlowPickerTile-dashedTile"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._blank_project = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.BLANK_PROJECT_BUTTON))
        )

    def click_on_blank_project_button(self):
        self._blank_project.click()