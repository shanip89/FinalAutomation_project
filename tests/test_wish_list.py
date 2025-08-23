import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class WishListTest(BaseTest):

    def test_login(self):
        email = ConfigReader.read_config("account", "email")
        password = ConfigReader.read_config("account", "password")
        self.login_page.login_right_information(email, password)

    @pytest.mark.parametrize("text_apple", [TestData.text_input[3]])
    def test_search_apple(self, text_apple):
        result_products = self.search_page.search_input_get_products(text_apple)
        assert len(result_products) > 0

    def test_wish(self):
        wish_list = self.wish_page.wish_add()
        for wish in wish_list:
            print(wish)
        assert len(wish_list) > 0

