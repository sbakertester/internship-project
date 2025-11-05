from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.main_page import MainPage


@given('Open Reelly main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)

@when('Click on the Secondary tab on side menu')
def click_tab(context):
    context.app.main_page.click_tab()

@when('Click on Off-plan tab')  # For mobile testing only
def click_off_plan(context):
    context.app.main_page.click_off_plan()