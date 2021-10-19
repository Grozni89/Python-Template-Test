from selenium.webdriver import Chrome
import logging

# Start browser on correct URL
path = "Resources\\chromedriver.exe"
driver = Chrome(executable_path=path)


# Creating logging object and setting the level
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# What logs we generate and where we store it
warn = logging.FileHandler("Logs\\Warning_logs.txt")
warn.setLevel(logging.WARNING)

info = logging.FileHandler("Logs\\Info_logs.txt")
info.setLevel(logging.INFO)

# Format for logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Use formats
warn.setFormatter(formatter)
info.setFormatter(formatter)

driver.get("https://thetestingworld.com/testings/")
log.info("[ My URL is opened ]")

# Maximize browser
driver.maximize_window()
log.info("[ Window maximized ]")


driver.close()
log.warn("[ Windows is closed ]")