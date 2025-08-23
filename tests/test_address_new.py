import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestAdress(BaseTest):

    def test_user_login(self):  # This is a TEST METHOD
        # Use the credentials stored in the fixture
        email = ConfigReader.read_config("account", "email")
        password = ConfigReader.read_config("account", "password")
        self.login_page.login_right_information(email, password)
        # Your test assertions here
        assert self.login_page.get_my_account() == "My Account"

    @pytest.mark.parametrize("text_first_name, text_last_name, text_address, text_city",
                             [(TestData.review_names[1], TestData.review_names[2],
                               TestData.address_list[0] ,TestData.city_names[1])])
    def test_fill_address(self, text_first_name, text_last_name, text_address, text_city):
        country = ConfigReader.read_config("calc", "country")
        region = ConfigReader.read_config("calc", "region")
        zipcode = ConfigReader.read_config("calc", "zipcode")
        result = self.address_page.add_address(text_first_name, text_last_name,
                                               text_address, text_city, zipcode, country, region)

        text = "".join(result)  # או result[0] אם יש תמיד רק אחד
        for value in [text_first_name, text_last_name, text_address, text_city, zipcode, country, region]:
            assert value in text
