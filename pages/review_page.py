from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class ReviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __PRODUCT_LINK = "h4 > a"
    __REVIEW_LINK = "[href='#tab-review']"
    __NAME_FIELD = "#input-name"
    __REVIEW_FIELD = "#input-review"
    __RADIO_CHK_HIGHEST = "input[name='rating'][value='5']"
    __CONTINUE_BTN = "#button-review"
    __MESSAGE_REC = ".alert-success.alert-dismissible"

    def review_product(self, text_name, text_review):
        self.click(self.__PRODUCT_LINK)
        self.click(self.__REVIEW_LINK)
        self.add_text(self.__NAME_FIELD, text_name)
        self.add_text(self.__REVIEW_FIELD, text_review)
        self._page.locator(self.__RADIO_CHK_HIGHEST).check()
        self.click(self.__CONTINUE_BTN)
        result = self.get_text(self.__MESSAGE_REC)
        return result


