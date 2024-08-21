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

from androidTest.test import login_in_sys, enter_otp_via_keyboard, click_by_coordinates

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

def test(device):
    login_in_sys()
