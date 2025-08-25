import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.CRITICAL)
@allure.epic("Security")
@allure.feature("Password recovery")
@allure.description("Verify that the password recovery process works")
@allure.title("Forgot password test")
@allure.story("As a user I want to make sure that I get I can recover "
              "my password in case I forgot it and got the password to my email address")
@pytest.mark.usefixtures("setup_page_class")
class TestForgotPassword(BaseTest):

    @pytest.mark.run(order=3)
    def test_forgot_password(self):
        email = ConfigReader.read_config("account", "email")
        self.forgot_page.forgot_password(email)
        assert self.forgot_page.get_alert()
