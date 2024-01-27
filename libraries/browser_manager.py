from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class BrowserManager:
    def __init__(self, driver):
        self.driver = driver
        self.browser_list = ["CHROME", "FIREFOX", "EDGE"]

    def launch_browser(self, browser):
        print(browser)
        browser = browser.upper()
        if browser in self.browser_list:
            print("Browser supported")
            if browser == "CHROME":
                self.driver = webdriver.Chrome()
            elif browser == "FIREFOX":
                self.driver = webdriver.Firefox()
            else:
                self.driver = webdriver.Edge()
        else:
            print("Unsupported browser")

    def browser_version(self):
        return self.driver.capabilities['browserVersion']


if __name__ == '__main__':
    b = BrowserManager(driver=webdriver)
    b.launch_browser("Firefox")
    b.driver.get("http://demoqa.com")
    print(b.driver.title)
    print(b.browser_version())
    b.driver.quit()
