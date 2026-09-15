from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.config import LOGIN_URL


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Login fields
        self.username = (
            By.ID,
            "user-name"
        )

        self.password = (
            By.ID,
            "password"
        )

        self.login_button = (
            By.ID,
            "login-button"
        )

        # Invalid login error message
        self.error_message = (
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        )

        self.url = LOGIN_URL

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.enter_text(
            self.username,
            username
        )

    def enter_password(self, password):
        self.enter_text(
            self.password,
            password
        )

    def click_login(self):
        self.click(
            self.login_button
        )

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        self.wait.until(
            lambda driver:
                "inventory" in driver.current_url
                or len(driver.find_elements(*self.error_message)) > 0
        )

    def get_error_message(self):
        return self.get_text(
            self.error_message
        )