from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):

    SECONDARY_TAB = (By.CSS_SELECTOR, 'button.pb-5.text-muted-foreground') # mobile only
    # SECONDARY_TAB = (By.CSS_SELECTOR, 'a.menu-button-block[href="/secondary-listings"]') # web browser
    OFF_PLAN_TAB = (By.CSS_SELECTOR, 'a.menu-link[wized="newOffPlanLink"]')


    def open_main(self):
        self.open_url('https://soft.reelly.io')

    def click_tab(self):
        self.click(*self.SECONDARY_TAB)

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_TAB)