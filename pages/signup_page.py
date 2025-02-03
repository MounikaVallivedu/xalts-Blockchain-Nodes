"""Signup page object"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignupPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(text(), 'Sign Up')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://xaltsocnportal.web.app/signup"

    def navigate(self):
        """Navigate to signup page"""
        self.driver.get(self.url)

    def signup(self, email, password):
        """Perform signup"""
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)
        self.click(self.SIGNUP_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)