import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest


@allure.severity(Severity.NORMAL)
@allure.epic("Searching method")
@allure.feature("Search option")
@allure.story("As a user, I want to see that I can search for specific companies names")
@allure.description("searching different items and see the results according to the search")
@allure.title("Search")
@pytest.mark.usefixtures("setup_page_class")
class TestSearchItem(BaseTest):

    @pytest.mark.parametrize("brand", [
        TestData.text_input[3],  # Apple
        TestData.text_input[5],  # Samsung
        TestData.text_input[6],  # Nikon
    ])
    def test_search_item(self, brand):
        with allure.step(f"Searching for: {brand}"):
            result_products = self.search_page.search_input_get_products(brand)
            for product in result_products:
                print(product)
            assert len(result_products) > 0
