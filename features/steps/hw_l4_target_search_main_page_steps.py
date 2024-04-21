from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, "input#search")
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@given("Open Target main page")
def open_target(context):
    context.driver.get("https://www.target.com/")

@when("Search for {item}")
def search_product(context, item):
    context.wait.until(
        EC.element_to_be_clickable(SEARCH_INPUT),
        message="SEARCH_INPUT is not clickable"
    ).send_keys(item)
    #context.driver.find_element(*SEARCH_INPUT).send_keys(item)

    context.wait.until(
        EC.element_to_be_clickable(SEARCH_BTN),
        message='SEARCH_BTN is not clickable'
    ).click()
    #context.driver.find_element(*SEARCH_BTN).click()

    sleep(6)