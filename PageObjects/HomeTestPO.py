from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class GlobalNavClass:

    def __init__(self, obj):
        global driver
        driver = obj
        driver.implicitly_wait(5)

    def move_to_global_nav_item(self, name):
        act = ActionChains(driver)
        act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'" + name + "')]")).perform()
        time.sleep(1)

    def move_in_video(self, item):
        act = ActionChains(driver)
        act.move_to_element(driver.find_element_by_xpath("//a[@title='" + item + "']")).perform()
        time.sleep(1)

    def click_in_video(self, item):
        driver.find_element_by_xpath("//a[@title='" + item + "']").click()
