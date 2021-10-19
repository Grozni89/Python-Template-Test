from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)

# This is page load timeout, default value is 30 sec
driver.set_page_load_timeout(45)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Set implicitly this will be executed for all find elements
# driver.implicitly_wait(5)

# Enter Data to the textbox
driver.find_element_by_name("fld_username").send_keys("Igor")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("mars@lol.com")
driver.find_element_by_name("fld_password").send_keys("Test123")
driver.find_element_by_name("fld_cpassword").send_keys("Test123")

driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("Igor")

# Click on radio button
driver.find_element_by_xpath("//input[@value='home']").click()
driver.find_element_by_xpath("//input[@value='office']").click()
driver.find_element_by_xpath("//input[@value='home']").click()

# Click on Checkbox
driver.find_element_by_name("terms").click()

# Work on button
driver.find_element_by_xpath("//input[@type='submit']").click()

# Click on Link
driver.find_element_by_link_text("Read Detail").click()

# Close Dialog
driver.find_element_by_partial_link_text("X").click()

# Work on dropdown
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_index(1)
obj.select_by_value("2")
obj.select_by_visible_text("Male")


# For explicit timeout
wait = WebDriverWait(driver, 5)
wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'), "India"))
objCountry = Select(driver.find_element_by_id("countryId"))
objCountry.select_by_visible_text("India")


wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
objState = Select(driver.find_element_by_id("stateId"))
objState.select_by_visible_text("Delhi")

# This is hardcoded timeout
time.sleep(5)

driver.close()