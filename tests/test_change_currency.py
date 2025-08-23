import allure
import pytest

from tests.base_test import BaseTest
from utils.config_reader import ConfigReader

@allure.description("Verify that the system updates prices when changing currencies")
@allure.title("Currency change test")
@pytest.mark.run(order=4)
@pytest.mark.usefixtures("setup_page_class")
class TestChangeCurrency(BaseTest):

    def test_change_currency_gpb(self):
        result_gpb = self.change_page.change_to_gpb()
        assert result_gpb == "£"

    def test_change_currency_dollar(self):
        result_dollar = self.change_page.change_to_dollar()
        assert result_dollar == "$"

    def test_change_currency_euro(self):
        result_euro = self.change_page.change_to_euro()
        assert result_euro == "€"
