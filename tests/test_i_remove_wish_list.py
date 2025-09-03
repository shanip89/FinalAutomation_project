import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.NORMAL)
@allure.epic("Wish List")
@allure.feature("Wish List")
@allure.story("As a user, I want to make sure that I can remove from the wish list")
@allure.description("login in order to remove from the wish list products")
@allure.title("Remove from wish list")
@pytest.mark.usefixtures("setup_page_class")
class TestRemoveWishList(BaseTest):

    def test_login(self):
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login(email, password)

    def test_remove_wish(self):
        with allure.step("Search for the removed product and remove it"):
            result = self.wish_page.wish_remove()
            assert result
