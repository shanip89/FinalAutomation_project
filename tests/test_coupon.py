import pytest

from data.test_data import TestData
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")
class TestSearchItem(BaseTest):

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

    @pytest.mark.parametrize("coupon", [TestData.coupon_list[2]])
    def test_wrong_coupon(self, coupon):
        result = self.coupon_page.fake_coupon(coupon)
        assert "Warning: Coupon is either invalid, expired or reached its usage limit!" in result
