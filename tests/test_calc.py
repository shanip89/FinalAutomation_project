import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestCalc(BaseTest):

    def test_login(self):
        email = ConfigReader.read_config("account", "email")
        password = ConfigReader.read_config("account", "password")
        self.login_page.login_right_information(email, password)

    @pytest.mark.parametrize("text_nikon", [TestData.text_input[6]])
    def test_search_nikon(self, text_nikon):
        result_products = self.search_page.search_input_get_products(text_nikon)
        for product in result_products:
            print(product)
        assert len(result_products) > 0

    def test_add_cart(self):
        cart_list = self.add_cart_page.add_cart()
        for cart in cart_list:
            print(cart)
        assert len(cart_list) > 0

    def test_calc(self):
        country = ConfigReader.read_config("calc", "country")
        region = ConfigReader.read_config("calc", "region")
        zipcode = ConfigReader.read_config("calc", "zipcode")
        result = self.calc_page.calc_custom(country, region, zipcode)
        assert "Success: Your shipping estimate has been applied!" in result

