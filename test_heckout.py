import pytest
from selenium import webdriver
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    driver.get("https://example-ecommerce.com/cart")
    yield driver
    driver.quit()

def test_checkout_process(driver):
    checkout_page = CheckoutPage(driver)
    billing_details = {
        'name': 'John Doe',
        'address': '123 Main St',
        'city': 'Metropolis',
        'postalCode': '12345',
        'country': 'USA'
    }
    checkout_page.fill_billing_details(billing_details)
    checkout_page.place_order()
    assert "Order Confirmation" in driver.title
