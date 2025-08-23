from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class NavPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __NAV_MAIN = ".navbar-nav"

    def nav_page(self, title):
        self.nav(self.__NAV_MAIN, title)
