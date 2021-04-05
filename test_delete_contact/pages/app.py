from appium import webdriver

from test_delete_contact.pages.information_page import InformationPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["udid"] = "127.0.0.1:7555"
        # 动态页面的等待时间是10000ms，手动设置为0
        # caps["settings[waitForIdleTimeout]"] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)