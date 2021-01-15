import re
from tkinter import *
import tkinter.messagebox
import urllib.request
import json
import xlrd
import xlwt
import os
from xlutils.copy import copy
import time
import datetime
import webbrowser

import insterdata
import autoCalculation


def clik(event):
    webbrowser.open("https://space.bilibili.com/4840862?from=search&seid=3440455061236298191")

#作者介绍新窗口
def newwind():
    winNew = Toplevel(root)
    winNew.geometry('320x240')
    winNew.title('关于作者')
    info = '欢迎使用小林基金计算统计工具！\n 如有更好意见，请邮件：nbnqdcd@yeah.net！\n 欢迎关注哔哩哔哩：\n'
    lb2 = Label(winNew,text=info)
    lb2.place(relx=0.1,rely=0.2)


    lb7 = Label(winNew,text='小林今天不吃饭')

    lb7.place(relx=0.34,rely=0.43)


    btClose = Button(winNew,text='关闭',command=winNew.destroy)
    btClose.place(relx=0.44,rely=0.55)

#时间更新
def gettime():
    timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb5.configure(text=timestr)  # 重新设置标签文本
    root.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间

#弹窗提醒
def tanc():
    answer = tkinter.messagebox.askokcancel('运算完成！','数据插入成功！\n 请打开shouyi.xls文件查看更新后的结果。')



root = Tk()
root.title('小林智能基金计算工具V1.0.1')
root.geometry('760x360')

# mainmenu = Menu(root)
# menuFile = Menu(mainmenu)
# mainmenu.add_cascade(label='菜单',menu = menuFile)
# menuFile.add_command(label='关于作者',command=newwind)
# menuFile.add_separator()
# menuFile.add_command(label='退出',command = root.destroy)



lb4 = Label(root, text='建议运行更新时间\n 为早上九点半！ \n',fg='blue',font=('黑体',13))
lb4.place(relx=0.76, rely=0.1)

lb3 = Label(root, text='现在的时间是：\n',fg='red',font=('黑体',18))
lb3.place(relx=0.76, rely=0.24)

lb5 = Label(root,text ='',fg='red',font=('黑体',26))
lb5.pack()
lb5.place(relx=0.77,rely= 0.4)
gettime()


#信息输出框
text = Text(root)
text.place(rely=0,relheight=1)
text.insert(END, "欢迎使用小林基金智能计算工具！\n")
s = str(datetime.datetime.now())+'\n'
text.insert(END, "现在的时间是：%s 请点击开始运行自动计算！\n" % s )
text.insert(END, "\n \n")


fundCode = []

nowdate = datetime.datetime.now().strftime('%y-%m-%d')

def main():
    # fundCode = input("基金代码：")
    #基金代码全局设置
    global fundCode
    global nowdate
    qishilieshu = 6
    fundCode,x,y = getfundCode(qishilieshu)

    infolist = getInfo(fundCode)

    print("有几行：%s" % x)

    print("这个是基金代码获取的输出：%s " % fundCode)
    text.insert(END, "这个是基金代码获取的输出：%s \n" % fundCode)
    print("需要叠加的个数：%s" % y)
    print("基金净值的情况：%s" % infolist)
    text.insert(END, "这是今天基金净值的情况：%s \n" % infolist)

    insterdata.insterData(infolist,x,y,qishilieshu)
    text.insert(END, "净值数据写入成功！\n")

    # autoCalculation(infolist,y,x,fundCode)
    autoCalculation.autoCalculation(infolist,y,x,fundCode,qishilieshu,nowdate)
    text.insert(END, "计算结果写入成功！\n")
    tanc()



#拼接报文地址
def getBaseUrl(fundCode):
    base = "http://fundgz.1234567.com.cn/js/"
    base = base + fundCode
    base = base +".js?rt=1463558676006"
    return base

#获取报文
def getHtml(url):
    header = {
        "User-Agent": "",
        "Referer": "",
        "Cookie":""
    }
    data = ""
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    return data

#解析数据
def Json(html):
    html = html.replace('}', '')
    html = html.replace('{', '')
    html = html.replace('(','')
    html = html.replace(')','')
    html = json.loads(html)
    return html

#获取基金代码
def getfundCode(qishilieshu):
    global fundCode
    global y
    #读取表中的数据
    rbook = xlrd.open_workbook('shouyi.xls')
    rbook.sheets()
    #读取第一页的表
    rsheet = rbook.sheet_by_index(0)

    #获取第三行的数据，基金代码
    colnames = rsheet.row_values(2)
    c = rsheet.col_values(qishilieshu)
    c = [i for i in c if i != '']
    d = len(c) + 1
    #筛选出代码正确值
    fundCode = [i for i in colnames if i != '']
    y = len(fundCode)

    return fundCode,d,y

#获取基金净值
def getInfo(fundCode):
    #空列表准备置放净值集合
    infolist = []
    #空列表准备置放净值详细集合
    dataList = []
    #开始遍历基金代码，获取对应的净值，并插入datalist
    for i in fundCode:
        fundCode = i
        #拼接地址
        baseURL = getBaseUrl(fundCode)
        #获取数据开始解析
        data = getHtml(baseURL)
        #去除多余数据
        data = data.split(('"'))
        dataList.append(data[7])
        dataList.append(data[14])
        dataList.append(data[15])
        infolist.append(data[15])
        #print(data)
        # print(''.join(dataList))
    # print("需要叠加的个数：%s" % y)
    # print("基金净值的详细情况：%s" % dataList)
    # print("基金净值的情况：%s" % infolist)

    return infolist

#写入基金净值
# def insterData(infolist,x,y):
#
#     wb = xlrd.open_workbook('shouyi.xls')
#
#     nwb =copy(wb)
#     print("复制表格")
#     nwb_sheet = nwb.get_sheet(0)
#     for i in range(y):
#         nwb_sheet.write(x,y,infolist[i])
#         y = y + 6
#
#     print("数据写入成功")
#     text.insert(END, "净值数据写入成功！\n" )
#     nwb.save('shouyi.xls')

# #自动计算全部结果并写入Excel
# def autoCalculation(infolist,y,x,fundcode):
#     # 准备读取列表存放读取数据
#     dqccje = []
#     dqcysy = []
#     dqjrsy = []
#     dqcysyl = []
#     dqccse = []
#
#     # 准备更新列表存放计算后的数据
#     gxccje = []
#     gxcysy = []
#     gxjrsy = []
#     gxcysyl = []
#
#     # 初始列数定位置用于定位存放位置和读取位置
#     chushi = qishilieshu
#     chushi2 = qishilieshu
#     # 初始行数定位
#     x = x - 1
#
#     global nowdate
#
#     wb = xlrd.open_workbook('shouyi.xls')
#     wb.sheets()
#
#     wb_sheet = wb.sheet_by_index(0)
#     #读取昨日数据
#     colnames = wb_sheet.row_values(x)
#
#     # 将原表的数据读取出来供计算
#     for i in range(len(infolist)):
#         dqccje.append(colnames[chushi])
#         chushi = chushi + 1
#         dqcysy.append(colnames[chushi])
#         chushi = chushi + 1
#         dqjrsy.append(colnames[chushi])
#         chushi = chushi + 3
#         dqccse.append(colnames[chushi])
#         chushi = chushi + 1
#
#     print("读取的持仓金额：%s" % dqccje)
#     text.insert(END, "这是读取到的昨日持仓金额：%s \n" % dqccje)
#     print("读取的持有收益：%s" % dqcysy)
#     text.insert(END, "这是读取到的昨日持有收益：%s \n" % dqcysy)
#     print("读取的持仓数额：%s" % dqccse)
#     text.insert(END, "这是读取到的昨日持仓数额：%s \n" % dqccse)
#
#     for i in range(len(infolist)):
#         # 获取值转换为浮点数进行计算
#         # 获取昨日持仓数额
#         q = float(dqccse[i])
#         # 读取今日获取净值
#         s = float(infolist[i])
#         # 读取昨日持仓金额
#         w = float(dqccje[i])
#         # 读取昨日持有收益
#         e = float(dqcysy[i])
#
#         gxccjes = q * s
#         # 控制结果精度为浮点两位数
#         gxccjes = round(gxccjes, 2)
#         # 将结果添加进入更新的列表
#         gxccje.append(gxccjes)
#         # 计算今日收益
#         gxjrsys = gxccjes - w
#         gxjrsys = round(gxjrsys, 2)
#         gxjrsy.append(gxjrsys)
#
#         # 计算持有收益
#         gxcysys = gxjrsys + e
#         gxcysys = round(gxcysys, 2)
#         gxcysy.append(gxcysys)
#         #计算持有收益率
#         gxcysyls = gxcysys / (gxccjes - gxcysys)
#         gxcysyls = round(gxcysyls, 2)
#         gxcysyls = '{:.2%}'.format(gxcysyls)
#         gxcysyl.append(gxcysyls)
#
#     print("更新的持仓金额：%s" % gxccje)
#     text.insert(END, "这是更新后今天的持仓数额：%s \n" % gxccje)
#     print("更新的今日收益：%s" % gxjrsy)
#     text.insert(END, "这是更新后今天收益：%s \n" % gxjrsy)
#     print("更新的持有收益：%s" % gxcysy)
#     text.insert(END, "这是更新后今天的持有收益：%s \n" % gxcysy)
#     print("更新的持有收益率：%s" % gxcysyl)
#
#     wb1 = xlrd.open_workbook('shouyi.xls')
#     nwb = copy(wb1)
#     nwb_sheet = nwb.get_sheet(0)
#     nwb_sheet.write_merge(1, 3, 0, 0, '序号')
#     x = x + 1
#     #按序将更新的数据插入列表
#     for i in range(y):
#         #合并基金代码单元格
#         nwb_sheet.write_merge(2, 2, chushi2,(chushi2 + 5),fundcode[i])
#         nwb_sheet.write(x, chushi2, gxccje[i])
#         chushi2 = chushi2 + 1
#         nwb_sheet.write(x, chushi2, gxcysy[i])
#         chushi2 = chushi2 + 1
#         nwb_sheet.write(x, chushi2, gxjrsy[i])
#         chushi2 = chushi2 + 2
#         nwb_sheet.write(x, chushi2, gxcysyl[i])
#         chushi2 = chushi2 + 1
#         nwb_sheet.write(x, chushi2, dqccse[i])
#         chushi2 = chushi2 + 1
#
#     #计算总持仓
#     jrzcc = 0
#     for i in range(len(gxccje)):
#         jrcc = gxccje[i]
#         jrcc = float(jrcc)
#         print(jrcc)
#         jrzcc = jrzcc + jrcc
#
#     nwb_sheet.write(x, 1, jrzcc)
#
#     #计算今日总收益
#     jrzsy = 0
#     for i in range(len(gxjrsy)):
#         jrsy = gxjrsy[i]
#         jrsy = float(jrsy)
#         print(jrsy)
#         jrzsy = jrzsy + jrsy
#
#     jrzsyl = jrzsy / (jrzcc - jrzsy)
#     jrzsyl = round(jrzsyl, 2)
#     jrzsyl = '{:.2%}'.format(jrzsyl)
#
#     nwb_sheet.write(x, 5, jrzsyl)
#     nwb_sheet.write(x, 4, jrzsy)
#
#     #计算今日持有总收益
#     jrcyzsy = 0
#     for i in range(len(gxcysy)):
#         jrcysy = gxcysy[i]
#         jrcysy = float(jrcysy)
#         print(jrcysy)
#         jrcyzsy = jrcyzsy + jrcysy
#     jrcyzsyl = jrcyzsy / (jrzcc - jrcyzsy)
#     jrcyzsyl = round(jrcyzsyl, 2)
#     jrcyzsyl = '{:.2%}'.format(jrcyzsyl)
#
#     nwb_sheet.write(x, 2, jrcyzsy)
#     nwb_sheet.write(x, 3, jrcyzsyl)
#     nwb_sheet.write(x, 0, nowdate)
#
#     print("自动计算结束")
#     text.insert(END, "完成数据的自动计算！开始进行数据插入！\n \n" )
#
#     nwb.save('shouyi.xls')
#     text.insert(END, "数据插入成功！\n 请打开shouyi.xls文件查看更新后的结果。")
#     tanc()




# main()

btn3 = Button(root,text='开始运行',command=main)
btn3.place(relx= 0.77,rely = 0.7)
btn4 = Button(root,text='点击退出',command=root.destroy)
btn4.place(relx= 0.81,rely = 0.8)
btn5 = Button(root,text='关于作者',command=newwind)
btn5.place(relx= 0.86,rely = 0.7)

# root.config(menu=mainmenu)
root.mainloop()