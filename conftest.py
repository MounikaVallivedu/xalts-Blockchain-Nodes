"""Pytest configuration file"""  # Pytest configuration file

import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Create and return WebDriver instance"""
    driver = get_driver()
    yield driver
    driver.quit()