import logging

import pytest
import time

from selenium.webdriver.common.by import By

from pages.page_factory.check_box import ElementsCheckBox
from pages.page_factory.text_box import ElementsTextBox
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestElementsCheckBox:

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

    def test_checkbox(self, browser):
        browser.get("http://demoqa.com/text-box")
        check_box = ElementsCheckBox(browser)
        check_box.navigate_to_check_box_page()
        check_box.click_on_home_checkbox()
        check_box.click_on_desktop_checkbox()
        time.sleep(3)

# if __name__ == '__main__':
#     pytest.main()
