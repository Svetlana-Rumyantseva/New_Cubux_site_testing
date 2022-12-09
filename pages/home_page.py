from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

expenses_link = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-expense"]')
incomes_link = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-income"]')
balance_link = (By.CSS_SELECTOR, 'a[class="btn-icon _size2 color-balance"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url1)

    def click_expenses_link(self):
        self.find_element(expenses_link).click()
        self.wait.until(EC.url_changes(self.find_current_url()), message=f"Page URL after link clicking is not changed")

    def click_incomes_link(self):
        self.find_element(incomes_link).click()
        self.wait.until(EC.url_changes(self.find_current_url()), message=f"Page URL after link clicking is not changed")

    def click_balance_link(self):
        self.find_element(balance_link).click()
