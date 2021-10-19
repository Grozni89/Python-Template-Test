from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://thetestingworld.com")

# Maximize browser
driver.maximize_window()

# Create object
act = ActionChains(driver)

# Simple Right click
act.click().perform()

# Simple left click
act2 = ActionChains(driver)
act2.context_click().perform()

# Click operation with located element
act3 = ActionChains(driver)
click_spot = driver.find_element_by_xpath("//a[text()='Login']")
act3.click(click_spot).perform()

driver.back()

# Move to location
act4 = ActionChains(driver)
act4.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()
