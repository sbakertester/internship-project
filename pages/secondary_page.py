from selenium.webdriver.common.by import By
from pages.base_page import Page

class SecondaryPage(Page):

    FILTER_BTN = (By.CSS_SELECTOR, 'div.filter-button')
    WANT_TO_BUY = (By.CSS_SELECTOR, 'div[wized="ListingTypeBuy"]')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')
    WANT_TO_BUY_TAGS = (By.CSS_SELECTOR, 'div[wized="saleTagBoxMLS"]')
    CARDS = (By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')

    def verify_secondary_page_opened(self):
        self.verify_partial_url('secondary-listings')

    def click_filters(self):
        self.wait_until_clickable_click(*self.FILTER_BTN)

    def select_want_to_buy(self):
        self.wait_until_clickable_click(*self.WANT_TO_BUY)


    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER_BTN)

    def verify_want_to_buy_tags(self):
        self.wait_until_element_appear(*self.CARDS)
        cards = self.driver.find_elements(*self.CARDS)
        assert cards, 'No cards found on this page'

        for card in cards:
            tag = card.find_elements(*self.WANT_TO_BUY_TAGS)
            assert tag, 'A card is missing the "Want to buy" tag'



