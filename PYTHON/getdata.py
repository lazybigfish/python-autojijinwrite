from tkinter import *
import tkinter.messagebox
import time
import datetime

import insterdata
import autoCalculation
import getinfook
import getfundcode

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
    #调用函数获取基金代码，初始行数，代码个数
    fundCode,x,y = getfundcode.getfundCode(qishilieshu)
    #调用函数获取基金最新净值
    infolist = getinfook.getInfo(fundCode)

    print("有几行：%s" % x)
    print("这个是基金代码获取的输出：%s " % fundCode)
    text.insert(END, "这个是基金代码获取的输出：%s \n" % fundCode)
    print("需要叠加的个数：%s" % y)
    print("基金净值的情况：%s" % infolist)
    text.insert(END, "这是今天基金净值的情况：%s \n" % infolist)
    #调用函数插入净值数据
    insterdata.insterData(infolist,x,y,qishilieshu)
    text.insert(END, "净值数据写入成功！\n")
    #调用函数计算其余数据并插入表格
    autoCalculation.autoCalculation(infolist,y,x,fundCode,qishilieshu,nowdate)
    text.insert(END, "计算结果写入成功！\n")
    tanc()

btn3 = Button(root,text='开始运行',command=main)
btn3.place(relx= 0.77,rely = 0.7)
btn4 = Button(root,text='点击退出',command=root.destroy)
btn4.place(relx= 0.81,rely = 0.8)
btn5 = Button(root,text='关于作者',command=newwind)
btn5.place(relx= 0.86,rely = 0.7)

root.mainloop()