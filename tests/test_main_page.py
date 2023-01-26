from time import sleep

import pytest

from tests.base_steps import Base
import allure

from selenium.webdriver.support import expected_conditions as EC

from utils.db_connector import DBAccess

DB = DBAccess()


# , "Beans", "Potato"

class TestBase(Base):

    @allure.feature('UI tests')
    @allure.story('Test adding product to favourites')
    @pytest.mark.UI
    @allure.description("""
                    Search, Add to Favourites, check DB 
                    """)
    @pytest.mark.parametrize("query", ["Cheese"])
    def test_search(self, query):
        self.base_page.search_basic_product(query)
        name = self.base_page.add_first_dish_to_favourites()
        assert name in DB.select_all()

    @allure.feature('UI tests')
    @allure.story('Test footer')
    @pytest.mark.UI
    @allure.description("""
                       Test links leading to right places
                       """)
    @pytest.mark.parametrize("button, link",
                             [("Email Us", "mailto:hi@bakingbad.com"), ("Umain", "https://www.umain.com/")])
    def test_footer(self, button, link):
        assert self.base_page.check_footer_link(button, link,)