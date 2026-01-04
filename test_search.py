import pytest
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    driver.get("https://example-ecommerce.com")
    yield driver
    driver.quit()

def test_search_functionality(driver):
    home_page = HomePage(driver)
    home_page.enter_search_query("laptop")
    home_page.click_search()
    assert "Search Results" in driver.title
