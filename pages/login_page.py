from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class LoginPage(BasePage):
    __LP_LOGIN_BUTTON = (By.ID, "edit-submit")
    __LP_LOGIN_FIELD = (By.XPATH, "//*[@id='edit-name']")
    __LP_PASSWORD_FIELD = (By.ID, "edit-pass")
    __LP_FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@id='edit-forgot']/a")
    __LP_KASEYAONE_BUTTON = (By.XPATH, "//a[text()='Learn More about KaseyaOne']")
    __LP_ALERT_MESSAGE = (By.XPATH, "//a[@data-dismiss='alert']/..")

    def click_login_button(self):
        self.click(by_locator=self.__LP_LOGIN_BUTTON)

    def enter_valid_login(self):
        self.clear_field(by_locator=self.__LP_LOGIN_FIELD)
        self.click(by_locator=self.__LP_LOGIN_FIELD)
        self.fill(by_locator=self.__LP_LOGIN_FIELD, value=BasePage.VALID_EMAIL)

    def enter_invalid_login(self):
        self.clear_field(by_locator=self.__LP_LOGIN_FIELD)
        self.click(by_locator=self.__LP_LOGIN_FIELD)
        self.fill(by_locator=self.__LP_LOGIN_FIELD, value=BasePage.INVALID_EMAIL)

    def enter_valid_password(self):
        self.clear_field(by_locator=self.__LP_PASSWORD_FIELD)
        self.fill(by_locator=self.__LP_PASSWORD_FIELD, value=BasePage.VALID_PASSWORD)

    def enter_invalid_password(self):
        self.clear_field(by_locator=self.__LP_PASSWORD_FIELD)
        self.fill(by_locator=self.__LP_PASSWORD_FIELD, value=BasePage.INVALID_PASSWORD)

    def click_forgot_password_link(self):
        self.click(by_locator=self.__LP_FORGOT_PASSWORD_LINK)

    def click_login_with_kaseyaone_button(self):
        self.click(by_locator=self.__LP_KASEYAONE_BUTTON)

        # Get current window handle (parent window)
        parent_window = self.driver.window_handles[0]

        # Switch to the new window/tab
        for window_handle in self.driver.window_handles:
            if window_handle != parent_window:
                self.driver.switch_to.window(window_handle)
                break  # Remove this line to switch to the last child window/tab(if you have only two)
        self.explicitly_wait.until(expected_conditions.title_is("KaseyaOne"))

    def check_if_alert_is_present(self):
        return self.get_element(by_locator=self.__LP_ALERT_MESSAGE)
