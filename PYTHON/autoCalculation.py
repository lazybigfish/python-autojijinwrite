import xlrd
from xlutils.copy import copy
import datetime

nowdate = datetime.datetime.now().strftime('%y-%m-%d')

#自动计算全部结果并写入Excel
def autoCalculation(infolist,y,x,fundcode,qishilieshu):
    # 准备读取列表存放读取数据
    dqccje = []
    dqcysy = []
    dqjrsy = []
    dqcysyl = []
    dqccse = []

    # 准备更新列表存放计算后的数据
    gxccje = []
    gxcysy = []
    gxjrsy = []
    gxcysyl = []

    # 初始列数定位置用于定位存放位置和读取位置
    chushi = qishilieshu
    chushi2 = qishilieshu
    # 初始行数定位
    global nowdate
    x = x - 2


    wb = xlrd.open_workbook('shouyi.xls')
    wb.sheets()

    wb_sheet = wb.sheet_by_index(0)
    #读取昨日数据
    colnames = wb_sheet.row_values(x)

    # 将原表的数据读取出来供计算
    for i in range(len(infolist)):
        dqccje.append(colnames[chushi])
        chushi = chushi + 1
        dqcysy.append(colnames[chushi])
        chushi = chushi + 1
        dqjrsy.append(colnames[chushi])
        chushi = chushi + 3
        dqccse.append(colnames[chushi])
        chushi = chushi + 1

    print("读取的持仓金额：%s" % dqccje)
    #text.insert(END, "这是读取到的昨日持仓金额：%s \n" % dqccje)
    print("读取的持有收益：%s" % dqcysy)
    #text.insert(END, "这是读取到的昨日持有收益：%s \n" % dqcysy)
    print("读取的持仓数额：%s" % dqccse)
    #text.insert(END, "这是读取到的昨日持仓数额：%s \n" % dqccse)

    for i in range(len(infolist)):
        # 获取值转换为浮点数进行计算
        # 获取昨日持仓数额
        q = float(dqccse[i])
        # 读取今日获取净值
        s = float(infolist[i])
        # 读取昨日持仓金额
        w = float(dqccje[i])
        # 读取昨日持有收益
        e = float(dqcysy[i])

        gxccjes = q * s
        # 控制结果精度为浮点两位数
        gxccjes = round(gxccjes, 2)
        # 将结果添加进入更新的列表
        gxccje.append(gxccjes)
        # 计算今日收益
        gxjrsys = gxccjes - w
        gxjrsys = round(gxjrsys, 2)
        gxjrsy.append(gxjrsys)

        # 计算持有收益
        gxcysys = gxjrsys + e
        gxcysys = round(gxcysys, 2)
        gxcysy.append(gxcysys)
        #计算持有收益率
        gxcysyls = gxcysys / (gxccjes - gxcysys)
        gxcysyls = round(gxcysyls, 2)
        gxcysyls = '{:.2%}'.format(gxcysyls)
        gxcysyl.append(gxcysyls)

    print("更新的持仓金额：%s" % gxccje)
    #text.insert(END, "这是更新后今天的持仓数额：%s \n" % gxccje)
    print("更新的今日收益：%s" % gxjrsy)
    #text.insert(END, "这是更新后今天收益：%s \n" % gxjrsy)
    print("更新的持有收益：%s" % gxcysy)
    #text.insert(END, "这是更新后今天的持有收益：%s \n" % gxcysy)
    print("更新的持有收益率：%s" % gxcysyl)

    wb1 = xlrd.open_workbook('shouyi.xls')
    nwb = copy(wb1)
    nwb_sheet = nwb.get_sheet(0)
    # nwb_sheet.write_merge(1, 2, 0, 0, '序号')
    x = x + 1
    #按序将更新的数据插入列表
    for i in range(y):
        #合并基金代码单元格
        nwb_sheet.write_merge(1, 1, (chushi2),(chushi2 + 5),fundcode[i])
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

    #计算总持仓
    jrzcc = 0
    for i in range(len(gxccje)):
        jrcc = gxccje[i]
        jrcc = float(jrcc)
        print(jrcc)
        jrzcc = jrzcc + jrcc

    nwb_sheet.write(x, 1, jrzcc)

    #计算今日总收益
    jrzsy = 0
    for i in range(len(gxjrsy)):
        jrsy = gxjrsy[i]
        jrsy = float(jrsy)
        print(jrsy)
        jrzsy = jrzsy + jrsy

    jrzsyl = jrzsy / (jrzcc - jrzsy)
    jrzsyl = round(jrzsyl, 2)
    jrzsyl = '{:.2%}'.format(jrzsyl)

    nwb_sheet.write(x, 5, jrzsyl)
    nwb_sheet.write(x, 4, jrzsy)

    #计算今日持有总收益
    jrcyzsy = 0
    for i in range(len(gxcysy)):
        jrcysy = gxcysy[i]
        jrcysy = float(jrcysy)
        print(jrcysy)
        jrcyzsy = jrcyzsy + jrcysy
    jrcyzsyl = jrcyzsy / (jrzcc - jrcyzsy)
    jrcyzsyl = round(jrcyzsyl, 2)
    jrcyzsyl = '{:.2%}'.format(jrcyzsyl)

    nwb_sheet.write(x, 2, jrcyzsy)
    nwb_sheet.write(x, 3, jrcyzsyl)
    nwb_sheet.write(x, 0, nowdate)

    print("自动计算结束")
    #text.insert(END, "完成数据的自动计算！开始进行数据插入！\n \n" )

    nwb.save('shouyi.xls')
    #text.insert(END, "数据插入成功！\n 请打开shouyi.xls文件查看更新后的结果。")

    return gxjrsy,gxccje,gxcysy,gxcysyl,jrzcc,jrzsy,jrcyzsy,jrcyzsyl