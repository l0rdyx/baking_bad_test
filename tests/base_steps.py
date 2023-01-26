import pytest
from _pytest.fixtures import FixtureRequest

from pages.base_page import BasePage


class Base:
    auth = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.base_page: BasePage = request.getfixturevalue('base_page')