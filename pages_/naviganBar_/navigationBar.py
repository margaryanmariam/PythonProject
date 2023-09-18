from selenium.webdriver.common.by import By
from pages_.base_.basePage_ import BasePage
from selenium.webdriver.common.keys import Keys



class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__userNameLocator = (By.ID, "nav-link-accountList-nav-line-1")
        self.__searchInput = (By.CSS_SELECTOR, "input[id='twotabsearchtextbox']")
        self.__cartLocator = (By.CSS_SELECTOR, "div[id='nav-cart-count-container']")


    def get_user_name(self):
        userNameElement = self._find_element(self.__userNameLocator)
        return (userNameElement.text.split(" "))[1]

    def search_for_product(self, text):
        searchInputElement = self._find_element(self.__searchInput)
        self._clear_and_send_keys(self._find_element(self.__searchInput), text)
        searchInputElement.send_keys(Keys.ENTER)

    def go_to_cart(self):
        cartButton = self._find_element(self.__cartLocator)
        cartButton.click()