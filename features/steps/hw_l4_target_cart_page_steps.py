from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then


RESULT_TEXT = (By.CSS_SELECTOR, "[class*='styles__CartSummarySpan']")


@then("Verify coffee in the cart")
def verify_cart_title(context):
    context.app.cart_page.verify_cart_title()