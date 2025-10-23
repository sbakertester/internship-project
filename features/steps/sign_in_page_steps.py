from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User is signed into page with email "{email}" and password "{password}"')
def sign_into_page(context, email, password):
    context.app.sign_in_page.sign_in(email, password)

