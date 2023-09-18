import time
from tests_.basetest_.baseTest import BaseTest
from pages_.logIn_.logInPage import LogInTest
from pages_.naviganBar_.navigationBar import NavigationBar
from pages_.productRelatedPages_.productDetailsPage import ProductDetails
from pages_.productRelatedPages_.searchResultPage import SearchResult

class ProductDetailsPageTest(BaseTest):

    def test_add_to_cart(self):
        loginPageObj = LogInTest(self.driver)
        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.search_for_product("agv helmet")
        searchResultObj = SearchResult(self.driver)
        searchResultObj.go_to_product_details()
        productDetailsObj = ProductDetails(self.driver)
        productDetailsObj.add_to_cart()

        #Assertion
        self.assertEqual(productDetailsObj.product_added_to_cart(), "Added to Cart")
