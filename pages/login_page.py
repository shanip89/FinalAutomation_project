import allure
from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    @allure.step("login with email: {email} and password: {password}")
    def login_right_information(self, email, password):
        self._user_info.account_details(email, password)

    def get_my_account(self):
        return self._user_info.get_text_by()

    def get_error_msg(self):
        return self._user_info.get_error()



