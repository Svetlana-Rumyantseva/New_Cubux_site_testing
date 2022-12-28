from selenium.webdriver.common.by import By

low_table_element = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/b345064b-1102-4a18-91c8-9a5b28579bf3"]')
incomes_button = (By.XPATH, '//button[@class="btn-filter color-income"]')
expenses_button = (By.XPATH, '//button[@class="btn-filter color-expense"]')
transfers_button = (By.XPATH, '//button[@class="btn-filter color-calendar"]')
loans_button = (By.XPATH, '//button[@class="btn-filter color-debt"]')

low_table_element1 = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/58874433-a176-4d92-b677-d219d49cf9b0"]')
all_accounts = (By.XPATH, '//td[@class="BalancePage-table_colAccount__7aXtO"]')
accounts_sort = (By.XPATH, '//button[text()="Account"]')
field_select = (By.XPATH, '//div[@class="Popper_popper__qeD+p popup-menu-container"]/div/div[2]/select')
cash_select = (By.XPATH, '//option[@value="930727"]')
card_select = (By.XPATH, '//option[@value="930726"]')

all_dates = (By.XPATH, '//td[@class="BalancePage-table_colDate__jtH+P"]')
date_button = (By.XPATH, '//button[text()="Date"]')
dates_choice = (By.XPATH, '//input[@class="_inp-size4 input-icon icon-calendar"]')
project = (By.XPATH, '//button[text()="Project"]')

sum_selection = (By.XPATH, '//button[text()="Amount"]')
sum_field = (By.XPATH, '//div[@class="no-margin"]/form/input')
amount_value = (By.CLASS_NAME, 'list-value')


all_categories = (By.XPATH, '//div[@class="category-path"]')
categ = (By.XPATH, '//span[text()="— Select a category —"]')

id = (By.XPATH, '//div[text()="Salary"]')
deletion_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size2" and @title="Delete"]')


edit_icon = (By.CSS_SELECTOR, 'button[title="Edit"]')
num = (By.XPATH, '//input[@placeholder="0" and @class="currency "]')
save_button = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-expense"]')
ok_alert_edit = (By.XPATH, '//button[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')

credit_card = (By.CSS_SELECTOR, 'span[class="hex-icon-symbol"]')
cash = (By.XPATH, '//div[text()="Cash"]')

minus_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-expense _space"]')
number = (By.CLASS_NAME, "currency")
account = (By.XPATH, '//div[text()="Select account"]')
category = (By.XPATH, '//div[text()="Select category"]')
ok_red_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]')
del_alert = (By.XPATH, '//div[@class="rc-dialog-body"]')
del_alert_submit = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')
alert2 = (By.XPATH, '//div[text()="Select an account"]')
alert3 = (By.XPATH, '//div[text()="Select a category"]')
alert1 = (By.XPATH, '//div[text()="Type an amount"]')


alert_submit = (By.CLASS_NAME, "ConfirmDialog_button__vzjDJ")
sorting_result = (By.XPATH, '//td[@colspan="9"]')


copy_icon = (By.CSS_SELECTOR, 'button[title="Create a copy"]')

categories1 = (By.XPATH, '//div[text()="Salary"]')
select_box = (By.XPATH, '//input[@type="checkbox"]')
deletion_icon1 = (By.XPATH, '//button[@class="Button_button__QS2NC btn color-danger"]')
alert_deletion = (By.XPATH, '//div[@class="rc-dialog-body"]')
deletion_button = (By.XPATH, '//button[@class="Button_button__QS2NC ConfirmDialog_button__vzjDJ btn color-danger"]')


plus_button = (By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-income _extra-space"]')
ok_green_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-income"]')

categories = (By.XPATH, '//div[text()="Travels"]')
new_category = (By.XPATH, '//div[text()="Car"]')

current_day = (By.XPATH, '//div[@class="hex-icon"]')
new_day = (By.XPATH, '//div[text()="20"]')

old_description = (By.CSS_SELECTOR, 'div[class="sub-line1"]')
description = (By.CLASS_NAME, "_txt-size4")

projects = (By.CSS_SELECTOR, 'td[class="BalancePage-table_colProject__zrg4I"]')
project_field1 = (By.XPATH, '//div[@class="select-search__select"]')
project_field = (By.XPATH, '//div[@class="select-search__value"]')


settings_icon = (By.CLASS_NAME, "color-settings")
participants_tab = (By.XPATH, '//span[text()="Participants"]')
email_field = (By.CSS_SELECTOR, 'input[placeholder="E-mail"]')
invite_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-settings"]')
select_rights = (By.XPATH, '//div[@class="Grid_col__NSAHt Grid_span_12__pZfWv Grid_span_up_lg_4__qvPjP"]/select')
invitation = (By.CSS_SELECTOR, 'i[class="color-grey"]')
del_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size4"]')
deletion_alert = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[1]')
emails = (By.CSS_SELECTOR, 'td[class="Users_colMail__+utHz"]')
alert_message = (By.CSS_SELECTOR, 'div[class="Alert_content__04oih"]')
small_page = (By.CSS_SELECTOR, 'div[class="rc-dialog-body"]')


setting_win = (By.CSS_SELECTOR, 'div[class="rc-dialog-content"]')
project_tab = (By.CSS_SELECTOR, 'span[class="Tabber_title__V9zFP"]')
add_button = (By.CSS_SELECTOR, 'button[class="btn-filter color-settings"]')
pr_field = (By.CSS_SELECTOR, 'input[name="name"]')
save = (By.CSS_SELECTOR, 'button[class="btn _inp-size4 color-settings"]')
project_names = (By.CSS_SELECTOR, 'td[class="list-full"]')
pr_edit_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size4"]')
ok_delete = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC ConfirmDialog_button__vzjDJ"]')
del_alert1 = (By.XPATH, '//div[@class="rc-dialog Dialog_dialog__fpfGR"]/div[2]/div')
