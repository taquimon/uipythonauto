import logging

from selenium import webdriver
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class BrowserManager:
    def __init__(self):
        self.driver = None
        self.browser_list = ["CHROME", "FIREFOX", "EDGE"]

    def launch_browser(self, browser):
        print(browser)
        browser = browser.upper()

        if browser in self.browser_list:

            match browser:
                case "CHROME":
                    self.driver = webdriver.Chrome()
                case "FIREFOX":
                    self.driver = webdriver.Firefox()
                case "EDGE":
                    self.driver = webdriver.Edge()
            LOGGER.debug("Browser supported")
        else:
            LOGGER.error("Unsupported browser")

        return self.driver

    def browser_version(self):
        return self.driver.capabilities['browserVersion'] if self.driver else None


if __name__ == '__main__':
    b = BrowserManager()
    b.launch_browser("Edge")
    b.driver.get("http://demoqa.com")
    print(b.driver.title)
    print(b.browser_version())
    b.driver.quit()
