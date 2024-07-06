from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import BasePage


class DragAndDrop(BasePage):

    FIRST_DRAGGABLE_ITEM = '//div[@id="column-a"]'
    SECOND_DRAGGABLE_ITEM = '//div[@id="column-b"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._first_draggable_item = self._driver.find_element(By.XPATH, self.FIRST_DRAGGABLE_ITEM)
        self._second_draggable_item = self._driver.find_element(By.XPATH, self.SECOND_DRAGGABLE_ITEM)

    def drag_first_item_to_second_item(self):
        ac = ActionChains(self._driver)
        ac.drag_and_drop(self._first_draggable_item, self._second_draggable_item).perform()

    def drag_second_item_to_first_item(self):
        ac = ActionChains(self._driver)
        ac.drag_and_drop(self._second_draggable_item, self._first_draggable_item).perform()