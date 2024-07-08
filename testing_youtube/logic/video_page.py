from selenium.webdriver.common.by import By
from logic.home_page import HomePage
from selenium.common.exceptions import *


class VideoPage(HomePage):
    SEARCH_INPUT = '//input[@id = "search"]'
    VIDEO_TITLE_LINK = '(//h3[@class = "title-and-badge style-scope ytd-video-renderer"])[1]'
    LIKE_BUTTON = '(//like-button-view-model[@class = "YtLikeButtonViewModelHost"])[1]'
    LIKE_EMOJI = '(//yt-animated-icon[@animated-icon-type = "LIKE"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            self._video_title_link = self._driver.find_element(By.XPATH, self.VIDEO_TITLE_LINK)
            self._like_button = None
            self._like_emoji = None
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_on_like_button(self):
        self._like_button = self._driver.find_element(By.XPATH, self.LIKE_BUTTON)
        self._like_button.click()

    def click_on_video_link(self):
        self._video_title_link = self._driver.find_element(By.XPATH, self.VIDEO_TITLE_LINK)
        self._video_title_link.click()

    def like_emoji_is_displayed(self):
        self._like_emoji = self._driver.find_element(By.XPATH, self.LIKE_EMOJI)
        return self._like_emoji.is_displayed()

