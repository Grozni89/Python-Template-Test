from selenium.webdriver import Chrome
import pytest
import sys


@pytest.mark.Smoke
def test_setup():
    # Start browser on correct URL
    path = "../Resources/chromedriver.exe"

    global driver
    driver = Chrome(executable_path=path)
    driver.get("https://thetestingworld.com/testings/")

    # Maximize browser
    driver.maximize_window()


@pytest.mark.Sanity
def test_title():
    title = "Login & Sign Up Forms"
    assert title == driver.title


@pytest.mark.Smoke
def test_title2():
    title = "Login & Sign Up Forms"
    assert title == driver.title

# Execute Smoke tests
# pytest -m Smoke // pytest -m Smoke -v

# Execute all but Sanity tests
# pytest -m "not Sanity" -v