from selenium.webdriver.common.by import By
from behave import then
from time import sleep


RESULT_TEXT = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")


@then("Verify coffee in the cart")
def verify_cart(context):
    actual_text = context.driver.find_element(*RESULT_TEXT).text
    sleep(5)
    assert "1 item" in actual_text, f'ERROR!!! 1 item not in {actual_text}'
    sleep(5)