import xlrd
import os
from xlutils.copy import copy

"""
使用xlrd xlutils修改Excel内容
思路：
1.先复制打开一个新的Excel
2.对新Excel中的sheet表单进行修改
3.保存修改
4.查看修改内容与实际内容是否一致
5.取列内容并进行排序
"""
# 创建测试Excel文件地址
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
# print(excel_path)
# 创建工作簿对象
wb = xlrd.open_workbook(excel_path)
# 创建表格对象
# sheet2 = wb.sheet_by_name('Sheet1')  # 使用sheet名称来获取sheet表单
sheet = wb.sheet_by_index(0)  # 使用下标/索引来获取sheet表单，下标从0开始
# 复制打开新excel
new_excel = copy(wb)
# 打开新Excel的sheet表单
new_sheet = new_excel.get_sheet(0)
# ---------------------------------修改单元格内容/某一列内容
# 修改单元格内容
# new_sheet.write(6, 2, 666)
# 修改某列单元格内容
score = [60, 90, 100, 40]
# print(score[0])
col = sheet.col_values(3, 1)
print(col)
for i in range(1, len(col)):
    new_sheet.write(i, 3, score[i])
# 保存修改内容
new_excel.save('./data/new_excel.xlsx')

# --------------------对某列内容排序
print(sorted(col, reverse=True))


