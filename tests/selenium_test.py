import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

# initialize webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# load http://demoqa.com/ page
driver.get("http://demoqa.com/")

# print the page title
# elements_menu = driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card' and contains(., 'Elements')]")
elements_menu = driver.find_element(By.XPATH, "//h5[text()='Elements']")
elements_menu.click()
LOGGER.info(driver.title)
text_box = driver.find_element(By.XPATH, "//span[contains(@class, 'text') and text() = 'Text Box']")
text_box_links = driver.find_element(By.XPATH, "//span[contains(@class, 'text') and text() = 'Links']")
text_box_links.click()

links = driver.find_element(By.LINK_TEXT, "Bad Request")
# driver.find_element(By.ID, "userName").send_keys("taquimon")
links.click()
time.sleep(5)
# close the driver
driver.close()
