from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_result(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'ERROR!!! {expected_item} not in {actual_text}'