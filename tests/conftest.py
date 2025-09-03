from idlelib import browser

import pytest
from playwright.sync_api import Page, sync_playwright

from pages.add_cart_page import AddCartPage
from pages.calculate_page import CalcPage
from pages.change_currency_page import ChangeCurrencyPage
from pages.copun_page import CouponPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.form_page import FormPage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.nav_page import NavPage
from pages.new_address_page import AddressPage
from pages.remove_cart_page import RemoveCartPage
from pages.review_page import ReviewPage
from pages.search_page import SearchPage
from pages.wish_list_page import WishListPage
from utils.config_reader import ConfigReader

# conftest.py
import pytest
import allure
import logging
from pathlib import Path
from playwright.sync_api import Page


@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    page = browser.new_page()
    url1 = ConfigReader.read_config("general", "url")
    page.goto(url1)
    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.forgot_page = ForgotPasswordPage(page)
    request.cls.change_page = ChangeCurrencyPage(page)
    request.cls.search_page = SearchPage(page)
    request.cls.wish_page = WishListPage(page)
    request.cls.add_cart_page = AddCartPage(page)
    request.cls.remove_cart_page = RemoveCartPage(page)
    request.cls.nav_page = NavPage(page)
    request.cls.review_page = ReviewPage(page)
    request.cls.coupon_page = CouponPage(page)
    request.cls.calc_page = CalcPage(page)
    request.cls.form_page = FormPage(page)
    request.cls.address_page = AddressPage(page)
    request.cls.logout_page = LogoutPage(page)
    yield
    page.close()


@pytest.fixture(scope="function")
def fresh_function(request, page: Page):
    url1 = ConfigReader.read_config("general", "url")
    page.goto(url1)
    request.cls.page = page
    request.cls.login_page = LoginPage(page)
    request.cls.forgot_page = ForgotPasswordPage(page)
    request.cls.change_page = ChangeCurrencyPage(page)
    request.cls.search_page = SearchPage(page)
    request.cls.wish_page = WishListPage(page)
    request.cls.add_cart_page = AddCartPage(page)
    request.cls.remove_cart_page = RemoveCartPage(page)
    request.cls.nav_page = NavPage(page)
    request.cls.review_page = ReviewPage(page)
    request.cls.coupon_page = CouponPage(page)
    request.cls.calc_page = CalcPage(page)
    request.cls.form_page = FormPage(page)
    request.cls.address_page = AddressPage(page)
    request.cls.logout_page = LogoutPage(page)
    yield
    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = None

        # אם יש fixture page
        if "page" in item.funcargs:
            page = item.funcargs["page"]
        # אם יש page ששמרנו ב-request.cls
        elif hasattr(item.instance, "page"):
            page = item.instance.page

        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot - {item.name}",
                attachment_type=allure.attachment_type.PNG
            )
