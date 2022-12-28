import allure
from pages.home_page import HomePage


@allure.feature('Links testing on the home page')
class TestHomePage:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('The transition to the expenses page')
    def test_go_to_expenses_icon(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.click_expenses_link()
        assert 'https://new.cubux.net/team/293036/expense/details' == home_page.find_current_url()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('The transition to the incomes page')
    def test_go_to_incomes_icon(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.click_incomes_link()
        assert 'https://new.cubux.net/team/293036/income/details' == home_page.find_current_url()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('The transition to the balance page')
    def test_go_to_balance_icon(self, driver, authorization):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.click_balance_link()
        assert 'https://new.cubux.net/team/293036/balance' == home_page.find_current_url()
