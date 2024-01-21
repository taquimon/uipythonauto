from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# initialize webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# load http://demoqa.com/ page
driver.get("http://demoqa.com/")

# print the page title
print(driver.title)

# close the driver
driver.close()