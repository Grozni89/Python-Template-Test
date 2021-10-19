from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Fetching Title
print("Title of page is: " + driver.title)

# Fetching URL
print("Page URL is: " + driver.current_url)

# Fetching Complete Page HTML
#print(driver.page_source)

# Fetching Element text
print("Text on Link is: " + driver.find_element_by_class_name("displayPopup").text)

# Fetching attribute value of Element
print("Attribute value of element: " + driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))

# Work on Dropdown
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

# Fetch Selected option
print(obj.first_selected_option.text)

# Fetching all options
print("*******************")
for op in obj.options:
    print(op.text)

