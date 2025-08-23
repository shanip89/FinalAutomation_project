import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class LogoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    def logout(self):
        result = self._user_info.account_out()
        return result