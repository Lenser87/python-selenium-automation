from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then
from time import sleep


RESULT_TEXT = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")


@then("Verify coffee in the cart")
def verify_cart(context):
    actual_text = context.wait.until(
        EC.presence_of_element_located(RESULT_TEXT),
        message='RESULT_TEXT is not present'
    ).text
    #actual_text = context.driver.find_element(*RESULT_TEXT).text

    assert "1 item" in actual_text, f'ERROR!!! 1 item not in {actual_text}'