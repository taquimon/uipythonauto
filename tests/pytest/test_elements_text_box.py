import logging

import pytest
import time

from selenium.webdriver.common.by import By

from pages.elements.text_box import ElementsTextBox
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestElementsTextBox:

    # ---------------------------
    # Class level setup/teardown
    # ---------------------------

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which usually contains tests)."""
        # print(f"\nSetUp (class)")
        # # initialize webdriver
        # cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #
        # # load http://demoqa.com/ page

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to setup_class. """
        print(f"\ntearDown (class)")
        # cls.driver.close()

    # ---------------------------
    # Class level setup/teardown
    # ---------------------------
    def setup_method(self):
        """
        setup any state tied to the execution of the given method in a class.  setup_method is
        invoked for every test method of a class.
        """
        print(f"\nSetUp method")

    def teardown_method(self):
        """
        teardown any state that was previously setup with a setup_method call.
        """
        print(f"\ntearDown")

    # @pytest.mark.usefixtures("driver")

    @pytest.mark.usefixtures("driver")
    def test_fill_text_box_elements(self, driver):
        LOGGER.info("Test Elements TextBox")
        # elements_menu = driver.find_element(By.XPATH, "//h5[text()='Elements']")
        # elements_menu.click()
        # print(driver.title)
        # text_box = driver.find_element(By.XPATH, "//span[contains(@class, 'text') and text() = 'Text Box']")
        # text_box.click()
        #
        # driver.find_element(By.ID, "userName").send_keys("taquimon")
        #
        # time.sleep(5)
        driver.get("http://demoqa.com/text-box")
        textbox = ElementsTextBox(driver)
        textbox.navigate_to_elements_text_box_page()
        textbox.enter_full_name("Edwin Taquichiri")
        textbox.enter_email("taquimon@gmail.com")
        textbox.enter_current_address("My Address")
        textbox.enter_permanent_address("Ticti Norte")
        textbox.click_submit()

    def test_login_2(self):
        print(f"\ntest login 2")

# if __name__ == '__main__':
#     pytest.main()
