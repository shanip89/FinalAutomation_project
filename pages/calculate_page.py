from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class CalcPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __CUSTOM_LINK = "[href='#collapse-shipping']"
    __COUNTRY_FIELD = "#input-country"
    __REGION_FIELD = "#input-zone"
    __ZIPCODE_FIELD = "#input-postcode"
    __BTN_CLICK = "#button-quote"
    __RADIO_TYPE = "[type='radio']"
    __SHIPPING_BTN = "#button-shipping"
    __ALERT_SUC_MSG = ".alert-success"

    def calc_custom(self, country, region, zipcode):
        self.click(self.__CUSTOM_LINK)
        self._page.locator(self.__COUNTRY_FIELD).select_option(label=country)
        self._page.locator(self.__REGION_FIELD).select_option(label=region)
        self.add_text(self.__ZIPCODE_FIELD, zipcode)
        self.click(self.__BTN_CLICK)
        self._page.locator(self.__RADIO_TYPE).check()
        self.click(self.__SHIPPING_BTN)
        result = self.get_text(self.__ALERT_SUC_MSG)
        return result
