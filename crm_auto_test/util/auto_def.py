import time
from selenium.webdriver.support.select import Select

from util.auto_log import AutoLog


class AutoDef():
    def __init__(self,dr):
        self.dr=dr
        self.log=AutoLog()

    def swich_frame(self, name):
        try:
            time.sleep(1)
            self.dr.switch_to.frame(name)
            self.log.set_messge("frame:{} 切换成功！".format(name), "info")
            time.sleep(1)
        except Exception as e:
            self.log.set_messge(e, "error")
    def get_title_xpath(self):
        try:
            time.sleep(1)
            title=self.dr.title
            self.log.set_messge("title:{}".format(title), "info")
            return title
        except Exception as e:
            self.log.set_messge(e, "error")
    def swich_frame_default(self):
        try:
            time.sleep(1)
            self.dr.switch_to.default_content()
            self.log.set_messge("frame切换到default成功！", "info")
            time.sleep(1)
        except Exception as e:
            self.log.set_messge(e, "error")

    def send_keys_xpath(self, xpath, value):
        try:
            self.dr.find_element_by_xpath(xpath).send_keys(value)
            self.log.set_messge("xpth:{} 添加:{} 成功".format(xpath, value), "info")
        except Exception as e:
            self.log.set_messge(e, "error")

    def send_keys_id_js(self, name, value):
        try:
            js = "document.getElementById('{}').value='{}'".format(name, value)
            self.dr.execute_script(js)
            self.log.set_messge("send_js:{} 添加:{} 成功".format(name, value), "info")
        except Exception as e:
            self.log.set_messge(e, "error")

    def click_xpath(self, xpath):
        try:
            self.dr.find_element_by_xpath(xpath).click()
            self.log.set_messge("xpth:{} 点击成功".format(xpath), "info")
        except Exception as e:
            self.log.set_messge(e, "error")



    def select_xpath_visible_text(self, xpath, text):
        try:
            Select(self.dr.find_element_by_xpath(xpath)).select_by_visible_text(text)
            self.log.set_messge("select_xpth:{} text:{} 选择成功".format(xpath, text), "info")
        except Exception as e:
            self.log.set_messge(e, "error")

    def alert_info(self):
        try:
            text = self.dr.switch_to.alert.text
            self.log.set_messge("Alert:{}".format(text), "info")
            return text
        except Exception as e:
            self.log.set_messge(e, "error")