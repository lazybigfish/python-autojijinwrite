import xlrd
from tkinter import *
from xlutils.copy import copy

def insterData(infolist,x,y,qishiweizhi):

    wb = xlrd.open_workbook('shouyi.xls')
    x = x - 1
    qishiweizhi = qishiweizhi +3
    nwb =copy(wb)
    print("复制表格")
    nwb_sheet = nwb.get_sheet(0)
    for i in range(y):
        nwb_sheet.write(x,qishiweizhi,infolist[i])
        qishiweizhi = qishiweizhi + 6

    print("数据写入成功")
    nwb.save('shouyi.xls')