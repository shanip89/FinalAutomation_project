from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class WishListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    def wish_add(self):
        self._user_info.add_to_wish()
        return self._user_info.get_all_list()

    def wish_remove(self):
        result = self._user_info.clear_wish_list
        return result
