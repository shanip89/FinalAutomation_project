import allure
import pytest
import test as users

from data.test_data import TestData
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@allure.epic("Web interface")
@allure.feature("Nav")
@allure.description("Verify that products can be found via the navigation menu")
@allure.title("Navigation menu search test")
@allure.story("As a user I have the ability to navigate freely in the website")
@pytest.mark.usefixtures("setup_page_class")
class TestNav(BaseTest):  # This is the TEST CLASS

    @pytest.mark.parametrize("title_right", [TestData.text_nav[0]])
    def test_desk(self, title_right):
        with allure.step(f"Navigate to: {title_right}"):
            self.nav_page.nav_page(title_right)

    @pytest.mark.parametrize("title_right", [TestData.text_nav[1]])
    def test_tablet(self, title_right):
        with allure.step(f"Navigate to: {title_right}"):
            self.nav_page.nav_page(title_right)

    @pytest.mark.parametrize("title_right", [TestData.text_nav[2]])
    def test_cam(self, title_right):
        with allure.step(f"Navigate to: {title_right}"):
            self.nav_page.nav_page(title_right)

    @pytest.mark.parametrize("title_wrong", [TestData.text_nav[3]])
    def test_wrong(self, title_wrong):
        with allure.step(f"Navigate to missing: {title_wrong}"):
            self.nav_page.nav_page(title_wrong)



