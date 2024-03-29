import logging

import pytest
import time

from selenium.webdriver.common.by import By

from pages.page_factory.check_box import ElementsCheckBox
from pages.page_factory.text_box import ElementsTextBox
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestElementsTextBox:

    # ---------------------------
    # Class level setup/teardown
    # ---------------------------

    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which usually contains tests)."""
        print(f"\nSetUp (class)")
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

    # @pytest.mark.usefixtures("browser")
    def test_fill_text_box_elements(self, browser):
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
        browser.get("http://demoqa.com/text-box")

        textbox = ElementsTextBox(browser)
        textbox.navigate_to_elements_text_box_page()
        textbox.enter_full_name("Edwin Taquichiri")
        textbox.enter_email("taquimon@gmail.com")
        textbox.enter_current_address("My Address")
        textbox.enter_permanent_address("Ticti Norte")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        textbox.click_submit()

    def test_fill_text_box_elements_2(self, browser):
        LOGGER.info("Test Elements TextBox 2")
        browser.get("http://demoqa.com/text-box")

        textbox = ElementsTextBox(browser)
        textbox.navigate_to_elements_text_box_page()
        textbox.enter_full_name("Edwin Taquichiri")
        textbox.enter_email("taquimon@gmail.com")

# if __name__ == '__main__':
#     pytest.main()
