import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    driver_type = request.config.getoption('--driver')
    print(driver_type)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver_version = driver.capabilities['browserVersion']
    driver_name = driver.capabilities['browserName']
    print(f"Running tests on {driver_name} browser, version: {driver_version}")
    # load http://demoqa.com/ page
    driver.get("http://demoqa.com/")
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        '--driver', action='store', default='chrome', help='Driver to run tests'
    )
    print(parser)