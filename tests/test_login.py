import allure
import pytest
import test as users

from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("fresh_function")
class TestLogin(BaseTest):  # This is the TEST CLASS

    @allure.severity(Severity.BLOCKER)
    @allure.epic("Security")
    @allure.feature("Login")
    @allure.description("Verify that a user can log in with valid credentials")
    @allure.title("Successful login test")
    def test_user_login(self):  # This is a TEST METHOD
        # Use the credentials stored in the fixture
        with allure.step("login step with the valid credentials"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login_right_information(email, password)
            # Your test assertions here
            assert self.login_page.get_my_account() == "My Account"

    @allure.description("Verify that login fails with an incorrect password")
    @allure.title("Invalid password test")
    @pytest.mark.parametrize("password", TestData.users)
    def test_user_wrong_info(self, password):
        with allure.step("login with incorrect password"):
            email = ConfigReader.read_config("account", "email")
            self.login_page.login_right_information(email, password)
            assert self.login_page.get_error_msg()

