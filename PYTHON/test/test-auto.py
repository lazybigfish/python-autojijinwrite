import xlrd
import xlwt
from xlutils.copy import copy

x = 5
y = 7
infolist = ['3.8020', '2.9001', '1.8620', '3.0335', '3.3590', '3.6030', '2.4138']
#准备读取列表存放读取数据
dqccje = []
dqcysy = []
dqjrsy = []
dqcysyl = []
dqccse = []

#准备更新列表存放计算后的数据
gxccje = []
gxcysy = []
gxjrsy = []
gxcysyl = []
#初始列数定位置用于定位存放位置和读取位置
chushi = 1
chushi2 = 1
#初始行数定位
x = x - 1

wb = xlrd.open_workbook('shouyi1.xls')
wb.sheets()

wb_sheet = wb.sheet_by_index(0)

colnames = wb_sheet.row_values(x)
#print(colnames)

#将原表的数据读取出来供计算
for i in range(len(infolist)):
    dqccje.append(colnames[chushi])
    chushi = chushi + 1
    dqcysy.append(colnames[chushi])
    chushi = chushi + 1
    dqjrsy.append(colnames[chushi])
    chushi = chushi + 3
    dqccse.append(colnames[chushi])
    chushi = chushi +1

print("读取的持仓金额：%s" % dqccje)
print("读取的持有收益：%s" % dqcysy)
print("读取的持仓数额：%s" % dqccse)

for i in range(len(infolist)):
    #获取值转换为浮点数进行计算
    #获取昨日持仓数额
    q = float(dqccse[i])
    #读取今日获取净值
    s = float(infolist[i])
    #读取昨日持仓金额
    w = float(dqccje[i])
    #读取昨日持有收益
    e = float(dqcysy[i])

    gxccjes = q * s
    #控制结果精度为浮点两位数
    gxccjes = round(gxccjes,2)
    #将结果添加进入更新的列表
    gxccje.append(gxccjes)
    #计算今日收益
    gxjrsys = gxccjes - w
    gxjrsys = round(gxjrsys,2)
    gxjrsy.append(gxjrsys)

    #计算持有收益
    gxcysys = gxjrsys + e
    gxcysys = round(gxcysys,2)
    gxcysy.append(gxcysys)

    gxcysyls = gxcysys / (gxccjes - gxcysys)
    gxcysyls = round(gxcysyls,2)
    gxcysyl.append(gxcysyls)



print("更新的持仓金额：%s" % gxccje)
print("更新的今日收益：%s" % gxjrsy)
print("更新的持有收益：%s" % gxcysy)
print("更新的持有收益率：%s" % gxcysyl)



wb1 = xlrd.open_workbook('shouyi1.xls')
nwb = copy(wb1)
nwb_sheet = nwb.get_sheet(0)
x = x + 1


for i in range(y):
    nwb_sheet.write_merge(2, 2, chushi2, (chushi2 + 5), infolist[i])
    nwb_sheet.write(x, chushi2, gxccje[i])
    chushi2 = chushi2 + 1
    nwb_sheet.write(x, chushi2, gxcysy[i])
    chushi2 = chushi2 + 1
    nwb_sheet.write(x, chushi2, gxjrsy[i])
    chushi2 = chushi2 + 2
    nwb_sheet.write(x, chushi2, gxcysyl[i])
    chushi2 = chushi2 + 1
    nwb_sheet.write(x, chushi2, dqccse[i])
    chushi2 = chushi2 + 1

print("自动计算结束")
nwb.save('shouyi2.xls')