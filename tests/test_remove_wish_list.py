import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestRemoveWishList(BaseTest):

    def test_login(self):
        email = ConfigReader.read_config("account", "email")
        password = ConfigReader.read_config("account", "password")
        self.login_page.login_right_information(email, password)

    def test_remove_wish(self):
        result = self.wish_page.wish_remove()
        assert result
