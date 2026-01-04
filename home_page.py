from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchBox")
        self.search_button = (By.ID, "searchButton")

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()
