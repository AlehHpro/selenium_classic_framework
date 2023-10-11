from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    __FP_EMAIL_FIELD = (By.ID, "edit-name")
    __FP_RESET_BUTTON = (By.ID, "edit-submit")
    __FP_BACK_TO_LOGIN_BUTTON = (By.XPATH, "//*[@id='block-system-main']/a")

    def enter_valid_email(self):
        self.fill(by_locator=self.__FP_EMAIL_FIELD, value=BasePage.VALID_EMAIL)

    def enter_invalid_email(self):
        self.fill(by_locator=self.__FP_EMAIL_FIELD, value=BasePage.INVALID_EMAIL)

    def click_reset_button(self):
        self.click(by_locator=self.__FP_RESET_BUTTON)

    def click_back_to_login_button(self):
        self.click(by_locator=self.__FP_BACK_TO_LOGIN_BUTTON)
