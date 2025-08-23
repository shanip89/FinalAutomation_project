from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class CouponPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __COUPON_LINK = "[href='#collapse-coupon']"
    __COUPON_FIELD = "#input-coupon"
    __APPLY_BTN = "#button-coupon"
    __ALERT_MSG = ".alert-danger"

    def fake_coupon(self, coupon):
        self.click(self.__COUPON_LINK)
        self.add_text(self.__COUPON_FIELD, coupon)
        self.click(self.__APPLY_BTN)
        result = self.get_text(self.__ALERT_MSG)
        return result

