import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest


@allure.severity(Severity.NORMAL)
@allure.epic("Searching method")
@allure.feature("Search option")
@allure.story("As a user, I want to see that I can search for specific products")
@allure.description("searching different items and see the results according to the search")
@allure.title("Search")
@pytest.mark.usefixtures("setup_page_class")
class TestSearch(BaseTest):

    @pytest.mark.parametrize(
        "search_text, expect_products",
        [
            (TestData.text_input[0], False),  # cellphone → no product
            (TestData.text_input[1], False),  # computer → no product
            (TestData.text_input[2], False),  # new → no product
            (TestData.text_input[4], True),  # touch → should return products
        ]
    )
    def test_search_items(self, search_text, expect_products):
        with allure.step(f"Searching for: {search_text}"):
            if expect_products:
                result_products = self.search_page.search_input_get_products(search_text)
                for product in result_products:
                    print(product)
                assert len(result_products) > 0
            else:
                result_products = self.search_page.search_input_no_products(search_text)
                assert "no product" in result_products

