from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Название товара
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product__name")

    # Цена
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product__price")

    # Кнопка "Add to cart"
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-button-action='add-to-cart']")

    # Изображение товара
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img.img-fluid")

    # Описание товара (обновлённый локатор)
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.product__description")

    def check_elements(self):
        """Проверяет 5 ключевых элементов на карточке товара."""
        self.is_visible(self.PRODUCT_NAME)
        self.is_visible(self.PRODUCT_PRICE)
        self.is_visible(self.ADD_TO_CART)
        self.is_visible(self.PRODUCT_IMAGE)
        self.is_visible(self.PRODUCT_DESCRIPTION)