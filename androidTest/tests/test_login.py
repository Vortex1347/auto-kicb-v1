import pytest
from androidTest.pages.login_page import LoginPage
from androidTest.pages.otp_page import OTPPage
# from androidTest.pages.home_page import HomePage
from androidTest.users import get_user

@pytest.fixture()
def driver(appium_driver):
    return appium_driver

def test_login(driver):

    user = get_user('ataiyr')

    login_page = LoginPage(driver)
    otp_page = OTPPage()
    home_page = HomePage(driver)

    login_page.enter_username(user.username)
    login_page.enter
