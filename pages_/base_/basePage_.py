from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout, 0.3).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print("ERROR: ELEMENT NOT FOUND")
            exit(5)

    def _find_elements(self, locator, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout, 0.3).until(EC.visibility_of_all_elements_located(locator))
            return elements
        except:
            return None

    def _clear_and_send_keys(self, locator, text):
        locator.clear()
        locator.send_keys(text)
