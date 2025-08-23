from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class ChangeCurrencyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    __GPB = "[name='GBP']"
    __DOLLAR = "[name='USD']"
    __EURO = "[name='EUR']"

    def change_to_gpb(self):
        self._user_info.change_currency()
        self.click(self.__GPB)
        return self.get_text('text=£')

    def change_to_dollar(self):
        self._user_info.change_currency()
        self.click(self.__DOLLAR)
        return self.get_text('text=$')

    def change_to_euro(self):
        self._user_info.change_currency()
        self.click(self.__EURO)
        return self.get_text('text=€')
