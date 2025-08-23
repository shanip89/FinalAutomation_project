from pages import review_page
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


class BaseTest:
    login_page: LoginPage
    forgot_page: ForgotPasswordPage
    change_page: ChangeCurrencyPage
    search_page: SearchPage
    wish_page: WishListPage
    add_cart_page: AddCartPage
    remove_cart_page: RemoveCartPage
    nav_page: NavPage
    review_page: ReviewPage
    coupon_page: CouponPage
    calc_page: CalcPage
    form_page: FormPage
    address_page: AddressPage
    logout_page: LogoutPage


