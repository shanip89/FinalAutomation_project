import allure
import pytest
import test as users

from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.NORMAL)
@allure.epic("Logout validation")
@allure.feature("Logout")
@allure.story("As a user, I want to have ability to logout from my account")
@allure.description("Go to my account and logout")
@allure.title("Logout")
@pytest.mark.usefixtures("setup_page_class")
class TestLogout(BaseTest):  # This is the TEST CLASS

    def test_user_login(self):  # This is a TEST METHOD
        # Use the credentials stored in the fixture
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login_right_information(email, password)
            # Your test assertions here
            assert self.login_page.get_my_account() == "My Account"

    def test_user_logout(self):
        with allure.step("Logout successfully from the account"):
            result = self.logout_page.logout()
            assert "You have been logged off your account." in result
