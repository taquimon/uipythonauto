from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
url = 'http://demoqa.com/'
driver.get(url)

# load http://demoqa.com/ page
# driver.get("http://demoqa.com/")

# print the page title
print(driver.title)

# close the driver
driver.close()