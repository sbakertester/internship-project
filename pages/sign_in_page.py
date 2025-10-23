from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):

    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a[wized="loginButton"]')


    def enter_email(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_continue_btn(self):
        self.click(*self.CONTINUE_BTN)

    def sign_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_continue_btn()
