import allure
import pytest

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestForgotPassword(BaseTest):

    @allure.description("Verify that the password recovery process works")
    @allure.title("Forgot password test")
    @pytest.mark.run(order=3)
    def test_forgot_password(self):
        email = ConfigReader.read_config("account", "email")
        self.forgot_page.forgot_password(email)
        assert self.forgot_page.get_alert()
