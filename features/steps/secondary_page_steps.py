
from selenium.webdriver.common.by import By
from behave import given, when, then

from pages.main_page import MainPage


@when('Clicks on Filters')
def click_filters(context):
    context.app.secondary_page.click_filters()

@when('Selects the Want to buy option')
def select_want_to_buy(context):
    context.app.secondary_page.select_want_to_buy()

@when('Clicks on Apply Filter button')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()

@then('Verify all cards have the Want to buy tag')
def verify_want_to_buy_tags(context):
    context.app.secondary_page.verify_want_to_buy_tags()

@then('Verify the right page opens')
def verify_secondary_page(context):
    context.app.secondary_page.verify_secondary_page_opened()