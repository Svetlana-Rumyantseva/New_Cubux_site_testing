import ast
from datetime import timedelta, datetime
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

incomes_button = (By.XPATH, '//button[@class="btn-filter color-income"]')
expenses_button = (By.XPATH, '//button[@class="btn-filter color-expense"]')
transfers_button = (By.XPATH, '//button[@class="btn-filter color-calendar"]')
loans_button = (By.XPATH, '//button[@class="btn-filter color-debt"]')
all_accounts = (By.XPATH, '//td[@class="BalancePage-table_colAccount__7aXtO"]')
accounts_sort = (By.XPATH, '//button[text()="Счёт"]')
field_select = (By.XPATH,
                '//*[@id="popup-container_1"]/main/div[3]/table/tbody/tr[1]/td[5]/div/div/div/div[2]/select/option[1]')
cash_select = (By.XPATH, '//option[@value="930727"]')
card_select = (By.XPATH, '//option[@value="930726"]')
low_table_element1 = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/58874433-a176-4d92-b677-d219d49cf9b0"]')
sum_selection = (By.XPATH, '//button[text()="Сумма"]')
sum_field = (By.XPATH, '/html/body/div[1]/div/main/div[3]/table/tbody/tr[1]/td[3]/div/div/div/div[2]/form/input')
sorting_result = (By.XPATH, '//td[text()="Нет транзакций"]')

sum_filter = (By.CLASS_NAME, 'FilterSummary_badge__emkSO')
all_dates = (By.XPATH, '//td[@class="BalancePage-table_colDate__jtH+P"]')
date_button = (By.XPATH, '//button[text()="Дата"]')
dates_choice = (By.XPATH, '//input[@class="_inp-size4 input-icon icon-calendar"]')
project = (By.XPATH, '//button[text()="Проект"]')

categ = (By.XPATH, '//span[text()="— Выберите категорию —"]')
id = (By.XPATH, '//div[text()="Зарплата"]')

result = (By.XPATH, '//div[@href="/team/293036/income/details/3e06b49b-9dad-42a0-9588-d2cc930e66f1"]')
all_categories = (By.XPATH, '//div[@class="category-path"]')


minus_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-expense _space"]')
account = (By.XPATH, '//div[text()="Выберите счёт"]')
credit_card = (By.CSS_SELECTOR, 'span[class="hex-icon-symbol"]')
category = (By.XPATH, '//div[text()="Выберите категорию"]')
categories = (By.XPATH, '//div[text()="Путешествия"]')
today = (By.CLASS_NAME, "react-datepicker__today-button")
number = (By.CLASS_NAME, "currency")
description = (By.CLASS_NAME, "_txt-size4")
ok_red_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]')
alert = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]')
alert_submit = (By.CLASS_NAME, "ConfirmDialog_button__vzjDJ")

plus_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-income _extra-space"]')
cash = (By.XPATH, '//div[text()="Наличные"]')
categories1 = (By.XPATH, '//div[text()="Зарплата"]')
ok_green_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-income"]')
amount_value = (By.CLASS_NAME, 'list-value')

deletion_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size2" and @title="Удалить"]')
del_alert = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[1]')
del_alert_submit = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')

small_page = (By.XPATH, '//button[text()="OK"]')
low_table_element = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/b345064b-1102-4a18-91c8-9a5b28579bf3"]')

copy_icon = (By.CSS_SELECTOR, 'button[title="Создать копию"]')
edit_icon = (By.CSS_SELECTOR, 'button[title="Редактировать"]')
save_button = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-expense"]')
num = (By.XPATH, '//input[@placeholder="0" and @class="currency "]')
ok_alert_edit = (By.XPATH, '//button[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')

new_category = (By.XPATH, '//div[text()="Авто"]')
current_day = (By.XPATH, '//div[@class="hex-icon"]')
new_day = (By.XPATH, '//div[text()="20"]')
old_description = (By.CSS_SELECTOR, 'div[class="sub-line1"]')

projects = (By.CSS_SELECTOR, 'td[class="BalancePage-table_colProject__zrg4I"]')
project_field1 = (By.XPATH, '//div[@class="select-search__select"]')
project_field = (By.XPATH, '//div[@class="select-search__value"]')

select_box = (By.XPATH, '//input[@type="checkbox"]')
deletion_icon1 = (By.XPATH, '//button[@class="Button_button__QS2NC btn color-danger"]')
alert_deletion = (By.XPATH, '//div[@class="rc-dialog-body"]')
deletion_button = (By.XPATH, '//button[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn color-danger"]')

settings_icon = (By.CLASS_NAME, "color-settings")
users_tab = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/ul/li[5]/button/span')
email_field = (By.CSS_SELECTOR, 'input[placeholder="E-mail"]')
invite_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-settings"]')
select_rights = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/select')
invitation = (By.CSS_SELECTOR, 'i[class="color-grey"]')
user_deletion = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size4"]')
deletion_alert = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[1]')
emails = (By.CSS_SELECTOR, 'td[class="Users_colMail__+utHz"]')
alert_message = (By.CSS_SELECTOR, 'div[class="Alert_content__04oih"]')

setting_win = (By.CSS_SELECTOR, 'div[class="rc-dialog-content"]')
project_tab = (By.CSS_SELECTOR, 'span[class="Tabber_title__V9zFP"]')
add_button = (By.CSS_SELECTOR, 'button[class="btn-filter color-settings"]')
pr_field = (By.CSS_SELECTOR, 'input[name="name"]')
save = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-settings"]')
project_names = (By.CSS_SELECTOR, 'td[class="list-full"]')
pr_edit_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size4"]')
ok_delete = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')
del_alert1 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]')


class BalancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, ):
        self.driver.get(self.base_url2)

    def click_incomes_button(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(incomes_button).click()

    def click_expenses_button(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(expenses_button).click()

    @staticmethod
    def get_number_value(elements):
        my_list = []
        for i in range(len(elements)):
            elem = elements[i].text
            text = elem[:-4:]
            if "," in text:
                text = text.replace(",", ".")
            if " " in text:
                text = text.replace(" ", "", text.count(" "))
            my_list.append(float(text))
        return my_list

    def click_transfers_button(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(transfers_button).click()

    def click_loans_button(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(loans_button).click()

    def click_minus_button(self):
        self.find_element(minus_button).click()

    def fill_amount_field(self, money):
        self.find_element(number).send_keys(money)

    def choose_account(self):
        self.find_element(account).click()
        self.wait.until(EC.element_to_be_clickable(credit_card)).click()

    def choose_category(self):
        self.find_element(category).click()
        self.wait.until(EC.element_to_be_clickable(categories)).click()

    def click_ok_red_button(self):
        self.wait.until(EC.element_to_be_clickable(ok_red_button)).click()

    def find_alert1(self):
        if self.wait.until(EC.text_to_be_present_in_element(alert, "Укажите сумму"),
                           'The message <Укажите сумму> is not received'):
            return self.find_element(alert).text

    def click_alert_submit(self):
        self.wait.until(EC.element_to_be_clickable(alert_submit)).click()

    def click_plus_button(self):
        self.find_element(plus_button).click()

    def click_ok_green_button(self):
        self.wait.until(EC.element_to_be_clickable(ok_green_button)).click()

    def choose_account_(self):
        self.find_element(account).click()
        self.wait.until(EC.element_to_be_clickable(cash)).click()

    def choose_category_(self):
        self.find_element(category).click()
        self.wait.until(EC.element_to_be_clickable(categories1)).click()

    def find_alert2(self):
        if self.wait.until(EC.text_to_be_present_in_element(alert, "Выберите счёт")):
            return self.find_element(alert).text

    def find_alert3(self):
        if self.wait.until(EC.text_to_be_present_in_element(alert, "Выберите категорию")):
            return self.find_element(alert).text

    def click_green_ok(self):
        self.wait.until(EC.element_to_be_clickable(ok_green_button)).click()
        self.wait.until(EC.invisibility_of_element(ok_green_button))

    def click_red_ok(self):
        self.wait.until(EC.element_to_be_clickable(ok_red_button)).click()
        self.wait.until(EC.invisibility_of_element(ok_red_button))

    def find_amounts_values(self):
        return self.find_elements(amount_value)

    def click_deletion_icon(self):
        self.find_element(deletion_icon).click()

    def find_deletion_alert(self):
        if self.wait.until(EC.text_to_be_present_in_element(del_alert, "Вы уверены, что хотите удалить транзакцию? "
                                                                       "Операцию нельзя будет отменить.")):
            return self.find_element(del_alert).text

    def click_deletion_alert_submit(self):
        self.wait.until(EC.element_to_be_clickable(del_alert_submit)).click()
        self.wait.until((EC.invisibility_of_element_located(del_alert_submit)))

    def click_copy_icon(self):
        # self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(copy_icon).click()

    def waiting(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))

    def waiting1(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element1))

    def find_all_accounts(self):
        elements = self.find_elements(all_accounts)
        my_accounts = []
        for elem in elements:
            my_accounts.append(elem.text)
        return ' '.join(my_accounts)

    @staticmethod
    def calculate_operation(my_string, value):
        counter = my_string.count(value)
        return counter

    def click_cash_select(self):
        self.find_element(accounts_sort).click()
        self.find_element(field_select).click()
        self.find_element(cash_select).click()

    def click_card_select(self):
        self.find_element(accounts_sort).click()
        self.find_element(field_select).click()
        self.find_element(card_select).click()

    @staticmethod
    def calculate_same_amounts(elements, value):
        my_list, counter = [], 0
        for elem in elements:
            text_elem = elem.text
            text_value = text_elem[:-4:]
            if "," in text_value:
                text_value = text_value.replace(",", ".")
            if " " in text_value:
                text_value = text_value.replace(" ", "", text_value.count(" "))
            my_list.append(str(abs(float(text_value))))
            if abs(float(text_value)) == value:
                counter += 1
        return counter

    def click_sum_selection(self, value):
        self.find_element(sum_selection).click()
        self.find_element(sum_field).send_keys(value)
        self.find_element(project).click()

    def get_sorting_result(self):
        return self.find_element(sorting_result).text

    def find_dates(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        return self.find_elements(all_dates)

    def find_dates1(self):
        return self.find_elements(all_dates)

    @staticmethod
    def calculate_dates(elements, st_date, fin_date):
        str_dates = [elem.text for elem in elements]
        start_date = datetime.strptime(st_date, '%d.%m.%Y').date()
        finish_date = datetime.strptime(fin_date, '%d.%m.%Y').date()
        delta = (finish_date - start_date).days
        counter = 0
        for i in range(delta + 1):
            day = '.'.join(str(start_date + timedelta(i)).split('-')[::-1])
            if day in str_dates:
                counter_day = str_dates.count(day)
                counter += counter_day
        return counter

    def click_period_from_to(self, start_date, finish_date):
        self.find_element(date_button).click()
        dates = self.find_elements(dates_choice)
        dates[0].send_keys(start_date)
        dates[1].send_keys(finish_date)
        self.find_element(project).click()

    def click_category_choice(self):
        self.find_element(categ).click()
        self.find_element(id).click()
        self.wait.until(EC.visibility_of_element_located(deletion_icon))
        self.find_element(project).click()

    def find_categories(self):
        return self.find_elements(all_categories)

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
        return self.find_elements(select_box)[1].click()

    def click_deletion_icon1(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(deletion_icon1).click()
        self.wait.until(EC.visibility_of_element_located(alert_deletion))

    def find_deletion_alert1(self):
        return self.find_element(alert_deletion).text

    def click_deletion_alert_submit1(self):
        self.find_element(deletion_button).click()
        self.wait.until(EC.invisibility_of_element_located(deletion_button))

    def click_edit_icon(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        self.find_element(edit_icon).click()

    def edit_amount_value(self):
        self.find_element(num).send_keys(Keys.CONTROL + "a")
        self.find_element(num).send_keys(Keys.DELETE)
        self.find_element(num).send_keys(44444444444)

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(save_button)).click()
        self.wait.until(EC.invisibility_of_element(save_button))

    def find_current_account(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        return self.find_elements(all_accounts)[1].text

    def choose_new_account(self):
        self.find_element(credit_card).click()
        self.wait.until(EC.element_to_be_clickable(cash)).click()

    def find_current_category(self):
        return self.find_elements(all_categories)[0].text

    def choose_new_category(self):
        self.find_element(categories).click()
        self.wait.until(EC.element_to_be_clickable(new_category)).click()

    def find_current_date(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        return self.find_elements(all_dates)[1].text

    def choose_new_date(self):
        self.wait.until(EC.element_to_be_clickable(current_day))
        self.find_elements(current_day)[1].click()
        self.chains.move_to_element(self.find_element(new_day)).click().perform()

    def find_description(self):
        return self.find_elements(old_description)[0].text

    def add_new_description(self, text):
        self.find_element(description).send_keys(Keys.CONTROL + "a")
        self.find_element(description).send_keys(Keys.DELETE)
        self.find_element(description).send_keys(text)

    def find_project_name(self):
        self.wait.until(EC.element_to_be_clickable(low_table_element))
        return self.find_elements(projects)[1].text

    def choose_new_project(self):
        self.wait.until(EC.element_to_be_clickable(project_field))
        self.find_element(project_field).click()
        self.chains.move_to_element(self.find_element(project_field1)).click().perform()

    def click_settings_icon(self):
        self.find_element(settings_icon).click()

    def click_users_tab(self):
        self.find_element(users_tab).click()

    def fill_email_field(self, email):
        self.find_element(email_field).send_keys(email)

    def click_invite_button(self):
        self.wait.until(EC.element_to_be_clickable(invite_button)).click()

    def select_rights(self):
        self.select(select_rights, 'user')

    def find_invitation(self):
        return self.find_element(invitation).text

    def click_user_deletion(self):
        self.find_elements(user_deletion)[1].click()

    def find_deletion_alert2(self):
        self.wait.until(EC.visibility_of_element_located(deletion_alert))
        return self.find_element(deletion_alert).text

    def click_deletion_button(self):
        self.find_element(deletion_button).click()
        self.wait.until(EC.invisibility_of_element_located(deletion_alert))

    def find_emails(self):
        return self.find_elements(emails)

    def get_alert_message(self):
        return self.find_element(alert_message).text

    def click_project_tab(self):
        self.wait.until(EC.visibility_of_element_located(setting_win))
        self.find_elements(project_tab)[8].click()

    def click_add_project_button(self):
        self.find_element(add_button).click()

    def enter_project_name(self, text):
        self.find_element(pr_field).send_keys(text)

    def click_save(self):
        self.wait.until(EC.visibility_of_element_located(save))
        self.find_element(save).click()
        self.wait.until(EC.invisibility_of_element_located(save))

    def find_project_names(self):
        return [elem.text for elem in self.find_elements(project_names)]

    def click_project_edit_icon(self):
        self.find_elements(pr_edit_icon)[4].click()

    def click_edit_save_button(self):
        self.find_element(save).click()
        self.wait.until(EC.invisibility_of_element_located(save))

    def click_project_deletion(self):
        self.find_elements(user_deletion)[5].click()

    def find_deletion_alert3(self):
        self.wait.until(EC.visibility_of_element_located(del_alert1))
        return self.find_element(del_alert1).text

    def click_ok_deletion(self):
        self.find_element(ok_delete).click()
        self.wait.until(EC.invisibility_of_element_located(ok_delete))
