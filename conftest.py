# conftest.py
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)
    options.set_capability("appPackage", "com.google.android.dialer")
    options.set_capability("appActivity", "com.google.android.dialer.extensions.GoogleDialtactsActivity")

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
