import time

import selenium.common.exceptions
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_page_app import BasePageApp


class NewMessagePopUp(BasePageApp):
    ADD_SUBJECT = '//input[@placeholder = "Add subject"]'
    TO_INPUT_FIELD = '(//input[@placeholder = "Type the name of a team, a project, or people"])[1]'
    MESSAGE_BODY = '//p[@class = "ProsemirrorEditor-paragraph"]'
    SEND_BUTTON = '//div[text() = "Send"]'
    VIEW_MESSAGE_LINK = '//a[@class = "PrimaryNavigationLink"]'
    TITLE_FIELD_IN_VIEW_MESSAGE_MODE = '//textarea[@placeholder = "Write a message title"]'
    CLOSE_NEW_MESSAGE_POPUP_BUTTON = '//div[@class = "FocusTrap"]//div[@aria-label = "Close"]'
    CLOSE_DRAFT_MESSAGE_BUTTON = '//div[contains(@class, "collapsed")]//div[@aria-label = "Close"]'
    DELETE_BUTTON_CLOSING_DRAFT = '//div[text() = "Delete message"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._message_receiver = None
        # self._close_draft_message = None

    def fill_add_subject_field(self, subject):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_SUBJECT))
        ).send_keys(subject)

    def add_message_receiver_email(self, email):
        self._message_receiver = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.TO_INPUT_FIELD))
        )
        self._message_receiver.send_keys(email)
        self._message_receiver.send_keys(Keys.RETURN)

    def fill_message_content(self, message):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.MESSAGE_BODY))
        ).send_keys(message)

    def click_on_send_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEND_BUTTON))
        ).click()

    def click_on_view_message_link(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.VIEW_MESSAGE_LINK))
        ).click()

    def view_message_title_is_visible(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.TITLE_FIELD_IN_VIEW_MESSAGE_MODE))
        ).is_displayed()

    def view_message_title_text(self):
        return WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.TITLE_FIELD_IN_VIEW_MESSAGE_MODE))
        ).text

    def close_new_message_popup(self):
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CLOSE_NEW_MESSAGE_POPUP_BUTTON))
        ).click()

    def click_on_to_field_in_message_popup(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.TO_INPUT_FIELD))
        ).click()

    def close_draft_message(self):
        try:
            WebDriverWait(self._driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.CLOSE_DRAFT_MESSAGE_BUTTON))
            ).click()
            time.sleep(1)
            WebDriverWait(self._driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, self.DELETE_BUTTON_CLOSING_DRAFT))
            ).click()
            self.click_on_to_field_in_message_popup()
        except selenium.common.exceptions.TimeoutException:
            pass
