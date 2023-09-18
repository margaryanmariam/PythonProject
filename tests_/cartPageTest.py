import time
from tests_.basetest_.baseTest import BaseTest
from pages_.logIn_.logInPage import LogInTest
from pages_.naviganBar_.navigationBar import NavigationBar
from pages_.naviganBar_.cartPage import CartPage

class CartPageTest(BaseTest):
    def test_product_deletion(self):
        loginPageObj = LogInTest(self.driver)
        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.go_to_cart()
        cartPageObj = CartPage(self.driver)
        productName = cartPageObj.get_first_product_name()
        cartPageObj.delete_first_product()
        confirmationText = cartPageObj.get_deleting_confirmation_text()

        #Assertion
        self.assertTrue(cartPageObj.isSubstring(confirmationText, productName))

    def test_all_product_deletion(self):
        loginPageObj = LogInTest(self.driver)
        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.go_to_cart()
        cartPageObj = CartPage(self.driver)
        cartPageObj.delete_all_products()
        time.sleep(2)

        # Assertion
        self.assertEqual(cartPageObj.get_cart_empty_confirmation_text(), "Your Amazon Cart is empty.")