from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):
    # Заголовок страницы "Art"
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title-section")

    # Контейнер со всеми товарами
    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, "div.products")

    # Карточка товара
    PRODUCT_CARD = (By.CSS_SELECTOR, "article.product-miniature")

    # Название товара
    PRODUCT_TITLE = (By.CSS_SELECTOR, "a.product-miniature__title")

    # Цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product-miniature__price")

    # Ссылка на первый товар (для перехода в карточку)
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, "a.product-miniature__title")

    # Блок сортировки
    SORT_DROPDOWN = (By.CSS_SELECTOR, "button#sort_dropdown_button")

    # Пагинация / информация о количестве
    PAGINATION_INFO = (By.CSS_SELECTOR, "div.pagination__number")

    def open_catalog(self, path="/9-art"):
        self.open(path)

    def check_elements(self):
        """Проверяет 5+ ключевых элементов на странице каталога."""
        self.is_visible(self.PAGE_TITLE)
        self.is_visible(self.PRODUCTS_CONTAINER)
        self.is_visible(self.PRODUCT_CARD)
        self.is_visible(self.PRODUCT_TITLE)
        self.is_visible(self.PRODUCT_PRICE)
        self.is_visible(self.SORT_DROPDOWN)

    def click_first_product(self):
        """Кликает по названию первого товара."""
        self.is_clickable(self.FIRST_PRODUCT_LINK).click()