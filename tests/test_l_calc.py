import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.CRITICAL)
@allure.epic("Calculation")
@allure.feature("Customs and shipping  Calculation")
@allure.story("As a user, I want to know how much I will pay on shipping")
@allure.description("Add a product and give information about my address")
@allure.title("Customs and shipping  Calculation")
@pytest.mark.usefixtures("setup_page_class")
class TestCalc(BaseTest):

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
            for cart in cart_list:
                print(cart)
            assert len(cart_list) > 0

    def test_calc(self):
        country = ConfigReader.read_config("calc", "country")
        region = ConfigReader.read_config("calc", "region")
        zipcode = ConfigReader.read_config("calc", "zipcode")
        with allure.step(f"Calculate shipping with: country={country}, region={region}, zipcode={zipcode}"):
            result = self.calc_page.calc_custom(country, region, zipcode)
            assert "Success: Your shipping estimate has been applied!" in result

