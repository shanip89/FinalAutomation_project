import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestReview(BaseTest):

    @pytest.mark.parametrize("text_nikon", [TestData.text_input[6]])
    def test_search_nikon(self, text_nikon):
        result_products = self.search_page.search_input_get_products(text_nikon)
        for product in result_products:
            print(product)
        assert len(result_products) > 0

    @pytest.mark.parametrize("text_name, text_review", [(TestData.review_names[0], TestData.review_content[2])])
    def test_review(self, text_name, text_review):
        result = self.review_page.review_product(text_name, text_review)
        assert "Thank you for your review." in result

