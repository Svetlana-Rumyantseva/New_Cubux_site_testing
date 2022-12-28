from pages.base_page import BasePage
from locators import home_page_locators as hpl
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url1)

    def click_expenses_link(self):
        self.find_element(hpl.expenses_link).click()
        self.wait.until(EC.url_changes(self.find_current_url()), message=f"Page URL after link clicking is not changed")

    def click_incomes_link(self):
        self.find_element(hpl.incomes_link).click()
        self.wait.until(EC.url_changes(self.find_current_url()), message=f"Page URL after link clicking is not changed")

    def click_balance_link(self):
        self.find_element(hpl.balance_link).click()
