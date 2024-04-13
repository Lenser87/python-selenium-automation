from selenium.webdriver.common.by import By
from behave import given, when
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, "input#search")
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@given("Open Target main page")
def open_target(context):
    context.driver.get("https://www.target.com/")

@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)