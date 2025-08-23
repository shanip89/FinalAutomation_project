import pytest

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestForm(BaseTest):

    @pytest.mark.parametrize("text_name, text_form", [(TestData.review_names[0], TestData.review_content[1])])
    def test_fill_form(self, text_name, text_form):
        email = ConfigReader.read_config("account", "email")
        self.form_page.form_fill(text_name, email, text_form)
        assert True
