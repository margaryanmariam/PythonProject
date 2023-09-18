from pages_.base_.basePage_ import BasePage
from selenium.webdriver.common.by import By


class SearchResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__firstProduct = (By.XPATH, "//div[@class = 's-main-slot s-result-list s-search-results sg-row']/div[2]")

    def go_to_product_details(self):
        firstProductElement = self._find_element(self.__firstProduct)
        firstProductElement.click()