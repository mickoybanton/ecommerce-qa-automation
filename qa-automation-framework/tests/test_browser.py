from utils.driver_factory import get_driver
import time

def test_browser_launch():
    driver = get_driver()
    driver.get("https://www.google.com")

    time.sleep(3)  # just so you can SEE it
    driver.quit()