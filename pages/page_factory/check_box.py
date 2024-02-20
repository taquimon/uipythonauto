import logging

from selenium.webdriver.common.by import By

from seleniumpagefactory.Pagefactory import PageFactory

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class ElementsCheckBox(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "CHECK_BOX_LINK": ("XPATH", "//span[contains(@class, 'text') and text() = 'Check Box']"),
        "CHECKBOX_HOME": ("XPATH", "//button[contains(@title, 'Toggle')]"),
        "CHECKBOX_DESKTOP": ("XPATH", "//span[@class='rct-title' and contains(text(),'Desktop')]"),
    }

    def navigate_to_check_box_page(self):
        self.CHECK_BOX_LINK.click()

    def click_on_home_checkbox(self):
        self.CHECKBOX_HOME.click()

    def click_on_desktop_checkbox(self):
        self.CHECKBOX_DESKTOP.click()