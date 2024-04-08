from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page 1")
def open_target(context):
    context.driver.get("https://www.target.com/")

@when("Clicking on Sign in")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(6)
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(6)

@then("Verifying the sign in is opened")
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    sleep(6)
    assert 'Sign into your Target account' in actual_text, f'ERROR!!! Text Sign into your Target account not in {actual_text}'