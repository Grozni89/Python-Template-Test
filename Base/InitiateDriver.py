from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def start_browser():
    # Start browser on correct URL
    global driver

    if((ConfigReader.readConfigData('Details', 'Browser')) == "Chrome"):
        driver = Chrome(executable_path=ConfigReader.readConfigData('Details', 'Driver_path_GC'))

    elif((ConfigReader.readConfigData('Details', 'Browser')) == "Firefox"):
        driver = Firefox(executable_path=ConfigReader.readConfigData('Details', 'Driver_path_FF'))

    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))

    # Maximize browser
    driver.maximize_window()
    return driver


def close_browser():
    # Close browser
    driver.close()