import pytest
from selenium import webdriver
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    driver.get("https://example-ecommerce.com")
    yield driver
    driver.quit()

def test_cart_functionality(driver):
    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.click_checkout()
    assert "Checkout" in driver.title
