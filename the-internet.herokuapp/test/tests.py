import time
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.add_remove_elements import AddRemoveElementsPage
from logic.challenging_dom import ChallengingDomPage
from logic.check_boxes_page import CheckBoxesPage
from logic.context_menu_page import ContextMenuPage
from logic.drag_and_drop_page import DragAndDrop
from logic.dropdown_page import DropdownPage
from logic.dynamic_content_page import DynamicContentPage


from logic.home_page import HomePage


class Test(unittest.TestCase):

    browser = BrowserWrapper()
    config = browser.config

    def test_add_remove_element(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_add_remove_link()

        time.sleep(1)
        add_remove_elements = AddRemoveElementsPage(driver)
        add_remove_elements.click_on_add_elements_counts(5)
        time.sleep(1)

        add_remove_elements.click_on_delete(3)
        time.sleep(1)

    def test_chall_dom_press_on_edit(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_challenging_dom_link()
        time.sleep(1)
        challenging_dom_page = ChallengingDomPage(driver)
        challenging_dom_page.click_on_edit(5)  # click on edit button in the 5th row
        time.sleep(3)

    def test_chall_dom_first_button(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_challenging_dom_link()
        time.sleep(1)
        challenging_dom_page = ChallengingDomPage(driver)
        challenging_dom_page.click_on_first_button()
        time.sleep(3)

    def test_checkboxes_page(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_checkboxes_link()
        time.sleep(1)
        check_boxes = CheckBoxesPage(driver)
        check_boxes.click_on_all_checkboxes()
        time.sleep(3)

    def test_context_menu_page(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_context_menu_link()
        time.sleep(1)
        context_menu = ContextMenuPage(driver)
        context_menu.right_click_on_context_menu()
        time.sleep(3)

    def test_drag_and_drop_page(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_drag_and_drop_link()
        time.sleep(1)
        drag_and_drop = DragAndDrop(driver)
        drag_and_drop.drag_first_item_to_second_item()
        time.sleep(3)

    def test_dropdown_page(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_dropdown_link()
        time.sleep(1)
        dropdown = DropdownPage(driver)
        dropdown.select_dropdown_by_value()
        time.sleep(2)
        dropdown.select_dropdown_by_index(2)
        time.sleep(3)

    def test_dynamic_content_page(self):
        driver = BrowserWrapper().get_driver(self.config["base_url"])
        time.sleep(1)
        home_page = HomePage(driver)
        home_page.click_on_dynamic_content_link()
        time.sleep(1)
        dynamic = DynamicContentPage(driver)
        print(dynamic.get_dynamic_content_text())
        time.sleep(1)
        dynamic.click_on_here_button()
        print(dynamic.get_dynamic_content_text())
        time.sleep(2)
