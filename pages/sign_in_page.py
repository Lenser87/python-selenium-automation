from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TITLE = (By.XPATH, "//span[text()='Sign into your Target account']")
    T_AND_C_LINK = (By.XPATH,"//a[text()='Target terms and conditions']")

    def verify_sign_in(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TITLE)

    def t_and_c_link(self):
        self.wait_until_clickable_click(*self.T_AND_C_LINK)

    def verify_t_and_c_page_opened(self):
        self.verify_partial_url('terms-conditions')


