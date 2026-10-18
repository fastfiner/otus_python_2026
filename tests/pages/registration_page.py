from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    # Поле First name
    FIRSTNAME = (By.CSS_SELECTOR, "input[name='firstname']")

    # Поле Last name
    LASTNAME = (By.CSS_SELECTOR, "input[name='lastname']")

    # Поле Email
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")

    # Поле Password
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")

    # Кнопка "Create account"
    SUBMIT = (By.CSS_SELECTOR, "button[data-link-action='save-customer']")

    def open_registration(self):
        """Открыть страницу регистрации (через iframe демо-стенда)"""
        self.driver.get("https://demo.prestashop.com/#/en/front")
        from selenium.webdriver.support import expected_conditions as EC
        iframe = self.wait.until(
            EC.presence_of_element_located((By.ID, "framelive"))
        )
        self.driver.switch_to.frame(iframe)
        self.driver.get(f"{self.base_url}/registration")

    def check_elements(self):
        """Проверяет 5 ключевых элементов на странице регистрации."""
        self.is_visible(self.FIRSTNAME)
        self.is_visible(self.LASTNAME)
        self.is_visible(self.EMAIL)
        self.is_visible(self.PASSWORD)
        self.is_visible(self.SUBMIT)