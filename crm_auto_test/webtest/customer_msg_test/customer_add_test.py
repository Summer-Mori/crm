import time
import unittest
import sys
sys.path.append("E:\\gxa\\crm_auto_test")
from HTMLTestRunner import HTMLTestRunner

from base.use_browser import UseBrowser
from util.db_operation import DbOperation
from webpage.customer_msg.customer_add import CustomerAdd
from util.excel_operation import OperationExcel


class CustomerAddTest(unittest.TestCase):
    conut=0
    def setUp(self) -> None:
        CustomerAddTest.conut+=1
        self.dp=DbOperation()
        self.exl= OperationExcel("../../config/customertest.xlsx","用例数据")
        self.exl2=OperationExcel("../../config/customertest.xlsx","sql")
        self.dp.update(self.exl2.get_cell(CustomerAddTest.conut,1))
        self.dr=CustomerAdd(self.exl.get_cell(1,1),"../../config/locator.yaml")

    def tearDown(self) -> None:
        UseBrowser.quit()

    def test_01_all_success(self):
        msg=self.dr.add_customer(name=self.exl.get_cell(CustomerAddTest.conut,2),job=self.exl.get_cell(CustomerAddTest.conut,3),sex=self.exl.get_cell(CustomerAddTest.conut,4),
                             birthday=self.exl.get_cell(CustomerAddTest.conut,5),mobile=self.exl.get_cell(CustomerAddTest.conut,6),address=self.exl.get_cell(CustomerAddTest.conut,7),
                                 addman=self.exl.get_cell(CustomerAddTest.conut,8),tel=self.exl.get_cell(CustomerAddTest.conut,9),company=self.exl.get_cell(CustomerAddTest.conut,10),
                                 source=self.exl.get_cell(CustomerAddTest.conut,11),type=self.exl.get_cell(1,12),email=self.exl.get_cell(CustomerAddTest.conut,13),
                                 condition=self.exl.get_cell(CustomerAddTest.conut,14),qq=self.exl.get_cell(CustomerAddTest.conut,15),changeman=self.exl.get_cell(CustomerAddTest.conut,16),
                                 blog=self.exl.get_cell(CustomerAddTest.conut,17),msn=self.exl.get_cell(CustomerAddTest.conut,18),remark=self.exl.get_cell(CustomerAddTest.conut,19))
        self.assertEqual(self.exl.get_cell(CustomerAddTest.conut,20),msg)
    def test_02_all_success(self):
        msg=self.dr.add_customer(name=self.exl.get_cell(CustomerAddTest.conut,2),job=self.exl.get_cell(CustomerAddTest.conut,3),sex=self.exl.get_cell(CustomerAddTest.conut,4),
                             birthday=self.exl.get_cell(CustomerAddTest.conut,5),mobile=self.exl.get_cell(CustomerAddTest.conut,6),address=self.exl.get_cell(CustomerAddTest.conut,7),
                                 addman=self.exl.get_cell(CustomerAddTest.conut,8),tel=self.exl.get_cell(CustomerAddTest.conut,9),company=self.exl.get_cell(CustomerAddTest.conut,10),
                                 source=self.exl.get_cell(CustomerAddTest.conut,11),type=self.exl.get_cell(1,12),email=self.exl.get_cell(CustomerAddTest.conut,13),
                                 condition=self.exl.get_cell(CustomerAddTest.conut,14),qq=self.exl.get_cell(CustomerAddTest.conut,15),changeman=self.exl.get_cell(CustomerAddTest.conut,16),
                                 blog=self.exl.get_cell(CustomerAddTest.conut,17),msn=self.exl.get_cell(CustomerAddTest.conut,18),remark=self.exl.get_cell(CustomerAddTest.conut,19))
        self.assertEqual(self.exl.get_cell(CustomerAddTest.conut,20),msg)
if __name__ == '__main__':
    # 创建套件
    suite = unittest.TestSuite()
    # 添加全部测试用例
    test_case = unittest.TestLoader().loadTestsFromTestCase(CustomerAddTest)
    suite.addTest(test_case)
    # 获取当前时间
    new_time = time.strftime("%Y-%m-%d", time.localtime())
    # 创建文件
    with open("../../report/CustomerAddTest_reprot_{}.html".format(new_time), "wb+") as f:
        HTMLTestRunner(stream=f,
                       verbosity=4,
                       title="auto_test",
                       description="ui_auto_test"
                       ).run(suite)