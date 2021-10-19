from selenium.webdriver import Chrome
import pytest
import sys

a = 101


def test_setup():
    # Start browser on correct URL
    path = "../Resources/chromedriver.exe"

    global driver
    driver = Chrome(executable_path=path)
    driver.get("https://thetestingworld.com/testings/")

    # Maximize browser
    driver.maximize_window()


@pytest.mark.skip("Don't run this time")
def test_title():
    title = "Login & Sign Up Forms"
    assert title == driver.title


@pytest.mark.skipif(a > 100, reason="Don't run this time")
def test_title2():
    title = "Login & Sign Up Forms"
    assert title == driver.title

# Execute tests that have condition in name of test
# pytest -k title
# Will run only 2 tests with title in name