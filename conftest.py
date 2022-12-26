import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import registration_settings as rs

import os

deletion_icon = (By.XPATH, '//button[@class="Button_link__5qRQJ btn-icon _size2" and @title="Удалить"]')
del_alert = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[1]')
del_alert_submit = (By.XPATH, '//button[text()="OK"]')

credit_card = (By.CSS_SELECTOR, 'span[class="hex-icon-symbol"]')
categories = (By.XPATH, '//div[text()="Путешествия"]')
ok_red_button = (By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]')
low_table_element = (By.CSS_SELECTOR, 'a[href="/team/293036/expense/details/b345064b-1102-4a18-91c8-9a5b28579bf3"]')
small_page = (By.XPATH, '//button[text()="OK"]')
description = (By.XPATH, '//textarea[class="_txt-size4 scrollbar"]')


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    options.add_argument(f"user-data-dir={os.path.join(os.path.dirname(__file__), 'authorization')}")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    # options = Options()
    # options.add_argument(f"user-data-dir={os.path.join(os.path.dirname(__file__), 'authorization')}")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # yield driver
    # driver.quit()


@pytest.fixture(scope='function')
def authorization(driver):
    driver.get('https://new.cubux.net/')
    if driver.current_url == 'https://new.cubux.net/login':
        driver.find_element(By.CSS_SELECTOR, 'a[href = "/login?switch-language=en"]').click()
        driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys(rs.email)
        driver.find_element(By.NAME, 'LoginForm[password]').send_keys(rs.password)
        driver.find_element(By.CLASS_NAME, 'button-loading-content').click()
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url),
                                        message=f"The url page after login is changed")
        cur_language = driver.find_element(By.XPATH, '//span[@class="LanguageSelect_nameCurrent__uU0qT"]').text
        print(cur_language)
        if cur_language != 'Русский':
            driver.find_element(By.CLASS_NAME, "Button_button__QS2NC").click()
            ActionChains(driver).\
                move_to_element(driver.find_elements(By.XPATH, '//div[@class="LanguageSelect_item__eB6gw"]')[3]).\
                click().perform()
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located(driver.find_elements(By.XPATH,
                                                                        '//div[@class="LanguageSelect_popup__Sw11j"]')))


@pytest.fixture(scope='function')
def operation_for_edit(driver):
    driver.get('https://new.cubux.net/team/293036/balance')
    driver.find_element(By.CSS_SELECTOR, 'button[class="Button_link__5qRQJ icon _size1 color-expense _space"]').click()
    driver.find_element(By.CLASS_NAME, "currency").send_keys(33333333333)
    driver.find_element(By.CLASS_NAME, "_txt-size4").send_keys('Простой тест')
    driver.find_element(By.XPATH, '//div[text()="Выберите счёт"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(credit_card)).click()
    driver.find_element(By.XPATH, '//div[text()="Выберите категорию"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(categories)).click()
    driver.find_element(By.CSS_SELECTOR, 'button[class="Button_button__QS2NC btn _inp-size4 color-expense"]').click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element(small_page))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(low_table_element))
    yield None
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(low_table_element))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(deletion_icon)).click()
    if WebDriverWait(driver, 10).\
            until(EC.text_to_be_present_in_element(del_alert, "Вы уверены, что хотите удалить транзакцию? "
                                                              "Операцию нельзя будет отменить.")):

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(del_alert_submit)).click()
        WebDriverWait(driver, 10).until((EC.invisibility_of_element_located(del_alert)))


@pytest.fixture(scope='function')
def operation_deletion(driver):
    driver.get('https://new.cubux.net/team/293036/balance')
    yield None
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(low_table_element))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(deletion_icon)).click()
    if WebDriverWait(driver, 10).\
            until(EC.text_to_be_present_in_element(del_alert, "Вы уверены, что хотите удалить транзакцию? "
                                                              "Операцию нельзя будет отменить.")):

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(del_alert_submit)).click()
        WebDriverWait(driver, 10).until((EC.invisibility_of_element_located(del_alert)))
