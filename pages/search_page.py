from playwright.sync_api import Page

from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __SEARCH_FIELD_INPUT = ".form-control.input-lg"
    __SEARCH_BTN = ".fa-search"
    __NO_RESULTS = "p:has-text('no product')"
    __PRODUCT_LIST = ".product-thumb"

    def search_input_no_products(self, input_text):
        self.add_text(self.__SEARCH_FIELD_INPUT, input_text)
        self.click(self.__SEARCH_BTN)
        return self.get_text(self.__NO_RESULTS)

    def search_input_get_products(self, input_text):
        self.add_text(self.__SEARCH_FIELD_INPUT, input_text)
        self.click(self.__SEARCH_BTN)
        return self.get_all_text(self.__PRODUCT_LIST)

