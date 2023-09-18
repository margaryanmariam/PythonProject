import time
from tests_.basetest_.baseTest import BaseTest
from pages_.logIn_.logInPage import LogInTest
from pages_.naviganBar_.navigationBar import NavigationBar

class LoginPageTest(BaseTest):
    def test_valid_login(self):
        loginPageObj = LogInTest(self.driver)
        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()

        #Assertion
        navigationBarObj = NavigationBar(self.driver)
        self.assertEqual(navigationBarObj.get_user_name(), "Fname")

    def test_invalid_login(self):
        loginPageObj = LogInTest(self.driver)
        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun333")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()

        #Assertion
        self.assertEqual(loginPageObj.get_incorrect_password_error_message(), "Your password is incorrect")