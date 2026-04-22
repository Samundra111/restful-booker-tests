# Restful Booker QA Automation Project

A complete QA automation project for Restful Booker hotel booking application covering both API and UI testing.

## Tech Stack

- Python 3.9
- Pytest
- Playwright (UI Automation)
- Requests (API Automation)
- Pydantic (Schema Validation)
- Allure Reports
- GitHub Actions (CI/CD)

## Project Structure
restful-booker-tests/
├── pages/
│   ├── booking_page.py           # Room booking POM
│   ├── contact_page.py           # Contact form POM
│   └── admin_page.py             # Admin panel POM
├── tests/
│   ├── test_ui.py                # UI E2E tests
│   ├── test_booking_api.py       # API CRUD tests
│   ├── test_authentication.py    # Auth tests
│   └── test_schema_validation.py # Schema validation
├── conftest.py                   # Shared fixtures
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Dependencies
├── .env                          # Environment variables
└── .gitignore                    # Git ignore rules

## Test Coverage

### UI Tests
- Room booking E2E flow
- Contact form successful submission
- Contact form empty validation
- Admin login with valid credentials
- Admin login with invalid credentials
- Admin logout

### API Tests
- GET all bookings
- GET single booking
- POST create booking
- PUT update booking
- DELETE booking
- Verify booking deleted after DELETE

### Authentication Tests
- Get token with valid credentials
- Get token with invalid credentials
- Missing credentials handling

### Schema Validation Tests
- Validate booking response schema
- Validate field types (string, integer, boolean)
- Validate nested bookingdates schema

## How to Run

### Install dependencies
pip install -r requirements.txt
playwright install

### Run all tests
pytest tests/ -v

### Run UI tests only
pytest tests/test_ui.py -v

### Run UI tests headed (see browser)
pytest tests/test_ui.py -v --headed

### Run UI tests with slow motion
pytest tests/test_ui.py -v --headed --slowmo=1000

### Run API tests only
pytest tests/test_booking_api.py -v

### Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

### Run with Allure report
pytest tests/ -v --alluredir=reports/allure-results
allure serve reports/allure-results

### Run in parallel
pytest tests/ -v -n=2

## Environment Variables

Create a `.env` file in root directory:
BASE_URL=https://restful-booker.herokuapp.com

## CI/CD

Tests run automatically on every push to main branch via GitHub Actions.
- API tests run on every push
- HTML report uploaded as artifact after every run

## Key Concepts Covered

- Page Object Model (POM)
- API automation with Requests
- UI automation with Playwright
- Schema validation with Pydantic
- Fixtures and conftest.py
- Parametrize
- CI/CD with GitHub Actions
- Allure Reports
- Parallel test execution