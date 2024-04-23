from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep


SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_BTN = (By.CSS_SELECTOR, "button#addToCartButtonOrTextIdFor13397813")
ADD_BTN_INSIDE = (By.XPATH, "//button[@data-test='orderPickupButton']")
CARD_BTN = (By.XPATH, "//a[@href='/cart']")


@then("Verify search result are shown for {expected_item}")
def verify_search_result(context, expected_item):
    #actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    #assert expected_item in actual_text, f'ERROR!!! {expected_item} not in {actual_text}'
    context.app.search_results_page.verify_search_result(expected_item)


@when("Add coffee")
def add_coffee(context):
    context.wait.until(
        EC.element_to_be_clickable(ADD_BTN),
        message='ADD_BTN is not clickable'
    ).click()
    #context.driver.find_element(*ADD_BTN).click()

    context.wait.until(
        EC.element_to_be_clickable(ADD_BTN_INSIDE),
        message='ADD_BTN_INSIDE is not clickable'
    ).click()
    #context.driver.find_element(*ADD_BTN_INSIDE).click()

    context.wait.until(
        EC.element_to_be_clickable(CARD_BTN),
        message='CARD_BTN is not clickable'
    ).click()
    #context.driver.find_element(*CARD_BTN).click()