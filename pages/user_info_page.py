from playwright.sync_api import Page

from pages.base_page import BasePage


class UserInfoPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    # place for methods
    __EMAIL_FIELD = "#input-email"
    __PASSWORD_FIELD = "#input-password"
    __LOGIN_BTN = "[value='Login']"
    __ACCOUNT_CLICK = ".caret"
    __CONTIUNE_BTN = "[value='Continue']"
    __ALERT_TXT = ".alert"
    __DROP_CURRENCY = ".fa-caret-down"
    __ADD_TO_WISH_BTN = "[data-original-title='Add to Wish List']"
    __REMOVE_WISH_BTN = ".fa-times"
    __WISH_LIST = "#wishlist-total"
    __PRODUCT_TABLE = ".table-responsive"
    __REMOVE_CART_BTN = "[data-original-title='Remove']"
    __MAIN_NAV = ".navbar-nav"
    __CONTENT = "#content"

    def account_details(self, email, password):
        self.click(self.__ACCOUNT_CLICK)
        self.click('text=Login')
        self.add_text(self.__EMAIL_FIELD, email)
        self.add_text(self.__PASSWORD_FIELD, password)
        self.click(self.__LOGIN_BTN)

    def account_out(self):
        self.click(self.__ACCOUNT_CLICK)
        self.click_first('text=Logout')
        result = self.get_text(self.__CONTENT)
        return result

    def get_password(self, email):
        self.click(self.__ACCOUNT_CLICK)
        self.click('text=Login')
        self.click_first('text=Forgotten Password')
        self.add_text(self.__EMAIL_FIELD, email)
        self.click(self.__CONTIUNE_BTN)

    def get_text_by(self):
        return self.get_text('text=My Account')

    def get_error(self):
        return self.get_text(self.__ALERT_TXT)

    def change_currency(self):
        self.click(self.__DROP_CURRENCY)

    def add_to_wish(self):
        self.click(self.__ADD_TO_WISH_BTN)
        self.click(self.__WISH_LIST)

    def clear_wish_list(self):
        self.click(self.__WISH_LIST)

        # בודק אם רשימת המשאלות ריקה
        empty_locator = self._page.locator('text=Your wish list is empty.')
        if empty_locator.count() > 0:
            return print("Wish list is already empty")
        product_count = len(self._page.locator(self.__PRODUCT_TABLE + " tr").all())
        for i in range(product_count):
            self.click(self.__REMOVE_WISH_BTN)
            # אם יש הודעה או אנימציה, אפשר להמתין כאן
        return print("Wish list cleared")

    def get_all_list(self):
        return self.get_all_text(self.__PRODUCT_TABLE)

    def remove_product(self):
        self.click(self.__REMOVE_CART_BTN)
