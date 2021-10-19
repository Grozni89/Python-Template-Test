from PageObjects import RegistrationPagePO
from Base import InitiateDriver
from PageObjects import HomeTestPO
import random
import pytest


@pytest.fixture(scope="module")
def setup():
    # Start browser on correct URL
    global driver
    global global_nav

    driver = InitiateDriver.start_browser()
    global_nav = HomeTestPO.GlobalNavClass(driver)

    # Close browser
    yield
    InitiateDriver.close_browser()


def test_home_page(setup):
    driver.get("https://thetestingworld.com")

    title = "Testing World Experienced in making experts"
    assert title == driver.title

    url = "https://thetestingworld.com/"
    assert url == driver.current_url


def test_move_to_home(setup):
    global_nav.move_to_global_nav_item("Home")


def test_move_to_about_us(setup):
    global_nav.move_to_global_nav_item("ABOUT US")


def test_move_to_training(setup):
    global_nav.move_to_global_nav_item("TRAINING")


def test_move_to_videos(setup):
    global_nav.move_to_global_nav_item("VIDEOS")


def test_move_to_tutorial(setup):
    global_nav.move_to_global_nav_item("TUTORIAL")


def test_move_to_testing_quiz(setup):
    global_nav.move_to_global_nav_item("TESTING QUIZ")


def test_move_to_certifications(setup):
    global_nav.move_to_global_nav_item("CERTIFICATIONS")


def test_open_page_with_free_videos(setup):
    global_nav.move_to_global_nav_item("VIDEOS")
    global_nav.click_in_video("Free Videos")

    title = "Free Videos"
    assert title == driver.title


@pytest.mark.flaky(reruns=5)
def test_open_page_with_free_videos_reruns(setup):
    driver.get("https://thetestingworld.com")
    num = random.randint(0, 2)
    global_nav.move_to_global_nav_item("VIDEOS")

    if num == 2:
        global_nav.click_in_video("Free Videos")
    else:
        global_nav.click_in_video("Free Videosss")

