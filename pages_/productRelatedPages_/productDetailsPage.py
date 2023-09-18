from pages_.base_.basePage_ import BasePage
from selenium.webdriver.common.by import By


class ProductDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__addToCart = (By.ID, "add-to-cart-button")
        self.__productAdded = (By.CSS_SELECTOR, "span[class *='a-size-medium-plus']")

    def add_to_cart(self):
        addToCartButton = self._find_element(self.__addToCart)
        addToCartButton.click()

    def product_added_to_cart(self):
        confirmationTextElement = self._find_element(self.__productAdded)
        return confirmationTextElement.text
