from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Enter Data to the textbox
driver.find_element_by_name("fld_username").send_keys("lol")
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

driver.close()