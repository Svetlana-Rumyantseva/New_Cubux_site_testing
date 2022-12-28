import pytest
import registration_settings as rs
from pages.locators import locators_conftest as lc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


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


@pytest.fixture(scope='function')
def authorization(driver):
    driver.get('https://new.cubux.net/')
    if driver.current_url == 'https://new.cubux.net/login':
        # email = 'sottopassagero@rambler.ru'
        # password = 'as!123kl789!#'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.eng_lang_icon)).click()
        driver.find_element(By.CSS_SELECTOR, lc.eng_language_icon)
        driver.find_element(By.CSS_SELECTOR, lc.email).send_keys(rs.email)
        driver.find_element(By.NAME, lc.password).send_keys(rs.password)
        driver.find_element(By.CLASS_NAME, lc.log_in_button).click()

        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url),
                                        message=f"The url page after login is not changed")
        cur_language = driver.find_element(By.XPATH, lc.current_language).text
        print(cur_language)
        if cur_language != 'English':
            driver.find_element(By.CLASS_NAME, lc.language_button).click()
            ActionChains(driver).move_to_element(driver.find_elements(By.XPATH, lc.eng_language)[2]).click().perform()
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located(driver.find_elements(By.XPATH, lc.select_menu)))


@pytest.fixture(scope='function')
def transaction_for_edit(driver):
    driver.get('https://new.cubux.net/team/293036/balance')
    driver.find_element(By.CSS_SELECTOR, lc.minus_button).click()
    driver.find_element(By.CLASS_NAME, lc.number).send_keys(33333333333)
    driver.find_element(By.CLASS_NAME, lc.description).send_keys('Simple test')
    driver.find_element(By.XPATH, lc.account).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.credit_card)).click()
    driver.find_element(By.XPATH, lc.category).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.categories)).click()
    driver.find_element(By.CSS_SELECTOR, lc.ok_red_button).click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element(lc.small_page))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.low_table_element))
    yield None
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.low_table_element))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.deletion_icon)).click()
    if WebDriverWait(driver, 10).\
            until(EC.text_to_be_present_in_element(lc.del_alert, "Are you sure to delete the transaction? "
                                                                 "This action cannot be undone.")):

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.del_alert_submit)).click()
        WebDriverWait(driver, 10).until((EC.invisibility_of_element_located(lc.del_alert)))


@pytest.fixture(scope='function')
def operation_deletion(driver):
    driver.get('https://new.cubux.net/team/293036/balance')

    yield None
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.low_table_element))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.deletion_icon)).click()
    if WebDriverWait(driver, 10).\
            until(EC.text_to_be_present_in_element(lc.del_alert, "Are you sure to delete the transaction? "
                                                                 "This action cannot be undone.")):

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lc.del_alert_submit)).click()
        WebDriverWait(driver, 10).until((EC.invisibility_of_element_located(lc.del_alert)))
