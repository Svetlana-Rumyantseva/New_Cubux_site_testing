from selenium.webdriver.common.by import By

eng_language_icon = 'a[href = "/login?switch-language=en"]'
eng_lang_icon = (By.CSS_SELECTOR, 'a[href = "/login?switch-language=en"]')
email = 'input[type="email"]'
password = 'LoginForm[password]'
log_in_button = 'button-loading-content'
current_language = '//span[@class="LanguageSelect_nameCurrent__uU0qT"]'
language_button = "Button_button__QS2NC"
eng_language = '//div[@class="LanguageSelect_item__eB6gw"]'
select_menu = '//div[@class="LanguageSelect_popup__Sw11j"]'

minus_button = 'button[class="Button_link__5qRQJ icon _size1 color-expense _space"]'
number = 'currency'
account = '//div[text()="Select account"]'
category = '//div[text()="Select category"]'
description = "_txt-size4"
credit_card = (By.CSS_SELECTOR, 'span[class="hex-icon-symbol"]')
categories = (By.XPATH, '//div[text()="Travels"]')
ok_red_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]')
low_table_element = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/b345064b-1102-4a18-91c8-9a5b28579bf3"]')
small_page = (By.XPATH, '//button[text()="OK"]')
deletion_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size2" and @title="Delete"]')
del_alert = (By.XPATH, '//div[@class="rc-dialog-body"]')
del_alert_submit = (By.XPATH, '//button[text()="OK"]')
