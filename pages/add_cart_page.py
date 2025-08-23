from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class AddCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._user_info = UserInfoPage(page)

    __ADD_TO_CART = "[onclick^='cart.add']"
    __CART_LINK = "[href$='index.php?route=checkout/cart']"

    def add_cart(self):
        self.click(self.__ADD_TO_CART)
        self.click_first(self.__CART_LINK)
        return self._user_info.get_all_list()