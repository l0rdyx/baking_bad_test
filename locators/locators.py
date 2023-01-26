from selenium.webdriver.common.by import By


class MainPageLocators:

    find_button = (By.XPATH, "//a[contains(@href, 'find')]")
    search_bar = (By.XPATH, "//input")
    first_recipe = (By.XPATH, "//section/div[1]//button")
    success_alert = (By.XPATH, "//div[contains(@class, 'success')]")
    first_recipe_name = (By.XPATH, "//section/div[1]//div[@class = 'text-3xl']")
