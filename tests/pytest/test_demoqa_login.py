import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestLoginPage:

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
        # cls.driver.get("http://demoqa.com/")

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

    @pytest.mark.usefixtures("driver")
    def test_login(self, driver):
        print(f"\ntest login")
        elements_menu = driver.find_element(By.XPATH, "//h5[text()='Elements']")
        elements_menu.click()
        print(driver.title)
        text_box = driver.find_element(By.XPATH, "//span[contains(@class, 'text') and text() = 'Text Box']")
        text_box.click()

        driver.find_element(By.ID, "userName").send_keys("taquimon")

        time.sleep(5)

    def test_login_2(self):
        print(f"\ntest login 2")

# if __name__ == '__main__':
#     pytest.main()
