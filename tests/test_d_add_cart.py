import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.CRITICAL)
@allure.epic("Cart Payment")
@allure.feature("Cart")
@allure.story("As a user, I want to make sure that I add to the cart products")
@allure.description("login in order to add to the cart products")
@allure.title("Add to the cart")
@pytest.mark.usefixtures("setup_page_class")
class AddCartTest(BaseTest):

    def test_login(self):
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login(email, password)

    @pytest.mark.parametrize("text_nikon", [TestData.text_input[6]])
    def test_search_nikon(self, text_nikon):
        with allure.step("Search for a product and add it to the cart"):
            result_products = self.search_page.search_input_get_products(text_nikon)
            for product in result_products:
                print(product)
            assert len(result_products) > 0

    def test_add_cart(self):
        cart_list = self.add_cart_page.add_cart()
        for cart in cart_list:
            print(cart)
        assert len(cart_list) > 0
