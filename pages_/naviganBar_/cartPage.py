
from pages_.base_.basePage_ import BasePage
from selenium.webdriver.common.by import By
class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__deleteFirstProductLocator = (By.XPATH, "(//span[@class='a-declarative']/input)[1]")
        self.__productListLocator = (By.CSS_SELECTOR, "div[class='sc-item-content-group']")
        self.__deletingConfirmationTextLocator = (By.XPATH, "(//span[@class='a-size-base']/a)[1]")
        self.__firstProductNameLocator = (By.XPATH, "(//span[@class='a-truncate-cut'])[1]")
        self.__cartEmptyTextLocator = (By.CSS_SELECTOR, "div[class='a-row sc-cart-header']>div>h1")

    def delete_first_product(self):
        deleteFirstProductElement = self._find_element(self.__deleteFirstProductLocator)
        deleteFirstProductElement.click()

    def get_first_product_name(self):
        firstProductNameElement = self._find_element(self.__firstProductNameLocator)
        return firstProductNameElement.text

    def get_deleting_confirmation_text(self):
        deletingConfirmationTextElement = self._find_element(self.__deletingConfirmationTextLocator)
        return deletingConfirmationTextElement.text.split("...")[0]

    def isSubstring(self, substring, fullstring):
        return substring in fullstring

    def delete_all_products(self):
        allProducts = self._find_elements(self.__productListLocator)
        if allProducts is not None and len(allProducts) > 0:
          for product in allProducts:
             self.delete_first_product()
        else:
            return "Your Amazon Cart is empty."

    def get_cart_empty_confirmation_text(self):
        cartEmptyConfirmationTextElement = self._find_element(self.__cartEmptyTextLocator)
        return cartEmptyConfirmationTextElement.text