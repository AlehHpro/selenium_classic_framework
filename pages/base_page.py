from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    VALID_EMAIL = "xxxxxxxxx@kaseya.com"
    VALID_PASSWORD = "xxxxxxxxx"
    INVALID_EMAIL = "invalid.email@kaseya.com"
    INVALID_PASSWORD = "password"

    # Singleton implementation. If driver does not exist we create one.
    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome()

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver
        self.explicitly_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element is not present on the page")
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator))
        self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element is not present on the page")
        self.driver.find_element(*by_locator).send_keys(value)

    def clear_field(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element is not present on the page")
        self.driver.find_element(*by_locator).clear()

    def quit_driver(self):
        self.driver.quit()
        print("\nRunning tearDown method...")
