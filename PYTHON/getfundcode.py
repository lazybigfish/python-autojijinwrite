import xlrd

fundCode = []

#获取基金代码
def getfundCode():
    global fundCode

    qishilieshu = 6
    #读取表中的数据
    rbook = xlrd.open_workbook('shouyi.xls')
    rbook.sheets()
    #读取第一页的表
    rsheet = rbook.sheet_by_index(0)

    #获取第三行的数据，基金代码
    colnames = rsheet.row_values(1)
    jijinname = rsheet.row_values(0)
    c = rsheet.col_values(qishilieshu)
    c = [i for i in c if i != '']
    d = len(c) + 1
    #筛选出代码正确值
    fundCode = [i for i in colnames if i != '']
    jijinnames = [i for i in jijinname if i != '']
    y = len(fundCode)

    print(fundCode)

    return fundCode,d,y,jijinnames