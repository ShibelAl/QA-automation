from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class BasePageApp(BasePage):
    CREATE_BUTTON = '//div[@aria-label = "Create"]'
    PROJECT_BUTTON_IN_CREATE = '//div[@class = "MenuItemA11y Omnibutton-menuItem Omnibutton-project"]'
    MESSAGE_BUTTON_IN_CREATE = '//span[text() = "Message"]'
    BLANK_PROJECT_BUTTON = '//div[@class = "DashedTile DashedTile--large FlowPickerTile-dashedTile"]'
    POP_UP_AFTER_PRESSING_CREATE = '//div[contains(@class, "LayerPositioner-layer")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._create_button = None
        self._project_button_in_create = None
        self._message_button_in_create = None
        self._blank_project_button = None
        self._pop_up_after_pressing_create = None

    def click_on_create_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CREATE_BUTTON))
        ).click()

    def click_on_project_button_in_create(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PROJECT_BUTTON_IN_CREATE))
        ).click()

    def click_on_message_button_in_create(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.MESSAGE_BUTTON_IN_CREATE))
        ).click()

    def open_new_project(self):
        self.click_on_create_button()
        self.click_on_project_button_in_create()

    def pop_up_after_pressing_create_is_displayed(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.POP_UP_AFTER_PRESSING_CREATE))
        ).is_displayed()

    def blank_project_button_is_displayed(self):
        return WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.BLANK_PROJECT_BUTTON))
        ).is_displayed()
