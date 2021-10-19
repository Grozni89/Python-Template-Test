from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj
        driver.implicitly_wait(5)

    def enter_username(self, username):
        driver.find_element_by_name("fld_username").send_keys(username)

    def enter_password(self, password):
        driver.find_element_by_name("fld_password").send_keys(password)

    def enter_password_again(self, password):
        driver.find_element_by_name("fld_cpassword").send_keys(password)

    def enter_email(self, email):
        driver.find_element_by_xpath("//input[@name='fld_email']").send_keys(email)

    # Use variable in xpath
    def select_address_type(self, address_type):
        driver.find_element_by_xpath("//input[@value='" + address_type + "']").click()

    def select_terms_conditions(self):
        driver.find_element_by_name("terms").click()

    def click_on_read_detail(self):
        driver.find_element_by_link_text("Read Detail").click()

    def close_read_detail_dialog(self):
        driver.find_element_by_partial_link_text("X").click()

    # Use select for dropdown with element name
    def select_gender(self, gender):
        obj = Select(driver.find_element_by_name("sex"))
        obj.select_by_visible_text(gender)

    def select_gender_index(self, index):
        obj = Select(driver.find_element_by_name("sex"))
        obj.select_by_index(index)

    def select_gender_value(self, value):
        obj = Select(driver.find_element_by_name("sex"))
        obj.select_by_value(value)

    def pick_country(self, country):
        objCountry = Select(driver.find_element_by_id("countryId"))
        objCountry.select_by_visible_text(country)

    def pick_state(self, state):
        objState = Select(driver.find_element_by_id("stateId"))
        objState.select_by_visible_text(state)

    def pick_city(self, city):
        wait = WebDriverWait(driver, 5)
        wait.until(ec.text_to_be_present_in_element((By.ID, 'cityId'), city))
        objState = Select(driver.find_element_by_id("cityId"))
        objState.select_by_visible_text(city)