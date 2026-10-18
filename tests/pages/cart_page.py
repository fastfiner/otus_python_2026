from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-name")

    def open_cart(self):
        self.open("/cart?action=show")

    def get_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAME)]