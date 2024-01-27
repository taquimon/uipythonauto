import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from libraries.browser_manager import BrowserManager


@pytest.fixture
def driver(request):
    driver_type = request.config.getoption('--driver')
    print(driver_type)
    driver = BrowserManager().launch_browser(driver_type)
    driver_version = BrowserManager().browser_version()
    print(f"Running tests on {driver_type} browser, version: {driver_version}")
    # load http://demoqa.com/ page
    driver.get("http://demoqa.com/")
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        '--driver', action='store', default='chrome', help='Driver to run tests'
    )
    print(parser)