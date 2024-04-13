from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


HEADER = (By.CSS_SELECTOR, "[class*='styles__CellsComponentContainer']")
HEADER_10 = (By.CSS_SELECTOR, "[class='cell-item-content']")


@given("Open Target circle page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/l/target-circle/-/N-pzno9")


@then("Verify benefits are shown")
def verify_benefits(context):
    context.driver.find_element(*HEADER)


@then("Verify {expected_amount} benefits are shown")
def verify_10_benefits(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_10)
    print(links)
    assert len(links) == expected_amount, f"Expected {expected_amount} links, but got {len(links)}"

    #for link in links:
        #print(link.text)