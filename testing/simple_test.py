from PageObjects import RegistrationPagePO
from Base import InitiateDriver
import pytest


@pytest.fixture(scope="module")
def setup():
    # Start browser on correct URL
    global driver
    global register

    driver = InitiateDriver.start_browser()
    register = RegistrationPagePO.RegistrationClass(driver)

    # Close browser
    yield
    InitiateDriver.close_browser()


def test_page_data(setup):
    title = "Login & Sign Up Forms"
    assert title == driver.title

    url = "https://thetestingworld.com/testings/"
    assert url == driver.current_url


def test_verify_registration(setup):
    # Enter Data to the textbox
    # register = RegistrationPagePO.RegistrationClass(driver)
    register.enter_username("Igor")
    register.enter_email("test@test")
    register.enter_password("test123!@#")
    register.enter_password_again("test123!@#")


def test_radio_button(setup):
    # Click on radio button
    # register = RegistrationPagePO.RegistrationClass(driver)
    register.select_address_type('home')
    register.select_address_type('office')
    register.select_address_type('home')


def test_select_checkbox(setup):
    # Click on Checkbox
    register.select_terms_conditions()


def test_read_detail(setup):
    # Click on Link
    register.click_on_read_detail()

    # Close Dialog
    register.close_read_detail_dialog()


def test_use_sex_dropdown(setup):
    # Work on dropdown
    register.select_gender("Male")
    register.select_gender_index(1)
    register.select_gender_value("2")
    register.select_gender("Male")


def test_select_country_state_city(setup):
    register.pick_country("India")
    register.pick_state("Delhi")
    register.pick_city("Delhi")