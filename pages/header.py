from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#search")
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//span[text()='Sign in']")
    SIGN_IN_BTN_POP_UP = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGN_IN_BTN)
        self.wait_until_clickable_click(*self.SIGN_IN_BTN_POP_UP)


