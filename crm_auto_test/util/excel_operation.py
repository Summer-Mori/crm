import xlrd

#封装
class OperationExcel():
    def __init__(self,path,sheet_name):
        # 获取exl工作簿和对象
        self.wordbook = xlrd.open_workbook(path)
        self.sheet=self.wordbook.sheet_by_name(sheet_name)

    def get_nrow(self):
        return self.sheet.nrows
    def get_nocl(self):
        return self.sheet.ncols

    #都是从0开始
    def get_cell(self,row,col):
        return self.sheet.cell_value(row,col)

if __name__ == '__main__':
    exl=OperationExcel("../config/customertest.xlsx","用例数据")
    print(exl.get_cell(1,1))