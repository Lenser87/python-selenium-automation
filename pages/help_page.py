from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_TOPIC = (By.XPATH, "//h1[text()=' Ulta Beauty at Target']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def _get_locator(self, text):
        #HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
        #(By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_STR}', text)]

    def open_help_page(self):
        self.open("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def select_help_topic(self, option):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value(option)

    #def verify_returns_header(self):
        #self.wait_until_visible(*self.HEADER_RETURNS)

    #def verify_topic_header(self):
        #self.wait_until_visible(*self.HEADER_TOPIC)

    def verify_header(self, header):
        locator = self._get_locator(header)
        self.wait_until_visible(*locator)
