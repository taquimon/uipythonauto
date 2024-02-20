import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from libraries.browser_manager import BrowserManager
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture
def browser(request):
    # LOGGER = get_logger(__name__, logging.DEBUG)
    driver_type = request.config.getoption('--driver')
    LOGGER.info(f"Driver type: %s", driver_type)
    driver = BrowserManager().launch_browser(driver_type)
    driver.maximize_window()
    driver_version = driver.capabilities['browserVersion']
    print(f"Running tests on {driver_type} browser, version: {driver_version}")
    # load http://demoqa.com/ page
    # driver.get("http://demoqa.com/")
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        '--driver', action='store', default='chrome', help='Driver to run tests'
    )
    print(parser)
