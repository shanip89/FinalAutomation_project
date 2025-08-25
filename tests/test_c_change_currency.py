import allure
import pytest
from allure_commons.types import Severity

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.NORMAL)
@allure.epic("Currency")
@allure.feature("Currency validation")
@allure.description("Verify that the system updates prices when changing currencies")
@allure.title("Currency change test")
@allure.story("As a user, I want to make sure that I can pay in different currencies")
@pytest.mark.usefixtures("setup_page_class")
class TestChangeCurrency(BaseTest):

    def test_change_currency_gpb(self):
        with allure.step("change the currency to GPB"):
            result_gpb = self.change_page.change_to_gpb()
            assert result_gpb == "£"

    def test_change_currency_dollar(self):
        with allure.step("change the currency to DOLLAR"):
            result_dollar = self.change_page.change_to_dollar()
            assert result_dollar == "$"

    def test_change_currency_euro(self):
        with allure.step("change the currency to EURO"):
            result_euro = self.change_page.change_to_euro()
            assert result_euro == "€"
