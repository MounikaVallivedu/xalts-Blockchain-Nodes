"""Login page object"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign In')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://xaltsocnportal.web.app/login"

    def navigate(self):
        """Navigate to login page"""
        self.driver.get(self.url)

    def login(self, email, password):
        """Perform login"""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_logged_in(self):
        """Check if user is logged in"""
        return "dashboard" in self.driver.current_url