from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.ID, "cartIcon")
        self.checkout_button = (By.ID, "checkoutBtn")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
