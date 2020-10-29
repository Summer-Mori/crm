import re
import time

from selenium import webdriver

from util.auto_def import AutoDef
from util.auto_log import AutoLog
from util.yaml_operation import YamlOperation
from webpage.loginpage.login_page import Login


class CustomerAdd():
    def __init__(self, url, yaml_path):
        login=Login(url, yaml_path)
        login.login(username="admin",password="123456")
        self.ub = login.ub
        self.bo = login.bo
        self.locator = login.locator


    def add_customer(self,**kwargs):
        self.bo.swich_frame("topFrame")
        self.bo.click_xpath(self.locator.get_locatoer("CustomerPage","customermsg"))
        self.bo.swich_frame_default()
        self.bo.swich_frame("mainFrame")
        self.bo.click_xpath(self.locator.get_locatoer("CustomerPage","customeradd"))

        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "name"),kwargs.get("name",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "job"), kwargs.get("job",""))
        if kwargs.get("sex","")=="女":
            self.bo.click_xpath(self.locator.get_locatoer("CustomerAddPage", "sexwoman"))
        self.bo.send_keys_id_js(self.locator.get_locatoer("CustomerAddPage", "birthday"),kwargs.get("birthday",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "mobile"), kwargs.get("mobile",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "address"), kwargs.get("address",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "addman"), kwargs.get("addman",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "tel"), kwargs.get("tel",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "company"),kwargs.get("company","") )
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "source"), kwargs.get("source",""))
        self.bo.select_xpath_visible_text(self.locator.get_locatoer("CustomerAddPage", "type"),kwargs.get("type",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "email"), kwargs.get("email",""))
        self.bo.select_xpath_visible_text(self.locator.get_locatoer("CustomerAddPage", "condition"), kwargs.get("condition",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "qq"), kwargs.get("qq",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "changeman"), kwargs.get("changeman",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "blog"),kwargs.get("blog",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "msn"), kwargs.get("msn",""))
        self.bo.send_keys_xpath(self.locator.get_locatoer("CustomerAddPage", "remark"),kwargs.get("remark",""))
        self.bo.click_xpath(self.locator.get_locatoer("CustomerAddPage", "submit"))
        return self.bo.alert_info()

