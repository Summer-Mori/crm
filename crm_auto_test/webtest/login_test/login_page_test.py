import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from util.auto_log import AutoLog
from webpage.loginpage.login_page import Login
from util.excel_operation import OperationExcel
import sys
import os
sys.path.append(os.getcwd()+"\\..\\..")
from HTMLTestRunner import HTMLTestRunner

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exl=OperationExcel("../../config/logindata.xlsx","用例参数")
        self.login=Login(self.exl.get_cell(1,1), "../../config/locator.yaml")

    def tearDown(self) -> None:
        self.login.ub.quit()
        AutoLog.set_messge("crm quite" ,"info")

    def test_01_success(self):
        self.login.login(username=self.exl.get_cell(1,2),password=self.exl.get_cell(1,3))

        self.assertEqual(self.exl.get_cell(1,4),self.login.login_success_msg())
        AutoLog.set_messge("case01 complete","info")

    def test_02_password_error(self):
        self.login.login(username=self.exl.get_cell(2,2),password=self.exl.get_cell(2,3))

        self.assertEqual(self.exl.get_cell(2,4),self.login.login_failed_msg())
        AutoLog.set_messge("case02 complete","info")

    def test_03_useranme_null(self):
        self.login.login(username=self.exl.get_cell(3, 2), password=self.exl.get_cell(3, 3))
        self.assertEqual(self.exl.get_cell(3, 4), self.login.login_failed_msg())
        AutoLog.set_messge("case03 complete","info")

    def test_04_password_null(self):
        self.login.login(username=self.exl.get_cell(4, 2), password=self.exl.get_cell(4, 3))
        self.assertEqual(self.exl.get_cell(4, 4), self.login.login_failed_msg())
        AutoLog.set_messge("case04 complete","info")

    def test_05_username_password_null(self):
        self.login.login(username=self.exl.get_cell(5, 2), password=self.exl.get_cell(5, 3))
        self.assertEqual(self.exl.get_cell(5, 4), self.login.login_failed_msg())
        AutoLog.set_messge("case05 complete","info")

if __name__ == '__main__':
    # 创建套件
    suite = unittest.TestSuite()
    # 添加全部测试用例
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTest(test_case)
    # 获取当前时间
    new_time = time.strftime("%Y-%m-%d", time.localtime())
    # 创建文件
    with open("../../report/LoginTest_reprot_{}.html".format(new_time), "wb+") as f:
        HTMLTestRunner(stream=f,
                       verbosity=1,
                       title="auto_test",
                       description="ui_auto_test"
                       ).run(suite)