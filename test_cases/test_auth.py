"""Test cases for authentication functionality"""
import pytest
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from .test_data import VALID_USER, INVALID_USERS

class TestAuthentication:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignupPage(self.driver)

    def test_valid_login(self):
        """Test login with valid credentials"""
        self.login_page.navigate()
        self.login_page.login(VALID_USER["email"], VALID_USER["password"])
        assert self.login_page.is_logged_in()

    @pytest.mark.parametrize("test_data", INVALID_USERS)
    def test_invalid_login(self, test_data):
        """Test login with invalid credentials"""
        self.login_page.navigate()
        self.login_page.login(test_data["email"], test_data["password"])
        error_message = self.login_page.get_error_message()
        assert test_data["error"] in error_message

    def test_valid_signup(self):
        """Test signup with valid data"""
        self.signup_page.navigate()
        self.signup_page.signup(VALID_USER["email"], VALID_USER["password"])
        assert self.login_page.is_logged_in()

    @pytest.mark.parametrize("test_data", INVALID_USERS)
    def test_invalid_signup(self, test_data):
        """Test signup with invalid data"""
        self.signup_page.navigate()
        self.signup_page.signup(test_data["email"], test_data["password"])
        error_message = self.signup_page.get_error_message()
        assert test_data["error"] in error_message

    def test_logout(self):
        """Test logout functionality"""
        # First login
        self.login_page.navigate()
        self.login_page.login(VALID_USER["email"], VALID_USER["password"])
        assert self.login_page.is_logged_in()

        # Then logout
        self.login_page.click((By.ID, "logout-button"))
        assert not self.login_page.is_logged_in()