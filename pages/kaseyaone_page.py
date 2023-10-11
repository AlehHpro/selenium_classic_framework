from selenium.common import NoSuchElementException

from pages.base_page import BasePage


class KaseyaonePage(BasePage):

    def check_if_kaseyaone_page_is_displayed(self):
        if_kaseyaone_page_is_displayed = True
        try:
            self.driver.title == "KaseyaOne"
        except NoSuchElementException:
            if_kaseyaone_page_is_displayed = False
        return if_kaseyaone_page_is_displayed
