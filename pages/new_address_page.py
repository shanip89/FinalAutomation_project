from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class AddressPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __ADDRESSES_LNK = "[href='https://tutorialsninja.com/demo/index.php?route=account/address']"
    __NEW_ADDRESS_BTN = "[href='https://tutorialsninja.com/demo/index.php?route=account/address/add']"
    __FIRST_NAME_FIELD = "#input-firstname"
    __LAST_NAME_FIELD = "#input-lastname"
    __ADDRESS_FIELD = "#input-address-1"
    __CITY_FIELD = "#input-city"
    __ZIPCODE_FIELD = "#input-postcode"
    __COUNTRY_FIELD = "#input-country"
    __REGION_FIELD = "#input-zone"
    __CONTINUE_BTN = "[value='Continue']"
    __ALERT_MSG = ".alert-success"
    __ADDRESS_LIST = ".table-responsive"

    def add_address(self, first_name, last_name, address, city, zipcode, country, zone):
        self.click_first(self.__ADDRESSES_LNK)
        self.click(self.__NEW_ADDRESS_BTN)
        self.add_text(self.__FIRST_NAME_FIELD, first_name)
        self.add_text(self.__LAST_NAME_FIELD, last_name)
        self.add_text(self.__ADDRESS_FIELD, address)
        self.add_text(self.__CITY_FIELD, city)
        self._page.locator(self.__COUNTRY_FIELD).select_option(country)
        self._page.locator(self.__REGION_FIELD).select_option(zone)
        self.add_text(self.__ZIPCODE_FIELD, zipcode)
        self.click(self.__CONTINUE_BTN)
        self.get_text(self.__ALERT_MSG)
        result = self.get_all_text(self.__ADDRESS_LIST)
        return result

