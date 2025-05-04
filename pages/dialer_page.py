from appium.webdriver.common.appiumby import AppiumBy

class DialerPage:
    def __init__(self, driver):
        self.driver = driver

def open_keypad(self):
    try:
        print("🟢 Mencoba klik 'Phone'")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Phone").click()
        time.sleep(2)
    except Exception as e:
        print("ℹ️ Tidak bisa klik Phone (mungkin sudah dibuka)")

    try:
        print("🟢 Mencoba klik 'key pad'")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "key pad").click()
        time.sleep(1)
    except Exception as e:
        print("❗ Tidak bisa klik key pad:", e)

    def enter_digits(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1,").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2,ABC").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3,DEF").click()

    def press_call(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "dial").click()

    def end_call(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "End call").click()

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
