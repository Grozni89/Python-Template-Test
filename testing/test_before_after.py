from selenium.webdriver import Chrome
import pytest
import sys


# fixture is to set data before tests
# if add scope it will execute only once and not open 2 tabs
@pytest.fixture(scope="module")
def setup():
    # Start browser on correct URL
    global driver
    path = "../Resources/chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://thetestingworld.com/testings/")

    # Maximize browser
    driver.maximize_window()

    # Execute after test case
    yield
    driver.close()


def test_title(setup):
    title = "Login & Sign Up Forms"
    assert title == driver.title


def test_title2(setup):
    url = "https://thetestingworld.com/testings/"
    assert url == driver.current_url

