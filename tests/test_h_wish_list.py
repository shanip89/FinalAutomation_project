import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.NORMAL)
@allure.epic("Wish List")
@allure.feature("Wish List")
@allure.story("As a user, I want to make sure that I add to my wish list")
@allure.description("login in order to add to the wish list products")
@allure.title("Add to wish list")
@pytest.mark.usefixtures("setup_page_class")
class WishListTest(BaseTest):

    def test_login(self):
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login_right_information(email, password)

    @pytest.mark.parametrize("text_apple", [TestData.text_input[3]])
    def test_search_apple(self, text_apple):
        with allure.step(f"Searching for: {text_apple}"):
            result_products = self.search_page.search_input_get_products(text_apple)
            assert len(result_products) > 0

    def test_wish(self):
        with allure.step("Search for a product and add it wish list"):
            wish_list = self.wish_page.wish_add()
            for wish in wish_list:
                print(wish)
            assert len(wish_list) > 0

