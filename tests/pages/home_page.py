from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand img.logo")
    MENU = (By.CSS_SELECTOR, "ul#top-menu")
    ART_LINK = (By.CSS_SELECTOR, "a[href*='/9-art']")
    SEARCH = (By.CSS_SELECTOR, "input#ps_searchbar_input")
    CART = (By.CSS_SELECTOR, ".header-block__badge")
    SIGN_IN = (By.CSS_SELECTOR, "a[href*='/login']")
    HEADER = (By.CSS_SELECTOR, "header")

    # Для корзины (3.2)
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, "button[data-button-action='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, ".header-block__badge")

    def open_home(self):
        self.open("/")

    def check_elements(self):
        self.is_visible(self.LOGO)
        self.is_visible(self.MENU)
        self.is_visible(self.ART_LINK)
        self.is_visible(self.SEARCH)
        self.is_visible(self.CART)
        self.is_visible(self.SIGN_IN)

    # === 3.2: корзина ===
    def get_cart_count(self):
        """Возвращает число товаров в корзине (из бейджа)"""
        return int(self.is_visible(self.CART_BADGE).text)

    def add_first_product_to_cart(self):
        """Добавляет первый товар с главной в корзину (JS-клик)"""
        button = self.is_clickable(self.FIRST_ADD_TO_CART)
        self.driver.execute_script("arguments[0].click();", button)