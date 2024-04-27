from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when
from time import sleep


@given("Open Target main page")
def open_target(context):
    context.app.main_page.open_main_page()


@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)


@when("Clicking on Sign in")
def click_sign_in(context):
    context.app.header.click_sign_in()
