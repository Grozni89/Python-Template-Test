from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("https://www.naukri.com")

# Maximize browser
driver.maximize_window()

# pop-up windows
all_windows = driver.window_handles
print(all_windows)

mainWin = ""

for win in all_windows:
    driver.switch_to.window(win)
    print(driver.current_url)

    if driver.current_url == "https://www.naukri.com":
        mainWin = win
        print("Main window")
    else:
        driver.close()

driver.switch_to.window(mainWin)

# Handling tabs
driver.get("https://thetestingworld.com/testings/")
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Delete')]").click()

allTabs = driver.window_handles

for tab in allTabs:
    driver.switch_to.window(tab)
    print(driver.current_url)

    if driver.title == "something something something":
        driver.find_element_by_xpath("//button[text()='Start Download']").click()
