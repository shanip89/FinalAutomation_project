import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.CRITICAL)
@allure.epic("Cart")
@allure.feature("Cart")
@allure.story("As a user, I want to make sure that I can remove from the cart")
@allure.description("login in order to remove from the cart products")
@allure.title("Remove from cart")
@pytest.mark.usefixtures("setup_page_class")
class TestRemoveFromCart(BaseTest):

    def test_login(self):
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login_right_information(email, password)

    @pytest.mark.parametrize("text_nikon", [TestData.text_input[6]])
    def test_search_nikon(self, text_nikon):
        with allure.step(f"Searching for: {text_nikon}"):
            result_products = self.search_page.search_input_get_products(text_nikon)
            for product in result_products:
                print(product)
            assert len(result_products) > 0

    def test_add_cart(self):
        with allure.step("make sure the product was added to the cart"):
            cart_list = self.add_cart_page.add_cart()
            assert len(cart_list) > 0

    def test_remove_cart(self):
        with allure.step("Remove the added product"):
            self.remove_cart_page.remove_from_cart()
