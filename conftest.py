import os
import pytest
from selenium import webdriver
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, firefox, or edge"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":

        options = webdriver.ChromeOptions()

        if os.getenv("CI"):
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            options=options
        )

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    yield driver

    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)