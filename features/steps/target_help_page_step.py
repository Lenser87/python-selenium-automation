from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given("Open Help page for Returns")
def open_help_page(context):
    context.app.help_page.open_help_page()


@when("Select Help topic {option}")
def select_help_topic(context, option):
    context.app.help_page.select_help_topic(option)


#@then("Verify Returns page has opened")
#def verify_returns_header(context):
    #context.app.help_page.verify_returns_header()


#@then("Verify current topic page has opened")
#def verify_topic_header(context):
    #context.app.help_page.verify_topic_header()


@then("Verify {header} page has opened")
def verify_help_page_header(context, header):
    context.app.help_page.verify_header(header)