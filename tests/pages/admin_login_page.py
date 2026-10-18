from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys


class AdminLoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    SUBMIT = (By.ID, "submit_login")
    LOGO = (By.CSS_SELECTOR, "img[alt='PrestaShop']")
    FORGOT_PASSWORD = (By.ID, "forgot-password-link")
    DASHBOARD = (By.CSS_SELECTOR, "h1.page-title")

    def open_admin(self):
        self.driver.get("https://demo.prestashop.com/#/en/back")
        iframe = self.wait.until(
            EC.presence_of_element_located((By.ID, "framelive"))
        )
        self.driver.switch_to.frame(iframe)

    def login(self, email, password):
        email_field = self.is_visible(self.EMAIL)
        password_field = self.is_visible(self.PASSWORD)

        self.driver.execute_script("arguments[0].value = '';", email_field)
        self.driver.execute_script("arguments[0].value = '';", password_field)

        email_field.send_keys(email)
        password_field.send_keys(password)

        print("Email:", email_field.get_attribute("value"))
        print("Password:", password_field.get_attribute("value"))

        self.is_clickable(self.SUBMIT).click()

    def is_logged_in(self):
        return self.is_visible(self.DASHBOARD).is_displayed()