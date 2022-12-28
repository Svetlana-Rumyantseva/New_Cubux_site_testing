import pytest
import allure
from datetime import date
from pages.balance_page import BalancePage


@allure.feature('The testing of difference type sorting')
class TestBalancePagePart1:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of incomes sorting')
    def test_incomes_sorting(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        elements = balance_page.find_amounts_values()
        sum_before_sort = sum(balance_page.get_number_values(elements, 'Incomes')[0])
        balance_page.click_incomes_button()
        elements = balance_page.find_amounts_values()
        sum_after_sort = sum(balance_page.get_number_values(elements, 'Incomes')[0])
        assert sum_before_sort == sum_after_sort, 'Incomes sorting is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of expenses sorting')
    def test_expenses_sorting(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        elements = balance_page.find_amounts_values()
        sum_before_sort = sum(balance_page.get_number_values(elements, 'Expenses')[1])
        balance_page.click_expenses_button()
        elements = balance_page.find_amounts_values()
        sum_after_sort = sum(balance_page.get_number_values(elements, 'Expenses')[1])
        assert sum_before_sort == sum_after_sort, 'Expenses sorting is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of loans sorting')
    def test_loans_sorting(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_loans_button()
        elements = balance_page.find_amounts_values()
        assert sum(balance_page.get_number_value(elements)) == -30, 'Loans sorting is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of transfers sorting.')
    def test_transfers_sorting(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_transfers_button()
        elements = balance_page.find_amounts_values()
        assert sum(balance_page.get_number_value(elements)) == 200, 'Transfers sorting is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of cash sorting')
    def test_sorting_by_cash(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.waiting()
        all_accounts_before_sort = balance_page.find_all_accounts()
        cash_before = balance_page.calculate_operation(all_accounts_before_sort, 'Cash')
        balance_page.click_cash_select()
        balance_page.waiting()
        all_accounts_after_sort = balance_page.find_all_accounts()
        cash_after = balance_page.calculate_operation(all_accounts_after_sort, 'Cash')
        assert cash_before == cash_after, 'The sorting by cash is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of credit card sorting')
    def test_sorting_by_credit_card(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.waiting()
        all_accounts_before_sort = balance_page.find_all_accounts()
        card_before = balance_page.calculate_operation(all_accounts_before_sort, 'Credit card')
        balance_page.click_card_select()
        balance_page.waiting1()
        all_accounts_after_sort = balance_page.find_all_accounts()
        card_after = balance_page.calculate_operation(all_accounts_after_sort, 'Credit card')
        assert card_before == card_after, 'The sorting by credit card is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of date sorting')
    def test_sorting_by_date(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        start_date, finish_date = '01/12/2022', '05/12/2022'
        dates_before_sort = balance_page.find_dates()
        counter_before = balance_page.calculate_dates(dates_before_sort, start_date, finish_date)
        balance_page.click_period_from_to(start_date, finish_date)
        dates_after_sort = balance_page.find_dates1()
        counter_after = balance_page.calculate_dates(dates_after_sort, start_date, finish_date)
        assert counter_before == counter_after, 'The sorting by dates is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of amounts sorting with value 50')
    def test_amounts_selection(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amounts_before_sort = balance_page.find_amounts_values()
        counter_before = balance_page.calculate_same_amounts(amounts_before_sort, 50)
        balance_page.click_sum_selection(50)
        amounts_after_sort = balance_page.find_amounts_values()
        counter_after = balance_page.calculate_same_amounts(amounts_after_sort, 50)
        assert counter_before == counter_after, 'The sorting by amount is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of amounts sorting with value 0')
    def test_amounts_selection1(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amounts_before_sort = balance_page.find_amounts_values()
        counter_before = balance_page.calculate_same_amounts(amounts_before_sort, '0')
        balance_page.click_sum_selection(0)
        amounts_after_sort = balance_page.find_amounts_values()
        counter_after = balance_page.calculate_same_amounts(amounts_after_sort, '0')
        assert counter_before == counter_after == 0 and \
               balance_page.get_sorting_result() == 'There are no transactions', 'The sorting by amount is wrong'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of category names sorting')
    def test_category_choice(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        all_categories = balance_page.find_categories()
        counter_before = balance_page.calculate_categories(all_categories, 'Salary', 'green')
        balance_page.click_category_choice()
        all_categories = balance_page.find_categories()
        counter_after = balance_page.calculate_categories(all_categories, 'Salary', 'green')
        assert counter_before == counter_after, 'The sorting by categories is wrong'


@allure.feature('The testing of transaction creation, deletion, copy and required_fields of the transaction')
class TestBalancePagePart2:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of required field: account')
    def test_required_fields(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_plus_button()
        balance_page.fill_amount_field(10000)
        balance_page.click_ok_green_button()
        message = balance_page.find_alert2()
        assert message == "Select an account"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of required field: category')
    def test_required_fields1(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_plus_button()
        balance_page.fill_amount_field(10000)
        balance_page.choose_account_()
        balance_page.click_ok_green_button()
        message = balance_page.find_alert3()
        assert message == "Select a category"

    MONEY = [0, -1, ' ', 35 - 55, '', -6 * 5, -300, 'gfngh']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The negative testing of required field: amount. Bug for amount value = 0')
    @pytest.mark.parametrize("money", MONEY)
    def test_amount_field_negative(self, driver, authorization, money):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_minus_button()
        balance_page.fill_amount_field(money)
        balance_page.choose_account()
        balance_page.choose_category()
        balance_page.click_ok_red_button()
        message = balance_page.find_alert1()
        balance_page.click_alert_submit()
        assert message == "Type an amount"

    MONEY1 = [0.01, 125.136, 18 + 22, 1000 / 2, 5 * 3, 5 ** 2, 100 - 30,
              100000000000000000]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The positive testing of required field: amount')
    @pytest.mark.parametrize("money1", MONEY1)
    def test_amount_field_positive(self, driver, authorization, money1):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amount_values_before = balance_page.find_amounts_values()
        balance_page.click_minus_button()
        balance_page.fill_amount_field(money1)
        balance_page.choose_account()
        balance_page.choose_category()
        balance_page.click_red_ok()
        amount_values_after = balance_page.find_amounts_values()
        if len(amount_values_after) == len(amount_values_before) + 1:
            amount_values_after_create = balance_page.find_amounts_values()
            balance_page.click_deletion_icon()
            balance_page.find_deletion_alert()
            balance_page.click_deletion_alert_submit()
            amount_values_after_del = balance_page.find_amounts_values()
            assert len(amount_values_after_del) == len(amount_values_after_create) - 1, 'A new operation is not deleted'
        else:
            assert len(amount_values_after) == len(amount_values_before) + 1, 'A new operation is not created'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of transaction creation and deletion')
    def test_transaction_creation_and_deletion(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amount_values_before = balance_page.find_amounts_values()
        balance_page.click_plus_button()
        balance_page.fill_amount_field(9999999)
        balance_page.choose_account_()
        balance_page.choose_category_()
        balance_page.click_green_ok()
        amount_values_after = balance_page.find_amounts_values()
        if len(amount_values_after) == len(amount_values_before) + 1:
            amount_values_after_create = balance_page.find_amounts_values()
            balance_page.click_deletion_icon()
            message = balance_page.find_deletion_alert()
            if message == "Are you sure to delete the transaction? This action cannot be undone.":
                balance_page.click_deletion_alert_submit()
                amount_values_after_del = balance_page.find_amounts_values()
                assert len(amount_values_after_create) - 1 == len(amount_values_after_del)
            else:
                amount_values_after_del = balance_page.find_amounts_values()
                assert len(amount_values_after_create) == len(
                    amount_values_after_del) + 1, 'A new operation is not deleted'
        else:
            assert len(amount_values_after) == len(amount_values_before) + 1, 'A new operation is not created'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of transaction copy')
    def test_transaction_copy(self, driver, authorization, operation_deletion):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amount_values_before = balance_page.find_amounts_values()
        balance_page.click_copy_icon()
        balance_page.click_green_ok()
        amount_values_after = balance_page.find_amounts_values()
        assert len(amount_values_after) == len(amount_values_before) + 1, 'The operation is not copied'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of transaction deletion: second version')
    def test_transaction_deletion_2nd_version(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amount_values_before = balance_page.find_amounts_values()
        balance_page.click_plus_button()
        balance_page.fill_amount_field(555555555555)
        balance_page.choose_account_()
        balance_page.choose_category_()
        balance_page.click_green_ok()
        amount_values_after = balance_page.find_amounts_values()
        if len(amount_values_after) == len(amount_values_before) + 1:
            amount_values_after_create = balance_page.find_amounts_values()
            balance_page.click_select_box()
            balance_page.click_deletion_icon1()
            message = balance_page.find_deletion_alert1()
            if message == "Are you sure to delete 1 transaction? This action cannot be undone.":
                balance_page.click_deletion_alert_submit1()
                amount_values_after_del = balance_page.find_amounts_values()
                assert len(amount_values_after_create) - 1 == len(amount_values_after_del), 'Operation is not deleted'
            else:
                amount_values_after_del = balance_page.find_amounts_values()
                assert len(amount_values_after_create) == len(
                    amount_values_after_del) + 1, 'An operation is not deleted'
        else:
            assert len(amount_values_after) == len(amount_values_before) + 1, 'An operation is not created'


@allure.feature('The transaction editing testing of the required fields of the transaction')
class TestBalancePagePart3:
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The testing of transaction field: amount')
    def test_transaction_edition_amount_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        amount_values_after_create = balance_page.find_amounts_values()
        numbers_after_create = balance_page.get_number_value(amount_values_after_create)
        balance_page.click_edit_icon()
        balance_page.edit_amount_value()
        balance_page.click_save_button()
        amount_values_after_edit = balance_page.find_amounts_values()
        numbers_after_edit = balance_page.get_number_value(amount_values_after_edit)
        assert numbers_after_create[0] == - 33333333333 and numbers_after_edit[0] == - 44444444444,\
            'An edited operation is not deleted'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edit testing of transaction field: account')
    def test_transaction_edition_account_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        current_account = balance_page.find_current_account()
        balance_page.click_edit_icon()
        balance_page.choose_new_account()
        balance_page.click_save_button()
        new_account = balance_page.find_current_account()
        assert current_account == 'Credit card' and new_account == 'Cash', 'The account is not edited'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edit testing of transaction field: category')
    def test_transaction_edition_category_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        current_category = balance_page.find_current_category()
        balance_page.click_edit_icon()
        balance_page.choose_new_category()
        balance_page.click_save_button()
        new_category = balance_page.find_current_category()
        assert current_category == 'Travels' and new_category == 'Car', 'The category is not edited'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edit testing of transaction field: date')
    def test_transaction_edition_date_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        current_date = balance_page.find_current_date()
        balance_page.click_edit_icon()
        balance_page.choose_new_date()
        balance_page.click_save_button()
        new_date = balance_page.find_current_date()
        assert new_date == '20/12/2022' and current_date == date.today().strftime('%d/%m/%Y'), 'The date is not edited'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edit testing of transaction field: category')
    def test_transaction_edition_description_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        current_description = balance_page.find_description()
        balance_page.click_edit_icon()
        balance_page.add_new_description("after editing")
        balance_page.click_save_button()
        new_description = balance_page.find_description()
        print(current_description, new_description)
        assert current_description == 'Simple test' and new_description == 'after editing', \
            'The description is not edited'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edit testing of transaction field: project')
    def test_transaction_edition_project_field(self, driver, authorization, transaction_for_edit):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        current_project = balance_page.find_project_name()
        balance_page.click_edit_icon()
        balance_page.choose_new_project()
        balance_page.click_save_button()
        new_project = balance_page.find_project_name()
        assert current_project == '' and new_project == 'apple', 'The project name is not edited'


@allure.feature('The settings testing of the participants tab, projects tab')
class TestBalancePagePart4:
    EMAIL = ['my@gmail.com', 'my@site.com', 'hello@1.2', '5@1.2', 'm#y@mail.ru', f"{'h'*64}" + '.k.ru']

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('The positive testing of email field for the participants tab')
    @pytest.mark.skip('Bug: Delete icon is an invisible if so long email exits in general emails list. '
                      'for an example: ' f"{'h'*64}" + '.k.ru')
    @pytest.mark.parametrize("email", EMAIL)
    def test_participants_tab_settings_positive(self, driver, authorization, email):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_settings_icon()
        balance_page.click_participants_tab()
        balance_page.fill_email_field(email)
        balance_page.select_rights()
        balance_page.click_invite_button()
        invite = balance_page.find_invitation()
        balance_page.click_participant_deletion()
        balance_page.find_deletion_alert2()
        balance_page.click_deletion_button()
        assert invite == 'Invited', 'Email is wrong'
        assert len(balance_page.find_emails()) == 2, 'Email is not deleted'

    EMAIL1 = [' my@mail.ru', 'my@157dhgf', 'myrambler.ru', '@gmail.com', 'hello@ . ', 'my@mail#.ru', 'my@mail.r$u',
              f"{'h'*65}" + '.k.ru']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The negative testing of email field for the participants tab')
    @pytest.mark.parametrize("email1", EMAIL1)
    def test_participants_tab_settings_negative(self, driver, authorization, email1):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_settings_icon()
        balance_page.click_participants_tab()
        balance_page.fill_email_field(email1)
        balance_page.select_rights()
        balance_page.click_invite_button()
        assert balance_page.get_alert_message() == 'Error: User Mail is not a valid email address.'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('The edition testing of projects tab')
    def test_project_tab_settings_for_creation_edition_and_deletion(self, driver, authorization):
        balance_page = BalancePage(driver)
        balance_page.open_page()
        balance_page.click_settings_icon()
        balance_page.click_project_tab()
        balance_page.click_add_project_button()
        balance_page.enter_project_name('my test')
        names_before = balance_page.find_project_names()
        balance_page.click_save()
        names_after = balance_page.find_project_names()
        name_index = names_after.index('my test')
        balance_page.click_project_edit_icon(name_index)
        balance_page.enter_project_name(' is edited')
        balance_page.click_edit_save_button()
        edit_name = balance_page.find_project_names()[name_index]
        balance_page.click_project_deletion(name_index)
        message = balance_page.find_deletion_alert3()
        balance_page.click_ok_deletion()
        assert names_after[name_index] == 'my test', 'The project_name is not created'
        assert edit_name == 'my test is edited', 'The project_name is not edited'
        assert message == 'Are you sure to delete the project?', 'The project_name is not deleted'
        assert len(names_after) - 1 == len(names_before), 'The project_name is not deleted'
