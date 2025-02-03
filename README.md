# Blockchain Portal Automation Testing

This project contains automated test cases for the Blockchain Portal application (xaltsocnportal.web.app) using Selenium WebDriver with Python.

## Project Structure

```
├── test_cases/
│   ├── test_auth.py       # Authentication test cases
│   └── test_data.py       # Test data and constants
├── pages/
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page object
│   └── signup_page.py     # Signup page object
├── utils/
│   └── driver_factory.py  # WebDriver initialization
├── requirements.txt       # Project dependencies
├── conftest.py           # Pytest configurations
└── README.md             # Project documentation
```

## Setup Instructions

1. Install Python 3.8 or higher
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run all tests:
```bash
pytest
```

To generate HTML report:
```bash
pytest --html=report.html
```

## Test Coverage

The automation suite covers:
- User Authentication
  - Sign Up
  - Sign In
  - Sign Out
- Both success and failure scenarios
- Input validation
- Error handling

## Test Data

- Test data is maintained in `test_cases/test_data.py`
- Includes valid and invalid test cases
- Follows specified format requirements:
  - Node ID format: "NodeID-{number}"
  - Wallet Address Format: "0x{checksum valid hexadecimal}"
  - IP Address: "X.X.X.X" where 0 <= X <= 255