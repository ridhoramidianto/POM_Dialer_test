import time
from pages.dialer_page import DialerPage

def test_call_sequence(driver):
    dialer = DialerPage(driver)

    time.sleep(2)
    dialer.open_keypad()
    time.sleep(1)

    dialer.enter_digits()
    time.sleep(1)

    dialer.take_screenshot("test_dialer_screen.png")

    dialer.press_call()
    time.sleep(3)

    dialer.end_call()
    time.sleep(1)

    driver.execute_script('mobile: pressKey', {"keycode": 3})
    assert True
