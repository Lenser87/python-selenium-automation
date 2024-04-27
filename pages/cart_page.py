from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    RESULT_TEXT = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")

    def verify_cart_title(self):
        self.verify_partial_text('1 item', *self.RESULT_TEXT)
