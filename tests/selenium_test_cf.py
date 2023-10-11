import unittest

from pages.authentication_page import AuthenticationPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.kaseyaone_page import KaseyaonePage
from pages.login_page import LoginPage


class TestSelenium(unittest.TestCase):

    __login_page = LoginPage()

    def setUp(self) -> None:
        self.login_page = self.__login_page
        self.authentication_page = AuthenticationPage()
        self.forgot_password_page = ForgotPasswordPage()
        self.kaseyaone_page = KaseyaonePage()
        # print("\nRunning setUp method...")

        self.login_page.go_to_url(url="https://dev.darkwebid.io/user/login?destination=resellers")

    def test_login(self):
        # 1. Enter invalid login and submit.
        self.login_page.enter_invalid_login()
        self.login_page.click_login_button()
        if_alert_is_displayed = self.login_page.check_if_alert_is_present()
        self.assertTrue(if_alert_is_displayed)

        # 2. Enter valid login and submit.
        self.login_page.enter_valid_login()
        self.login_page.click_login_button()

        # 3. Enter invalid login and submit.
        self.login_page.enter_invalid_login()
        self.login_page.click_login_button()
        self.login_page.check_if_alert_is_present()

        # 4. Enter valid login, password and submit.
        self.login_page.enter_valid_login()
        self.login_page.enter_valid_password()
        self.login_page.click_login_button()

        # 5. Check that Authentication page is displayed.
        self.assertTrue(self.authentication_page.check_if_authentication_page_is_displayed())

        # 6. Click back button
        self.authentication_page.click_back_button()

    def test_forgot_password(self):
        # 1. Enter valid login and submit.
        self.login_page.enter_valid_login()
        self.login_page.click_login_button()

        # 2. Navigate to Forgot Password screen.
        self.login_page.click_forgot_password_link()

        # 3. Enter valid email and submit.
        self.forgot_password_page.enter_valid_email()
        self.forgot_password_page.click_reset_button()

        # 4. Navigate back to Log in screen.
        self.forgot_password_page.click_back_to_login_button()

    def test_kaseya_helpdesk_display(self):
        # 1. Navigate to Helpdesk screen.
        self.login_page.click_login_with_kaseyaone_button()
        self.assertTrue(self.kaseyaone_page.check_if_kaseyaone_page_is_displayed())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.__login_page.quit_driver()
        # print("\nRunning tearDown method...")


if __name__ == '__main__':
    unittest.main()
