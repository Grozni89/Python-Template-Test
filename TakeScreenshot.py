
def take_page_screenshot(driver, name):

    screenshotsPath = "Screenshots\\"
    driver.get_screenshot_as_file(screenshotsPath + name + ".png")