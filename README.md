# Enterprise E-Commerce Test Automation Framework

A scalable end-to-end test automation framework built using Python and PyTest, covering UI automation, REST API testing, database validation, cross-browser testing, parallel execution, Dockerized test execution, and GitHub Actions CI/CD.

## Tech Stack

- Python
- PyTest
- Selenium WebDriver
- Page Object Model (POM)
- REST API Testing
- Requests
- SQLite
- Docker
- Git & GitHub
- GitHub Actions
- PyTest-Xdist
- PyTest-HTML

---

## Framework Architecture

```text
                    E-Commerce Test Automation
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
        UI Automation    API Automation   Database Testing
             |                |                |
         Selenium         Requests          SQLite
             |                |                |
          PyTest          API Client     Database Client
             |                |                |
             +----------------+----------------+
                              |
                              v
                     PyTest Test Runner
                              |
                 +------------+------------+
                 |                         |
                 v                         v
              Docker                 GitHub Actions
                 |                         |
                 +------------+------------+
                              |
                              v
                         CI Test Results
```

---

## Project Structure

```text
ecommerce-automation/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── api/
│   ├── api_client.py
│   └── endpoints.py
│
├── config/
│   └── config.py
│
├── database/
│   ├── database_client.py
│   └── db_connection.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test_data/
│   ├── checkout_data.json
│   ├── data_loader.py
│   └── login_data.json
│
├── tests/
│   ├── api/
│   │   ├── test_auth_api.py
│   │   ├── test_negative_api.py
│   │   └── test_posts_api.py
│   │
│   ├── database/
│   │   └── test_users_database.py
│   │
│   └── ui/
│       ├── test_checkout.py
│       ├── test_e2e.py
│       ├── test_login.py
│       └── test_products.py
│
├── conftest.py
├── Dockerfile
├── pytest.ini
├── requirements.txt
├── .dockerignore
└── .gitignore
```

---

## UI Automation

The UI automation layer uses **Selenium WebDriver**, **PyTest**, and the **Page Object Model**.

### UI test scenarios

- Valid login
- Invalid login
- Product display validation
- Add product to cart
- Remove product from cart
- Product information validation
- Checkout required-field validation
- Complete end-to-end purchase flow

### Page Objects

The framework provides reusable page objects for:

- Login
- Products
- Cart
- Checkout
- Common page operations

The Page Object Model keeps page locators and page-specific actions separate from the test cases, making the framework easier to maintain.

---

## API Automation

The API automation layer uses Python's **Requests** library.

### API test coverage

- GET requests
- POST requests
- PUT requests
- DELETE requests
- Authentication
- Bearer-token authentication
- Negative API testing
- Invalid authentication testing
- Non-existent resource testing

A reusable `APIClient` abstracts common HTTP operations and authentication handling.

### API architecture

```text
Test
 |
 v
APIClient
 |
 +---- Authentication
 |
 +---- GET
 |
 +---- POST
 |
 +---- PUT
 |
 +---- DELETE
 |
 v
REST API
```

---

## Database Testing

The database layer uses **SQLite** for database validation.

### Database test coverage

- SELECT
- INSERT
- UPDATE
- DELETE
- User record validation
- Database state verification

A reusable `DatabaseClient` provides common database operations to the test layer.

### Database architecture

```text
Test
 |
 v
DatabaseClient
 |
 v
SQLite Database
 |
 v
Validation
```

---

## Test Data Management

Test data is separated from test logic using JSON files.

Example:

```text
test_data/
├── login_data.json
├── checkout_data.json
└── data_loader.py
```

This allows test data to be maintained independently from the test implementation.

---

## PyTest Fixtures and Configuration

The framework uses PyTest fixtures through `conftest.py` for reusable test setup and teardown.

The configuration layer handles common framework settings such as:

- Browser configuration
- Test environment behavior
- Timeout configuration
- CI-specific browser options

---

## Cross-Browser Testing

The framework supports:

- Chrome
- Firefox
- Edge

Examples:

```bash
pytest -v --browser chrome
pytest -v --browser firefox
pytest -v --browser edge
```

GitHub Actions executes Chrome in headless mode.

---

## Parallel Test Execution

**PyTest-xdist** is used for parallel test execution.

Example:

```bash
pytest -v -n 2
```

This executes the test suite using two worker processes.

Parallel execution can help reduce overall test execution time when the suite grows.

---

## Test Reporting

The framework uses **PyTest-HTML** for HTML test reports.

Generate a report with:

```bash
pytest -v --html=reports/report.html
```

The generated reports are kept out of source control.

---

## Failure Screenshots

The framework captures screenshots when UI tests fail.

Screenshots are stored in:

```text
screenshots/
```

The screenshots directory is excluded from Git through `.gitignore`.

---

## Docker

The framework is containerized using Docker to provide a reproducible test execution environment.

The Docker image contains:

- Python
- Project dependencies
- Google Chrome
- Test framework
- Test suite

### Build Docker image

```bash
docker build -t ecommerce-automation .
```

### Run tests in Docker

```bash
docker run --rm ecommerce-automation
```

Current Docker execution:

```text
21 passed
```

---

## CI/CD with GitHub Actions

GitHub Actions automatically builds the Docker image and executes the test suite when code is pushed or a pull request is created.

### CI/CD pipeline

```text
Developer
   |
   | git push / pull request
   v
GitHub
   |
   v
GitHub Actions
   |
   v
Build Docker Image
   |
   v
Run PyTest Suite
   |
   v
21 Automated Tests
   |
   v
Test Result
```

### Workflow

The CI workflow is located at:

```text
.github/workflows/tests.yml
```

The workflow:

1. Checks out the repository.
2. Builds the Docker image.
3. Runs the complete test suite inside the Docker container.
4. Reports the test result.

The Docker-based GitHub Actions workflow has been successfully executed with all **21 tests passing**.

---

## Test Coverage

The current framework contains **21 automated tests** across multiple testing layers.

| Testing Layer | Coverage |
|---|---|
| UI | Login, products, cart, checkout, E2E |
| API | CRUD, authentication, negative scenarios |
| Database | SELECT, INSERT, UPDATE, DELETE |
| Cross-browser | Chrome, Firefox, Edge |
| Parallel execution | PyTest-xdist |
| Reporting | PyTest-HTML |
| CI/CD | GitHub Actions |
| Containerization | Docker |

---

## Key Framework Features

- Page Object Model
- Reusable page utilities
- Reusable API client
- Reusable database client
- UI automation
- REST API automation
- Database validation
- Positive and negative test scenarios
- Data-driven testing
- Cross-browser execution
- Parallel test execution
- Explicit synchronization
- Failure screenshots
- HTML reporting
- Dockerized test execution
- GitHub Actions CI/CD
- Git and GitHub integration

---

## Project Highlights

- Built a multi-layer automation framework covering **UI, API, and database testing**.
- Implemented reusable Page Object Model components for UI automation.
- Developed reusable API and database client abstractions.
- Added positive and negative test scenarios.
- Implemented cross-browser test execution.
- Implemented parallel test execution using PyTest-xdist.
- Added failure screenshot capture and HTML reporting.
- Containerized the test framework using Docker.
- Integrated Docker-based test execution with GitHub Actions CI/CD.
- Verified the complete automation suite with **21 automated tests passing**.

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Phani9123/ecommerce-automation.git
cd ecommerce-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the complete test suite

```bash
pytest -v
```

---

## Run Specific Test Layers

### Run UI tests

```bash
pytest -v tests/ui
```

### Run API tests

```bash
pytest -v tests/api
```

### Run database tests

```bash
pytest -v tests/database
```

### Run tests in parallel

```bash
pytest -v -n 2
```

### Run Chrome tests

```bash
pytest -v --browser chrome
```

### Run Firefox tests

```bash
pytest -v --browser firefox
```

### Run Edge tests

```bash
pytest -v --browser edge
```

---

## Run Tests with Docker

Build the image:

```bash
docker build -t ecommerce-automation .
```

Run the tests:

```bash
docker run --rm ecommerce-automation
```

Expected result:

```text
21 passed
```

---

## GitHub Actions

Every push or pull request triggers the automated CI workflow.

```text
Code Change
    |
    v
Git Push / Pull Request
    |
    v
GitHub Actions
    |
    v
Docker Build
    |
    v
Automated Test Execution
    |
    v
Test Result
```

This provides automated validation of the framework in a clean Docker environment.

---

## Example Test Commands

Run all tests:

```bash
pytest -v
```

Run tests with HTML reporting:

```bash
pytest -v --html=reports/report.html
```

Run tests in parallel:

```bash
pytest -v -n 2
```

Run a specific test:

```bash
pytest -v tests/ui/test_e2e.py
```

---

## Repository

GitHub Repository:

https://github.com/Phani9123/ecommerce-automation

---

## Author

**Phani**

GitHub:

https://github.com/Phani9123