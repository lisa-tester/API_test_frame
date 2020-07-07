import xlrd
import os
from common.excel_utils import ExcelUtils
"""
使用xlrd读取Excel文件
获取指定格式数据：将每一行数据以字典形式打印，表格总数据以列表形式打印
"""


# 创建测试Excel文件地址
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')

excelUtils = ExcelUtils(excel_path, 'Sheet1')


# **********************普通方法获取表格数据
# print(excelUtils.get_row_count())
# sheet_list = []
# for row in range(1, excelUtils.get_row_count()):  # 表头不算在内
#     row_dict = {}  # 创建空字典 来存放没行数据
#     row_dict['事件'] = excelUtils.get_merged_cell_value(row, 0)
#     row_dict['步骤序号'] = excelUtils.get_merged_cell_value(row, 1)
#     row_dict['步骤操作'] = excelUtils.get_merged_cell_value(row, 2)
#     row_dict['完成情况'] = excelUtils.get_merged_cell_value(row, 3)
#     sheet_list.append(row_dict)
#
# # print(sheet_list)
# # 利用循环输出某列的单元格内容
# for row in sheet_list:
#     print(row)


# **********************改造方法：使用遍历方式获取(字典 列表)
all_data_list = []
first_row = excelUtils.sheet.row(0)
# print(first_row[1].value)
for row in range(1, excelUtils.get_row_count()):  # 行循环
    row_dict = {}
    for col in range(1, excelUtils.get_col_count()):  # 列循环
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row, col)  # 将单元格值赋值给每行字典键值对值
    all_data_list.append(row_dict)

for row in all_data_list:
    print(row)










