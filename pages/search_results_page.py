from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, "button#addToCartButtonOrTextIdFor88040037")
    ADD_BTN = (By.XPATH, "//button[@data-test='shippingButton']")
    CARD_BTN = (By.XPATH, "//a[@href='/cart']")

    def verify_search_result(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'ERROR!!! {expected_item} not in {actual_text}'

    def clicking_coffee(self):
        self.wait_until_clickable_click(*self.ADD_PRODUCT_BTN)

    def add_product(self):
        self.wait_until_clickable_click(*self.ADD_BTN)
        self.wait_until_clickable_click(*self.CARD_BTN)