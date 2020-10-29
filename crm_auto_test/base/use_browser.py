import time

from selenium import webdriver

from util.auto_log import AutoLog


class UseBrowser:
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome("../../driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        UseBrowser.driver = self.driver

    @classmethod
    def quit(cls):
        try:
            time.sleep(4)
            UseBrowser.driver.quit()
            AutoLog.set_messge("quit！", "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")


