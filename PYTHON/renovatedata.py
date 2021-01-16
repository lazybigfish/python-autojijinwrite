

import datetime
import insterdata
import autoCalculation
import getinfook
import getfundcode


def start():
    # fundCode = input("基金代码：")
    # 基金代码全局设置
    qishilieshu = 6
    # 调用函数获取基金代码，初始行数，代码个数
    fundCode, x, y,jijinname = getfundcode.getfundCode()

    #调用函数获取基金最新净值
    infolist = getinfook.getInfo(fundCode)

    print("有几行：%s" % x)
    print("这个是基金代码获取的输出：%s " % fundCode)
    print("需要叠加的个数：%s" % y)
    print("基金净值的情况：%s" % infolist)
    #调用函数插入净值数据
    insterdata.insterData(infolist, x, y, qishilieshu)
    # 调用函数计算其余数据并插入表格
    gxjrsy,gxccje,gxcysy,gxcysyl,jrzcc,jrzsy,jrcyzsy,jrcyzsyl= autoCalculation.autoCalculation(infolist, y, x, fundCode,
                                                                                                qishilieshu)

    return gxjrsy, gxccje, gxcysy, gxcysyl, jrzcc, jrzsy, jrcyzsy,jrcyzsyl, jijinname