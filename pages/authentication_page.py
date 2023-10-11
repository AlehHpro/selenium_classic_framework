from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthenticationPage(BasePage):
    __AP_PAGE_NAME = (By.XPATH, "//div/h1[contains(text(),'Authentication')]")
    __AP_BACK_BUTTON = (By.XPATH, "//*[@id='edit-actions']/a")

    def check_if_authentication_page_is_displayed(self):
        if_authentication_page_is_displayed = True
        try:
            self.get_element(self.__AP_PAGE_NAME)
        except NoSuchElementException:
            if_authentication_page_is_displayed = False
        return if_authentication_page_is_displayed

    def click_back_button(self):
        self.click(by_locator=self.__AP_BACK_BUTTON)
