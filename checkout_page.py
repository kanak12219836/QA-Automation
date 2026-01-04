from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.billing_details_form = (By.ID, "billingDetails")
        self.place_order_button = (By.ID, "placeOrderBtn")

    def fill_billing_details(self, details):
        # Assume `details` is a dictionary with keys like 'name', 'address', etc.
        for key, value in details.items():
            input_field = self.driver.find_element(By.NAME, key)
            input_field.send_keys(value)

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()
