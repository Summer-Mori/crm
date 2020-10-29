import re
import time

from selenium import webdriver

from base.brower_operation import BrowserOperation
from base.use_browser import UseBrowser
from util.auto_def import AutoDef
from util.auto_log import AutoLog
from util.yaml_operation import YamlOperation


class Login():
    def __init__(self,url,yaml_path):
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url(url)
        self.locator=YamlOperation(yaml_path)


    def login(self,**kwargs):
        self.bo.send_keys_xpath(self.locator.get_locatoer("LoginPage","username"),kwargs.get("username",''))
        self.bo.send_keys_xpath(self.locator.get_locatoer("LoginPage", "password"),kwargs.get("password",''))
        self.bo.click_xpath(self.locator.get_locatoer("LoginPage", "submit"))

    def login_success_msg(self):
        msg = self.bo.get_title_xpath()
        msg = re.search(".+", msg).group()
        return msg

    def login_failed_msg(self):
        msg = self.bo.alert_info()
        msg = re.search(".+", msg).group()
        return msg

