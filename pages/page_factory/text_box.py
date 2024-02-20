import logging

from selenium.webdriver.common.by import By

from seleniumpagefactory.Pagefactory import PageFactory

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class ElementsTextBox(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.timeout = 15

        # self.highlight = True       #(Optional - To highlight every webElement in PageClass)

    locators = {

        "TEXT_BOX_LINK": ("XPATH", "//span[contains(@class, 'text') and text() = 'Text Box']"),
        "USER_NAME": ("ID", "userName"),
        "EMAIL": ("ID", "userEmail"),
        "CURRENT_ADDRESS": ("ID", "currentAddress"),
        "PERMANENT_ADDRESS": ("ID", "permanentAddress"),
        "SUBMIT": ("ID", "submit")
    }

    def navigate_to_elements_text_box_page(self):
        self.TEXT_BOX_LINK.click()

    def enter_full_name(self, full_name):
        self.USER_NAME.send_keys(full_name)

    def enter_email(self, email):
        self.EMAIL.send_keys(email)

    def enter_current_address(self, current_address):
        self.CURRENT_ADDRESS.send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.PERMANENT_ADDRESS.send_keys(permanent_address)

    def click_submit(self):
        self.SUBMIT.click()
