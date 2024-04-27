from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TITLE = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TITLE)

