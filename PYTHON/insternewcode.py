import xlrd
from xlutils.copy import copy


def insternewcode(x):
    global fundCode

    qishilieshu = 6
    # 读取表中的数据
    rbook = xlrd.open_workbook('shouyi.xls')
    rbook.sheets()
    print("读取表成功")
    # 读取第一页的表
    rsheet = rbook.sheet_by_index(0)

    # 获取第三行的数据，基金代码
    colnames = rsheet.row_values(1)
    # 筛选出代码正确值
    fundCode = [i for i in colnames if i != '']
    #获取当前基金个数，用于确定新基金插入的列
    s = len(fundCode)
    print("获取列成功")

    #获取基金当前占用列，用于确认插入的行
    c = rsheet.col_values(qishilieshu)
    c = [i for i in c if i != '']
    d = len(c)
    d = d -1
    print("获取行成功")
    nwb = copy(rbook)
    print("复制表格")
    nwb_sheet = nwb.get_sheet(0)
    nwb_sheet.write(0, (qishilieshu + (s * 6)), x[0])
    nwb_sheet.write(1, (qishilieshu + (s * 6)), x[1])
    nwb_sheet.write(d, (qishilieshu + (s * 6)), x[2])
    nwb_sheet.write(d, (qishilieshu + (s * 6) + 1), x[3])
    nwb_sheet.write(d, (qishilieshu + (s * 6) + 5), x[4])


    print("新的基金数据写入成功")
    nwb.save('shouyi.xls')
