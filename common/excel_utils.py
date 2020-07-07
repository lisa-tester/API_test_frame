"""
封装一个Excel操作类
导入模块顺序：内置模块 第三方模块  自定义模块

"""
import os
import xlrd

class ExcelUtils():

    def __init__(self, excel_path, sheet_name="Sheet1"):  # 也可以封装sheet_id:索引
        """构造/初始化函数"""
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # 小技巧：支持直接在构造函数之间调用方法

    def get_sheet(self):
        """获取excle中的表单"""
        # wb = xlrd.open_workbook(self.excel_path, formatting_info=True)  # formatting_info=True来避免获取合并单元格位置为空
        wb = xlrd.open_workbook(self.excel_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        """获取所有行"""
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        """获取所有列"""
        col_count = self.sheet.ncols
        return col_count

    def __get_cell_value(self, row_index, col_index):  # 私有方法
        """获取单元格值"""
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):
        """获取表单中所有的合并单元格位置信息:返回列表"""
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        """既能得到合并单元格也能得到普通单元格"""
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():  # 遍历表格中所有合并单元格位置信息
            # print(rlow,rhigh,clow,chigh)
            if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
                if (col_index >= clow and col_index < chigh):  # 列坐标判断
                    # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
                    cell_value = self.__get_cell_value(rlow, clow)
                    # print('合并单元格')
                    break  # 不符合条件跳出循环，防止覆盖
                else:
                    # print('普通单元格')
                    cell_value = self.__get_cell_value(row_index, col_index)
            # else:  #添加改行后只那一个单元格的内容5，0 会返回2个值普通单元格/合并单元格
            #     print('普通单元格')
            #     cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_date(self):
        """以列表包字典形式返回表单数据"""
        all_data_list = []
        first_row = self.sheet.row(0)  # 获取首行数据
        # print(first_row[1].value)
        for row in range(1, self.get_row_count()):  # 行循环
            row_dict = {}
            for col in range(1, self.get_col_count()):  # 列循环
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)  # 将单元格值赋值给每行字典键值对值
            all_data_list.append(row_dict)
        return all_data_list


if __name__ == "__main__":
    file_path = os.path.dirname(__file__)
    excel_path = os.path.join(file_path, '..', 'test_data/test_data.xlsx')
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    # print(excelUtils.get_merged_cell_value(3, 0))
    print(excelUtils.get_sheet_date())
