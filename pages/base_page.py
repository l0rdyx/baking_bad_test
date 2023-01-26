import logging

import allure
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from locators.locators import MainPageLocators
from utils.decorators import wait_dec

logger = logging.getLogger('test')


class PageNotLoadedException(Exception):
    pass


D_TO = 5


class BasePage(object):
    locators = MainPageLocators()

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} page is opening...')

    @allure.step('Find element by locator - {locator}')
    def find(self, locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = D_TO
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Fill input by locator - {locator}, with value {text}')
    def fill_input(self, locator, text):
        element = self.find(locator)
        WebDriverWait(self.driver, D_TO).until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
        self.wait().until(EC.text_to_be_present_in_element_value(locator, text))

    @allure.step('Click on element by locator - {locator}')
    def click(self, locator=None, timeout=D_TO, by_locator=True, element=None):
        if by_locator:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)
                                                             and EC.presence_of_element_located(locator))
            wait_dec(element.click, ElementNotInteractableException)
        else:
            wait_dec(element.click, ElementNotInteractableException)


    @allure.step('check recipe with name {name} appears')
    def check_recipe_appears(self, name):
        while True:
            try:
                print('searching for ' + name)
                recipe = self.find((By.XPATH, f"//a[contains(text(), '{name}')]"), timeout=0)
                print('Found!')
                return True

            except TimeoutException:
                pass
            if not self.find(self.locators.yuk):
                return False
            self.click(self.locators.yeh)

    def search_basic_product(self, query):
        self.fill_input(self.locators.search_bar, query)
        self.click(self.locators.find_button)

    def add_first_dish_to_favourites(self):
        while True:
            try:
                self.click(self.locators.first_recipe)
                self.find(self.locators.success_alert)
                return self.find(self.locators.first_recipe_name).text
            except TimeoutException:
                pass

    def check_footer_link(self, button, link):
        return self.find((By.XPATH, f"//footer//a[@href = '{link}' and text() = '{button}']"))







