import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.NORMAL)
@allure.epic("Form Contact")
@allure.feature("Contact")
@allure.story("As a user, I want contact the seller")
@allure.description("Go to contact page and fill a form")
@allure.title("Form filling")
@pytest.mark.usefixtures("setup_page_class")
class TestForm(BaseTest):

    @pytest.mark.parametrize("text_name, text_form", [(TestData.review_names[0], TestData.review_content[1])])
    def test_fill_form(self, text_name, text_form):
        with allure.step(f"Fill a form with the following information: Name: {text_name} Form text: {text_form}"):
            email = ConfigReader.read_config("account", "email")
            self.form_page.form_fill(text_name, email, text_form)
            assert True
