from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Store original window")
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when("Click on Target terms and conditions link")
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.t_and_c_link()


@when("Switch to the newly opened window")
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@when("Input incorrect email and password")
def input_incorrect(context):
    context.app.sign_in_page.incorrect_cred()


@when("Click login button")
def click_login(context):
    context.app.sign_in_page.click_login()


@then("Verify the “We can't find your account.” message is shown")
def verify_pwd_text(context):
    context.app.sign_in_page.verify_pwd_text()


@then("Verifying the sign in is opened")
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()


@then("Verify Terms and Conditions page is opened")
def verify_t_and_c_page_opened(context):
    context.app.sign_in_page.verify_t_and_c_page_opened()


@then("User can close new window")
def user_close_new_window(context):
    context.app.sign_in_page.close_window()


@then("Switch back to original page")
def return_to_original_window(context):
    context.app.sign_in_page.switch_window_by_id(context.original_window)


