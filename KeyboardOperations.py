from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://thetestingworld.com/testings/")

# Maximize browser
driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("Igor")

# Execute only one key
act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()

# Execute combination of keys
# For new set of actions I need a new object
act2 = ActionChains(driver)
driver.find_element_by_name("fld_username").send_keys("Igor")
act2.key_down(Keys.CONTROL).send_keys("a").perform()

act3 = ActionChains(driver)
act3.key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.DELETE).perform()

time.sleep(10)
