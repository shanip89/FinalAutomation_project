import allure
import pytest
from allure_commons.types import Severity

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.severity(Severity.CRITICAL)
@allure.epic("Address information")
@allure.feature("Address")
@allure.story("As a user, I want to have the option to change my address")
@allure.description("Go to my account and add a new address")
@allure.title("Add a new address")
@pytest.mark.usefixtures("setup_page_class")
class TestAdress(BaseTest):

    def test_user_login(self):  # This is a TEST METHOD
        # Use the credentials stored in the fixture
        with allure.step("login page steps"):
            email = ConfigReader.read_config("account", "email")
            password = ConfigReader.read_config("account", "password")
            self.login_page.login_right_information(email, password)
            # Your test assertions here
            assert self.login_page.get_my_account() == "My Account"

    @pytest.mark.parametrize("text_first_name, text_last_name, text_address, text_city",
                             [(TestData.review_names[1], TestData.review_names[2],
                               TestData.address_list[0] ,TestData.city_names[1])])
    def test_fill_address(self, text_first_name, text_last_name, text_address, text_city):
        with allure.step(f"New address info: \n "
                         f"Name: {text_first_name} \n "
                         f"Last name: {text_last_name} \n "
                         f"Address: {text_address} \n "
                         f"City: {text_city}"):
            country = ConfigReader.read_config("calc", "country")
            region = ConfigReader.read_config("calc", "region")
            zipcode = ConfigReader.read_config("calc", "zipcode")
            result = self.address_page.add_address(text_first_name, text_last_name,
                                                   text_address, text_city, zipcode, country, region)

            text = "".join(result)  # או result[0] אם יש תמיד רק אחד
            for value in [text_first_name, text_last_name, text_address, text_city, zipcode, country, region]:
                assert value in text
