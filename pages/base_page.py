from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.chains = ActionChains(driver)
        self.base_url = 'https://new.cubux.net/'
        self.base_url1 = 'https://new.cubux.net/team/293036'
        self.base_url2 = 'https://new.cubux.net/team/293036/balance'

    def find_current_url(self):
        return self.driver.current_url

    def find_element(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_element(by_name, by_value)

    def find_elements(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_elements(by_name, by_value)

    def select(self, args: tuple, text):
        by_name, by_value = args
        return Select(self.driver.find_element(by_name, by_value)).select_by_value(text)
