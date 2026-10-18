from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.admin_login_page import AdminLoginPage
from pages.registration_page import RegistrationPage
from pages.cart_page import CartPage


# ============================================
# ЗАДАНИЕ 2.1–2.3 (5 тестов — по странице)
# ============================================
def test_home_page_elements(driver, base_url):
    page = HomePage(driver, base_url)
    page.open_home()
    page.check_elements()


def test_catalog_page_elements(driver, base_url):
    page = CatalogPage(driver, base_url)
    page.open_catalog()
    page.check_elements()


def test_product_page_elements(driver, base_url):
    catalog = CatalogPage(driver, base_url)
    catalog.open_catalog()
    catalog.click_first_product()
    product = ProductPage(driver, base_url)
    product.check_elements()


def test_admin_login_page_elements(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    page.open_admin()
    page.check_elements()


def test_registration_page_elements(driver, base_url):
    page = RegistrationPage(driver, base_url)
    page.open_registration()
    page.check_elements()


# ============================================
# ЗАДАНИЕ 3.1–3.4 
# ============================================
def test_admin_login_logout(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    page.open_admin()
    page.login("demo@prestashop.com", "demo_prestashop")  

    assert page.is_logged_in(), "Логин не выполнен"
    page.logout()
    assert not page.is_logged_in(), "Разлогин не выполнен"


import time


def test_add_product_to_cart(driver, base_url):
    """3.2 — добавляем товар с главной и проверяем корзину"""
    page = HomePage(driver, base_url)
    page.open_home()

    count_before = page.get_cart_count()
    page.add_first_product_to_cart()

    time.sleep(3)

    count_after = page.get_cart_count()
    assert count_after > count_before, (
        f"Товар не добавился. Было: {count_before}, стало: {count_after}"
    )


def test_currency_change_home(driver, base_url):
    """3.3 — смена валюты на главной"""
    home = HomePage(driver, base_url)
    home.open_home()

    prices_before = home.get_prices()
    home.change_currency("USD")
    prices_after = home.get_prices()

    assert prices_before != prices_after, "Цены не изменились на главной"


def test_currency_change_catalog(driver, base_url):
    """3.4 — смена валюты в каталоге"""
    catalog = CatalogPage(driver, base_url)
    catalog.open_catalog()

    prices_before = catalog.get_prices()
    catalog.change_currency("USD")
    prices_after = catalog.get_prices()

    assert prices_before != prices_after, "Цены не изменились в каталоге"