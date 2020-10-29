import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from util.auto_log import AutoLog


class BrowserOperation:

    def __init__(self,driver):

        self.driver = driver
        #self.driver = webdriver.Chrome()

    def open_url(self,url):
        try:
            self.driver.get(url)
            AutoLog.set_messge("url:{} 打开！".format(url), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def swich_frame(self, name):
        try:
            time.sleep(1)
            self.driver.switch_to.frame(name)
            AutoLog.set_messge("frame:{} 切换成功！".format(name), "info")
            time.sleep(1)
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def get_title_xpath(self):
        try:
            time.sleep(1)
            title = self.driver.title
            AutoLog.set_messge("title:{}".format(title), "info")
            return title
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def swich_frame_default(self):
        try:
            time.sleep(1)
            self.driver.switch_to.default_content()
            AutoLog.set_messge("frame切换到default成功！", "info")
            time.sleep(1)
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def send_keys_xpath(self, xpath, value):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(value)
            AutoLog.set_messge("xpth:{} 添加:{} 成功".format(xpath, value), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def send_keys_id_js(self, name, value):
        try:
            js = "document.getElementById('{}').value='{}'".format(name, value)
            self.driver.execute_script(js)
            AutoLog.set_messge("send_js:{} 添加:{} 成功".format(name, value), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def click_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            AutoLog.set_messge("xpth:{} 点击成功".format(xpath), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def select_xpath_visible_text(self, xpath, text):
        try:
            Select(self.driver.find_element_by_xpath(xpath)).select_by_visible_text(text)
            AutoLog.set_messge("select_xpth:{} text:{} 选择成功".format(xpath, text), "info")
        except Exception as e:
            AutoLog.set_messge(e, "error")

    def alert_info(self):
        try:
            text = self.driver.switch_to.alert.text
            AutoLog.set_messge("Alert:{}".format(text), "info")
            return text
        except Exception as e:
            AutoLog.set_messge(e, "error")

