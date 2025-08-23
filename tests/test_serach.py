import pytest

from data.test_data import TestData
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")
class TestSearch(BaseTest):

    @pytest.mark.parametrize("text_cellphone", [TestData.text_input[0]])
    def test_search_cellphone(self, text_cellphone):
        result_products = self.search_page.search_input_no_products(text_cellphone)
        assert "no product" in result_products

    @pytest.mark.parametrize("text_computer", [TestData.text_input[1]])
    def test_search_computer(self, text_computer):
        result_products = self.search_page.search_input_no_products(text_computer)
        assert "no product" in result_products

    @pytest.mark.parametrize("text_new", [TestData.text_input[2]])
    def test_search_new(self, text_new):
        result_products = self.search_page.search_input_no_products(text_new)
        assert "no product" in result_products

    @pytest.mark.parametrize("text_touch", [TestData.text_input[4]])
    def test_search_touch(self, text_touch):
        result_products = self.search_page.search_input_get_products(text_touch)
        for product in result_products:
            print(product)
        assert len(result_products) > 0

