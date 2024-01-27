from selenium.webdriver.common.by import By

from pages.common import Common


class ElementsTextBox(Common):

    TEXT_BOX_LINK = (By.XPATH, "//span[contains(@class, 'text') and text() = 'Text Box']")
    USER_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")

    def navigate_to_elements_text_box_page(self):
        self.wait_for(self.TEXT_BOX_LINK).click()

    def enter_full_name(self, full_name):
        self.wait_for(self.USER_NAME).send_keys(full_name)

    def enter_email(self, email):
        self.wait_for(self.EMAIL).send_keys(email)

    def enter_current_address(self, current_address):
        self.wait_for(self.CURRENT_ADDRESS).send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.wait_for(self.PERMANENT_ADDRESS).send_keys(permanent_address)

    def click_submit(self):
        self.wait_for(self.SUBMIT).click()