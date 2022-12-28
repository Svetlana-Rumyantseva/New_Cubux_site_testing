import ast
from datetime import timedelta, datetime
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import balance_page_locators as bpl
from selenium.webdriver import Keys


class BalancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url2)

    def click_incomes_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.incomes_button).click()

    def click_expenses_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.expenses_button).click()

    @staticmethod
    def get_number_values(elements, value):
        incomes_green_list, expences_red_list, transfers_list, loans_list = [], [], [], []
        for elem in elements:
            rgba = elem.value_of_css_property('color')
            r, g, b, a = ast.literal_eval(rgba.strip("rgba"))
            hex_value = '#%02x%02x%02x' % (r, g, b)
            element = elem.text
            text = element[0] + element[5::]
            if "," in text:
                text = text.replace(",", ".")
            if " " in text:
                text = text.replace(" ", "", text.count(" "))
            if hex_value == '#6dba34' and value == 'Incomes':
                incomes_green_list.append(float(text))
            elif hex_value == '#e45c70' and value == 'Expenses':
                expences_red_list.append(float(text))

        return incomes_green_list, expences_red_list

    @staticmethod
    def get_number_value(elements):
        my_list = []
        for i in range(len(elements)):
            elem = elements[i].text
            text = elem[0] + elem[5::]
            if "," in text:
                text = text.replace(",", "")
            if " " in text:
                text = text.replace(" ", "", text.count(" "))
            my_list.append(float(text))
        return my_list

    def click_transfers_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.transfers_button).click()

    def click_loans_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.loans_button).click()

    def click_minus_button(self):
        self.find_element(bpl.minus_button).click()

    def fill_amount_field(self, money):
        self.find_element(bpl.number).send_keys(money)

    def choose_account(self):
        self.find_element(bpl.account).click()
        self.wait.until(EC.element_to_be_clickable(bpl.credit_card)).click()

    def choose_category(self):
        self.find_element(bpl.category).click()
        self.wait.until(EC.element_to_be_clickable(bpl.categories)).click()

    def click_ok_red_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.ok_red_button)).click()

    def find_alert1(self):
        self.wait.until(EC.visibility_of_element_located(bpl.alert1))
        return self.find_element(bpl.alert1).text

    def click_alert_submit(self):
        self.wait.until(EC.element_to_be_clickable(bpl.alert_submit)).click()

    def click_plus_button(self):
        self.find_element(bpl.plus_button).click()

    def click_ok_green_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.ok_green_button)).click()

    def choose_account_(self):
        self.find_element(bpl.account).click()
        self.wait.until(EC.element_to_be_clickable(bpl.cash)).click()

    def choose_category_(self):
        self.find_element(bpl.category).click()
        self.wait.until(EC.element_to_be_clickable(bpl.categories1)).click()

    def find_alert2(self):
        self.wait.until(EC.visibility_of_element_located(bpl.alert2))
        return self.find_element(bpl.alert2).text

    def find_alert3(self):
        self.wait.until(EC.visibility_of_element_located(bpl.alert3))
        return self.find_element(bpl.alert3).text

    def click_green_ok(self):
        self.wait.until(EC.element_to_be_clickable(bpl.ok_green_button)).click()
        self.wait.until(EC.invisibility_of_element(bpl.ok_green_button))

    def click_red_ok(self):
        self.wait.until(EC.element_to_be_clickable(bpl.ok_red_button)).click()
        self.wait.until(EC.invisibility_of_element(bpl.ok_red_button))

    def find_amounts_values(self):
        return self.find_elements(bpl.amount_value)

    def click_deletion_icon(self):
        self.find_element(bpl.deletion_icon).click()

    def find_deletion_alert(self):
        self.wait.until(EC.text_to_be_present_in_element(bpl.del_alert, "Are you sure to delete the transaction? "
                                                                        "This action cannot be undone."))
        return self.find_element(bpl.del_alert).text

    def click_deletion_alert_submit(self):
        self.wait.until(EC.element_to_be_clickable(bpl.del_alert_submit)).click()
        self.wait.until((EC.invisibility_of_element_located(bpl.del_alert_submit)))

    def click_copy_icon(self):
        self.find_element(bpl.copy_icon).click()

    def waiting(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))

    def waiting1(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element1))

    def find_all_accounts(self):
        elements = self.find_elements(bpl.all_accounts)
        my_accounts = []
        for elem in elements:
            my_accounts.append(elem.text)
        return ' '.join(my_accounts)

    @staticmethod
    def calculate_operation(my_string, value):
        counter = my_string.count(value)
        return counter

    def click_cash_select(self):
        self.find_element(bpl.accounts_sort).click()
        self.find_element(bpl.field_select).click()
        self.find_element(bpl.cash_select).click()

    def click_card_select(self):
        self.find_element(bpl.accounts_sort).click()
        self.find_element(bpl.field_select).click()
        self.find_element(bpl.card_select).click()

    @staticmethod
    def calculate_same_amounts(elements, value):
        my_list, counter = [], 0
        for elem in elements:
            text_elem = elem.text
            text_value = text_elem[0] + text_elem[5::]
            if "," in text_value:
                text_value = text_value.replace(",", ".")
            if " " in text_value:
                text_value = text_value.replace(" ", "", text_value.count(" "))
            my_list.append(str(abs(float(text_value))))
            if abs(float(text_value)) == value:
                counter += 1
        return counter

    def click_sum_selection(self, value):
        self.find_element(bpl.sum_selection).click()
        self.find_element(bpl.sum_field).send_keys(value)
        self.find_element(bpl.project).click()

    def get_sorting_result(self):
        return self.find_element(bpl.sorting_result).text

    def find_dates(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        return self.find_elements(bpl.all_dates)

    def find_dates1(self):
        return self.find_elements(bpl.all_dates)

    @staticmethod
    def calculate_dates(elements, st_date, fin_date):
        str_dates = [elem.text for elem in elements]
        start_date = datetime.strptime(st_date, '%d/%m/%Y').date()
        finish_date = datetime.strptime(fin_date, '%d/%m/%Y').date()
        delta = (finish_date - start_date).days
        counter = 0
        for i in range(delta + 1):
            day = '/'.join(str(start_date + timedelta(i)).split('-')[::-1])
            if day in str_dates:
                counter_day = str_dates.count(day)
                counter += counter_day
        return counter

    def click_period_from_to(self, start_date, finish_date):
        self.find_element(bpl.date_button).click()
        dates = self.find_elements(bpl.dates_choice)
        dates[0].send_keys(start_date)
        dates[1].send_keys(finish_date)
        self.find_element(bpl.project).click()

    def click_category_choice(self):
        self.find_element(bpl.categ).click()
        self.find_element(bpl.id).click()
        self.wait.until(EC.visibility_of_element_located(bpl.deletion_icon))
        self.find_element(bpl.project).click()

    def find_categories(self):
        return self.find_elements(bpl.all_categories)

    @staticmethod
    def calculate_categories(elements, word, value):
        counter = 0
        for elem in elements:
            rgba = elem.value_of_css_property('color')
            r, g, b, a = ast.literal_eval(rgba.strip("rgba"))
            hex_value = '#%02x%02x%02x' % (r, g, b)
            if hex_value == '#6dba34' and elem.text == word and value == 'green':
                counter += 1
            elif hex_value == '#e45c70' and elem.text == word and value == 'red':
                counter += 1
        return counter

    def click_select_box(self):
        return self.find_elements(bpl.select_box)[1].click()

    def click_deletion_icon1(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.deletion_icon1).click()
        self.wait.until(EC.visibility_of_element_located(bpl.alert_deletion))

    def find_deletion_alert1(self):
        return self.find_element(bpl.alert_deletion).text

    def click_deletion_alert_submit1(self):
        self.find_element(bpl.deletion_button).click()
        self.wait.until(EC.invisibility_of_element_located(bpl.deletion_button))

    def click_edit_icon(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        self.find_element(bpl.edit_icon).click()

    def edit_amount_value(self):
        self.find_element(bpl.num).send_keys(Keys.CONTROL + "a")
        self.find_element(bpl.num).send_keys(Keys.DELETE)
        self.find_element(bpl.num).send_keys(44444444444)

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.save_button)).click()
        self.wait.until(EC.invisibility_of_element(bpl.save_button))

    def find_current_account(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        return self.find_elements(bpl.all_accounts)[1].text

    def choose_new_account(self):
        self.find_element(bpl.credit_card).click()
        self.wait.until(EC.element_to_be_clickable(bpl.cash)).click()

    def find_current_category(self):
        return self.find_elements(bpl.all_categories)[0].text

    def choose_new_category(self):
        self.find_element(bpl.categories).click()
        self.wait.until(EC.element_to_be_clickable(bpl.new_category)).click()

    def find_current_date(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        return self.find_elements(bpl.all_dates)[1].text

    def choose_new_date(self):
        self.wait.until(EC.element_to_be_clickable(bpl.current_day))
        self.find_elements(bpl.current_day)[1].click()
        self.chains.move_to_element(self.find_element(bpl.new_day)).click().perform()

    def find_description(self):
        return self.find_elements(bpl.old_description)[0].text

    def add_new_description(self, text):
        self.find_element(bpl.description).send_keys(Keys.CONTROL + "a")
        self.find_element(bpl.description).send_keys(Keys.DELETE)
        self.find_element(bpl.description).send_keys(text)

    def find_project_name(self):
        self.wait.until(EC.element_to_be_clickable(bpl.low_table_element))
        return self.find_elements(bpl.projects)[1].text

    def choose_new_project(self):
        self.wait.until(EC.element_to_be_clickable(bpl.project_field))
        self.find_element(bpl.project_field).click()
        self.wait.until(EC.visibility_of_element_located(bpl.project_field1))
        self.chains.move_to_element(self.find_element(bpl.project_field1)).click().perform()

    def click_settings_icon(self):
        self.find_element(bpl.settings_icon).click()
        self.wait.until(EC.visibility_of_element_located(bpl.small_page))

    def click_participants_tab(self):
        self.find_element(bpl.participants_tab).click()

    def fill_email_field(self, email):
        self.find_element(bpl.email_field).send_keys(email)

    def click_invite_button(self):
        self.wait.until(EC.element_to_be_clickable(bpl.invite_button)).click()

    def select_rights(self):
        self.select(bpl.select_rights, 'user')

    def find_invitation(self):
        return self.find_element(bpl.invitation).text

    def click_participant_deletion(self):
        self.find_elements(bpl.del_icon)[1].click()

    def find_deletion_alert2(self):
        self.wait.until(EC.visibility_of_element_located(bpl.deletion_alert))
        return self.find_element(bpl.deletion_alert).text

    def click_deletion_button(self):
        self.find_element(bpl.deletion_button).click()
        self.wait.until(EC.invisibility_of_element_located(bpl.deletion_alert))

    def find_emails(self):
        return self.find_elements(bpl.emails)

    def get_alert_message(self):
        return self.find_element(bpl.alert_message).text

    def click_project_tab(self):
        self.wait.until(EC.visibility_of_element_located(bpl.setting_win))
        self.find_elements(bpl.project_tab)[8].click()

    def click_add_project_button(self):
        self.wait.until(EC.visibility_of_element_located(bpl.add_button))
        self.find_element(bpl.add_button).click()

    def enter_project_name(self, text):
        self.find_element(bpl.pr_field).send_keys(text)

    def click_save(self):
        self.wait.until(EC.visibility_of_element_located(bpl.save))
        self.find_element(bpl.save).click()
        self.wait.until(EC.invisibility_of_element_located(bpl.save))

    def find_project_names(self):
        return [elem.text for elem in self.find_elements(bpl.project_names)]

    def click_project_edit_icon(self, index_name):
        self.find_elements(bpl.pr_edit_icon)[index_name * 2].click()

    def click_edit_save_button(self):
        self.find_element(bpl.save).click()
        self.wait.until(EC.invisibility_of_element_located(bpl.save))

    def click_project_deletion(self, index_name):
        self.find_elements(bpl.del_icon)[index_name * 2 + 1].click()

    def find_deletion_alert3(self):
        self.wait.until(EC.visibility_of_element_located(bpl.del_alert1))
        return self.find_element(bpl.del_alert1).text

    def click_ok_deletion(self):
        self.find_element(bpl.ok_delete).click()
        self.wait.until(EC.invisibility_of_element_located(bpl.ok_delete))
