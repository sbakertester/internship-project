from selenium.webdriver.common.by import By

from pages.base_page import Page

class MainPage(Page):

    SECONDARY_TAB = (By.CSS_SELECTOR, 'a.menu-button-block[href="/secondary-listings"]')

    def open_main(self):
        self.open_url('https://soft.reelly.io')

    def click_tab(self):
        self.click(*self.SECONDARY_TAB)

