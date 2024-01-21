from selenium import webdriver
driver = webdriver.Chrome('/home/berserker/python/uidemoqa/chromedriver-linux64/chromedriver')
driver.get("https://bstackdemo.com/")

print(driver.title)

driver.close()