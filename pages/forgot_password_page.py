from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class ForgotPasswordPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    def forgot_password(self, email):
        self._user_info.get_password(email)

    def get_alert(self):
        return self._user_info.get_error()
