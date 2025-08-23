from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.user_info_page import UserInfoPage


class FormPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __CONTACT_LINK = "footer > div > div > div:nth-child(2) li:nth-child(1) > a"
    __NAME_FIELD = "#input-name"
    __EMAIL_FIELD = "#input-email"
    __FORM_FIELD = "#input-enquiry"
    __SUBMIT_BTN = "[type='submit']"

    def form_fill(self, name, email, form):
        self.click(self.__CONTACT_LINK)
        self.add_text(self.__NAME_FIELD, name)
        self.add_text(self.__EMAIL_FIELD, email)
        self.add_text(self.__FORM_FIELD, form)
        self.click(self.__SUBMIT_BTN)