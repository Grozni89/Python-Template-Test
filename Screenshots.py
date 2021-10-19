from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import TakeScreenshot

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

# Use screenshot
TakeScreenshot.take_page_screenshot(driver, "test")

driver.close()