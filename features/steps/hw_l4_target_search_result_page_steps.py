from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_BTN = (By.CSS_SELECTOR, "button#addToCartButtonOrTextIdFor12954148")
ADD_BTN_INSIDE = (By.XPATH, "//button[@data-test='orderPickupButton']")
CARD_BTN = (By.XPATH, "//a[@href='/cart']")


@then("Verify search result are shown for {expected_item}")
def verify_search_result(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    sleep(6)
    assert expected_item in actual_text, f'ERROR!!! {expected_item} not in {actual_text}'


@when("Add coffee")
def add_coffee(context):
    context.driver.find_element(*ADD_BTN).click()
    sleep(5)
    context.driver.find_element(*ADD_BTN_INSIDE).click()
    sleep(5)
    context.driver.find_element(*CARD_BTN).click()
    sleep(5)