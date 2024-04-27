from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep


SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@then("Verify search result are shown for {expected_item}")
def verify_search_result(context, expected_item):
    context.app.search_results_page.verify_search_result(expected_item)


@then("Verify that URL has {partial_url}")
def verify_search_page_url(context, partial_url):
    context.app.search_results_page.verify_partial_url(partial_url)


@when("Clicking coffee")
def clicking_coffee(context):
    context.app.search_results_page.clicking_coffee()


@when("Add product")
def add_product(context):
    context.app.search_results_page.add_product()