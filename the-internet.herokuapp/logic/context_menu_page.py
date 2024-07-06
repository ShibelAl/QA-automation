from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import BasePage


class ContextMenuPage(BasePage):
    CONTEXT_MENU = '//div[@id="hot-spot"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._context_menu = self._driver.find_element(By.XPATH, self.CONTEXT_MENU)

    def right_click_on_context_menu(self):
        action_chains = ActionChains(self._driver)
        action_chains.context_click(self._context_menu).perform()