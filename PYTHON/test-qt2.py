import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QLCDNumber, QTableWidget, \
    QTableWidgetItem, QLabel
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import numpy as np
import datetime


import insterdata
import autoCalculation
import getinfook
import getfundcode


class mywindos(QMainWindow):

    #初始化实例对象
    def __init__(self,funcode):
        #重载mywindos
        super(mywindos,self).__init__()
        self.fundcode = funcode
        self.initUI(self)


    def initUI(self):

        #添加状态通知栏目信息
        self.statusBar().showMessage('准备就绪...')
        self.setGeometry(100,100,1000,700)
        self.setWindowTitle('小林基金计算统计工具V1.1.2')

        self.lb1 = QLabel('收益情况一览表',self)


        qbtn = QPushButton('添加基金',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setGeometry(770,360,150,50)
        qbtn.setStatusTip('添加基金')

        qbtn1 = QPushButton('更新数据',self)
        qbtn1.clicked.connect(QCoreApplication.instance().quit)
        qbtn1.setGeometry(770,460,150,50)
        qbtn1.setStatusTip('更新数据')

        qbtn2 = QPushButton('导出表格',self)
        qbtn2.clicked.connect(QCoreApplication.instance().quit)
        qbtn2.setGeometry(770,560,150,50)
        qbtn2.setStatusTip('导出表格')



        self.table = QTableWidget(self)
        self.table.setGeometry(3,60,700,600)
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.setStyleSheet("selection-background-color:pink")
        self.table.raise_()

        tablecolums = len(self.fundCode)

        self.table.setColumnCount(tablecolums)
        self.table.setRowCount(4)

        for i in range(self.fundCode):
            table_clo_vlue = self.fundCode[i]
            newitem = QTableWidgetItem(table_clo_vlue)
            self.table.setItem(i,0,newitem)



        self.show()

def start():
    # fundCode = input("基金代码：")
    # 基金代码全局设置
    qishilieshu = 6
    # 调用函数获取基金代码，初始行数，代码个数
    fundCode, x, y = getfundcode.getfundCode(qishilieshu)
    # 调用函数获取基金最新净值
    infolist = getinfook.getInfo(fundCode)

    print("有几行：%s" % x)
    print("这个是基金代码获取的输出：%s " % fundCode)
    print("需要叠加的个数：%s" % y)
    print("基金净值的情况：%s" % infolist)
    # 调用函数插入净值数据
    insterdata.insterData(infolist, x, y, qishilieshu)
    # 调用函数计算其余数据并插入表格
    gxjrsy, gxccje, gxcysy, gxcysyl, jrzcc, jrzsy, jrzsyl = autoCalculation.autoCalculation(infolist, y, x, fundCode,
                                                                                                qishilieshu)

    return gxjrsy, gxccje, gxcysy, gxcysyl, jrzcc, jrzsy, jrzsyl,fundCode

if __name__ == '__main__':

        #每个QT5程序必须创建一个应用程序对象，
        #sys.argv参数是来自命令行的参数列表。 Python脚本可以从shell运行。 写了这句话就能让我们的程序从命令行启动。
    app = QApplication(sys.argv)
    gxjrsy, gxccje, gxcysy, gxcysyl, jrzcc, jrzsy, jrzsyl ,fundcode= start()
    ex = mywindos()


sys.exit(app.exec_())