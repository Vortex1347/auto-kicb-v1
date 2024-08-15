import subprocess
import time
import random
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'net.kicb.ibankprod.dev',
    'appActivity': 'net.kicb.newibank.activity.MainActivity',
    'language': 'en',
    'locale': 'US',
    'platformVersion': '12'
}
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'

adb_path = r'C:\platform-tools\adb.exe'


@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app_driver
    app_driver.quit()


def generate_random_kyrgyz_mobile_number():
    mobile_prefixes = ['700', '701', '702', '703', '705', '707', '708', '709', '550', '551', '552', '553',
                       '554', '555', '556', '557', '558', '559']
    prefix = random.choice(mobile_prefixes)
    number = prefix + str(random.randint(100000, 999999))
    return number


def login_in_sys(driver, successful_numbers):
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, "net.kicb.ibankprod.dev:id/registration_tv")))
        username_field.click()

        be_client_KICB = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, "net.kicb.ibankprod.dev:id/begin_client_btn")))
        be_client_KICB.click()

        welcome_screen1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH,
                                        '//androidx.compose.ui.platform.ComposeView[@resource-id="net.kicb.ibankprod.dev:id/composeViewRemote"]/android.view.View/android.view.View/android.view.View[3]'))
        )
        welcome_screen1.click()
        welcome_screen2 = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((AppiumBy.XPATH,
                                        '//androidx.compose.ui.platform.ComposeView[@resource-id="net.kicb.ibankprod.dev:id/composeViewRemote"]/android.view.View/android.view.View/android.view.View[2]'))
        )
        welcome_screen2.click()
        welcome_screen3 = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((AppiumBy.XPATH,
                                        '//androidx.compose.ui.platform.ComposeView[@resource-id="net.kicb.ibankprod.dev:id/composeViewRemote"]/android.view.View/android.view.View/android.view.View[4]'))
        )
        welcome_screen3.click()

        welcome_screen_start = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button'))
        )
        welcome_screen_start.click()

        number = generate_random_kyrgyz_mobile_number()

        welcome_edit_text = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText')))
        welcome_edit_text.send_keys(number)

        welcome_screen_approve = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button'))
        )
        welcome_screen_approve.click()

        try:
            modal_element = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="net.kicb.ibankprod.dev:id/positive_tv"]'))
            )
            modal_element.click()
            successful_numbers.append(number)
            print(f"Номер {number} добавлен в массив успешных номеров.")
        except TimeoutException:
            driver.quit()
    except TimeoutException as e:
        print(f"TimeoutException: {e}")
    except Exception as e:
        print(f"Exception: {e}")


def test_remote(driver):
    successful_numbers = []
    login_in_sys(driver, successful_numbers)
    print(f"Успешные номера: {successful_numbers}")
