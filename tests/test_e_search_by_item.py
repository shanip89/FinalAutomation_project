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

    @pytest.mark.parametrize("text_apple", [TestData.text_input[3]])
    def test_search_apple(self, text_apple):
        with allure.step(f"Searching for: {text_apple}"):
            result_products = self.search_page.search_input_get_products(text_apple)
            for product in result_products:
                print(product)
            assert len(result_products) > 0

    @pytest.mark.parametrize("text_samsung", [TestData.text_input[5]])
    def test_search_samsung(self, text_samsung):
        with allure.step(f"Searching for: {text_samsung}"):
            result_products = self.search_page.search_input_get_products(text_samsung)
            for product in result_products:
                print(product)
            assert len(result_products) > 0

    @pytest.mark.parametrize("text_nikon", [TestData.text_input[6]])
    def test_search_nikon(self, text_nikon):
        with allure.step(f"Searching for: {text_nikon}"):
            result_products = self.search_page.search_input_get_products(text_nikon)
            for product in result_products:
                print(product)
            assert len(result_products) > 0
