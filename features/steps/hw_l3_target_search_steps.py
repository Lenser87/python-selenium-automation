from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get("https://www.target.com/")

@when('Clicking on Cart icon')
def clicking_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(6)

@then('Verifying actual text is shown')
def verify_text(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    sleep(6)
    assert 'Your cart is empty' in actual_text, f'ERROR!!! Text Your cart is empty not in {actual_text}'

