import xlrd
import os

"""
使用xlrd读取Excel文件
"""


# 创建测试Excel文件地址
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
# print(excel_path)
# 创建工作簿对象
wb = xlrd.open_workbook(excel_path, formatting_info=True)
# 创建表格对象
sheet = wb.sheet_by_name('Sheet1')
# 获取指定列数据
col1 = sheet.col_values(1, 1)
print(col1)
cell_value = sheet.cell_value(2, 2)
print(cell_value)
# 获取表格中合并单元格位置 （起始行，结束行，起始列，结束列）
merged = sheet.merged_cells
print(merged)


def get_cell_type(row_index, col_index):
    """既能得到合并单元格也能得到普通单元格"""
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
        print(rlow,rhigh,clow,chigh)
        if (row_index >= rlow and row_index < rhigh):  # 行坐标判断
            if (col_index >= clow and col_index < chigh):  # 列坐标判断
                # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
                cell_value = sheet.cell_value(rlow, clow)
                print('合并单元格')
                break  # 不符合条件跳出循环，防止覆盖
            else:
                print('普通单元格')
                cell_value = sheet.cell_value(row_index, col_index)
        else:  #添加改行后只那一个单元格的内容5，0 会返回2个值普通单元格/合并单元格
            print('普通单元格')
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value


# 直接输入单元格的坐标。来获取单元格内容
# print(get_cell_type(3, 0))

# 利用循环输出某列的单元格内容
# for i in range(1, 9):
#     print(get_cell_type(i, 2))
