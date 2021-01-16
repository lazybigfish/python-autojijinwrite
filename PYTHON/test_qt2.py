import sys

import login as login
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QPushButton, QLCDNumber, QTableWidget, \
    QTableWidgetItem, QLabel, QWidget, QHeaderView, QMessageBox, QInputDialog,QLineEdit
from PyQt5.QtCore import QCoreApplication,QTimer,QDateTime
from PyQt5.QtGui import QIcon
import numpy as np

import renovatedata
import getfundcode
import insternewcode
import time


class mywindos(QWidget):

    #初始化实例对象
    def __init__(self):
        #重载mywindos
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start()

        fundCode, d, y, fundcode = getfundcode.getfundCode()
        print(fundcode)

        self.fundcode = fundcode

        self.diyilie = len(fundcode)

        self.huizong = []

        self.initUI()

    def reInfo(self):
        gxjrsy, gxccje, gxcysy, gxcysyl, jrzcc, jrzsy, jrcyzsy, jrcyzsyl, fundcode = renovatedata.start()

        self.huizong.append('汇总')
        self.huizong.append(jrzcc)
        self.huizong.append(jrcyzsy)
        self.huizong.append(jrzsy)
        self.huizong.append(jrcyzsyl)
        print('wozaiyunx')

        self.insterInfo(fundcode, 0, self.huizong, self.diyilie)
        self.insterInfo(gxccje, 1, self.huizong, self.diyilie)
        self.insterInfo(gxcysy, 2, self.huizong, self.diyilie)
        self.insterInfo(gxjrsy, 3, self.huizong, self.diyilie)
        self.insterInfo(gxcysyl, 4, self.huizong, self.diyilie)

    # def gettime(self):
    #     timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    #     self.label2.setText(timestr)
    #     mywindos.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间

    def showTime(self):
        time = QDateTime.currentDateTime()

        timeDisplay = time.toString(" yyyy-MM-dd\n  hh:mm:ss \n   dddd")
        self.label2.setText(timeDisplay)

    def insterInfo(self,x,y,z,q):

        if y == []:
            self.cuowujinggao()
            print('zhehisguo')
            return

        for i in range(len(x)):
            table_clo_vlue = x[i]
            table_clo_vlue = str(table_clo_vlue)
            newitem = QTableWidgetItem(table_clo_vlue)
            self.table.setItem(i,y,newitem)

        if z != []:
            huizong = z[y]
            huizong = str(huizong)
            huizong = QTableWidgetItem(huizong)
            print('zhehsibuguo!! ')
            self.table.setItem(q,y,huizong)

    def closewin(self):
        self.close()


    def setcolum(self):
        print("开始更新表格样式")
        self.tablerows = len(self.fundcode) + 1
        print("获取到行数")
        self.table.setRowCount(self.tablerows)
        self.table.setColumnCount(5)
        self.insterInfo(self.fundcode, 0, self.huizong, self.diyilie)

    def cuowujinggao(self):
        QMessageBox.warning(self, "警告", "没有设置基金！请添加基金后在尝试刷新！",QMessageBox.Cancel)

    def initUI(self):

        #添加状态通知栏目信息
        # self.statusBar().showMessage('准备就绪...')
        self.setGeometry(100,100,1000,700)
        self.setWindowTitle('小林基金计算统计工具V1.1.2')

        self.lb1 = QLabel('基金收益情况一览表',self)
        self.lb1.setGeometry(150,20,380,30)
        self.lb1.setStyleSheet("color:red;font:33px")

        self.qbtn3 = QPushButton('关于作者\n和软件',self)
        self.qbtn3.setGeometry(770,60,150,130)
        self.qbtn3.setStatusTip('关于作者')

        self.label1 = QLabel("现在的时间是：",self)
        self.label1.setGeometry(780,170,200,100)

        self.label2 = QLabel("",self)
        self.label2.setGeometry(740,240,200,120)
        self.label2.setStyleSheet("QLabel{background:yellow;color:red;font-size:31px;font-weight:bold;font-family:宋体;}")


        self.qbtn = QPushButton('添加基金',self)
        self.qbtn.setGeometry(770,380,150,50)
        self.qbtn.setStatusTip('添加基金')

        self.qbtn1 = QPushButton('更新数据',self)
        self.qbtn1.setGeometry(770,480,150,50)
        self.qbtn1.setStatusTip('更新数据')

        qbtn2 = QPushButton('退出',self)
        qbtn2.clicked.connect(QCoreApplication.instance().quit)
        qbtn2.setGeometry(770,580,150,50)
        qbtn2.setStatusTip('退出')

        self.table = QTableWidget(self)
        self.table.setGeometry(3,60,700,600)
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.setStyleSheet("selection-background-color:pink")
        self.table.raise_()

        self.setcolum()

        self.table.setHorizontalHeaderLabels(['基金名称','持有金额','持有收益','今日收益','收益率'])
        self.table.horizontalHeader().setStyleSheet( "QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.table.setColumnWidth(0,270)

        self.show()



class jijinzhuyemian(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.newinfo = []

    def closewin(self):
        self.close()

    def initUI(self):
        # 添加状态通知栏目信息
        # self.statusBar().showMessage('准备就绪...')
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('小林基金计算统计工具V1.1.2')

        self.label1 = QLabel("新增的基金名称：",self)
        self.label1.setGeometry(100,100,200,100)
        self.label2 = QLabel("",self)
        self.label2.setGeometry(280, 100, 300, 100)

        self.label3 = QLabel("新增的基金代码：",self)
        self.label3.setGeometry(550,100,170,100)
        self.label4 = QLabel("",self)
        self.label4.setGeometry(690, 100, 100, 100)

        self.label5 = QLabel("新增的基金持仓金额：",self)
        self.label5.setGeometry(100,200,200,100)
        self.label6 = QLabel("",self)
        self.label6.setGeometry(300,200,200,100)

        self.label7 = QLabel("新增的基金持仓收益：",self)
        self.label7.setGeometry(550,200,200,100)
        self.label8 = QLabel("",self)
        self.label8.setGeometry(720,200,200,100)

        self.label9 = QLabel("新增的基金持有份额：",self)
        self.label9.setGeometry(100,300,300,100)
        self.label10 = QLabel("",self)
        self.label10.setGeometry(300,300,200,100)

        self.btn = QPushButton("点击添加基金信息", self)
        self.btn.setGeometry(100,400,240,40)
        self.btn.clicked.connect(self.getText)

        self.btn1 = QPushButton("保存并返回", self)
        self.btn1.setGeometry(400,400,240,40)
        self.btn1.clicked.connect(self.insternewcode)
        self.btn1.clicked.connect(self.close)


    def insternewcode(self):
        print("开始插数据")
        insternewcode.insternewcode(self.newinfo)

    def getText(self):
        self.newinfo = []
        textname, okPressed1 = QInputDialog.getText(self, "添加基金参数", "基金名字:", QLineEdit.Normal, "")
        textcode, okPressed1 = QInputDialog.getText(self, "添加基金参数", "基金代码:", QLineEdit.Normal, "")
        text2, okPressed = QInputDialog.getText(self, "添加基金参数", "持仓金额:", QLineEdit.Normal, "")
        text3, okPressed = QInputDialog.getText(self, "添加基金参数", "持有收益:", QLineEdit.Normal, "")
        text4, okPressed = QInputDialog.getText(self, "添加基金参数", "持仓份额:", QLineEdit.Normal, "")
        if okPressed and text2 != '':
            self.newinfo.append(textname)
            self.label2.setText(textname)
            self.newinfo.append(textcode)
            self.label4.setText(textcode)
            self.newinfo.append(text2)
            self.label6.setText(text2)
            self.newinfo.append(text3)
            self.label8.setText(text3)
            self.newinfo.append(text4)
            self.label10.setText(text4)
            print("这是新增的基金信息 :%s" % self.newinfo)


class aboutme(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def closewin(self):
        self.close()

    def initUI(self):
        # 添加状态通知栏目信息
        # self.statusBar().showMessage('准备就绪...')
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('小林基金计算统计工具V1.1.2')

        self.label1 = QLabel("关于作者的一点说明",self)
        self.label1.setGeometry(200,30,620,100)
        self.label1.setStyleSheet("QLabel{color:red;font-size:66px;font-weight:bold;font-family:宋体;}")

        self.aboutme = '本工具为小林同学一行一行敲出来的。\n在此说明，本工具为\n宜春霸主jiam董\n上高首富xwu总\n湘潭资本家chul总\n私人订制。\n请以上人员速速发红包来！'
        self.label2 = QLabel(self.aboutme,self)
        self.label2.setGeometry(100,140,830,400)
        self.label2.setStyleSheet("QLabel{background:yellow;color:red;font-size:44px;font-weight:bold;font-family:宋体;}")

        self.aboutme = '欢迎关注作者哔哩哔哩：\n   小林今天不吃饭'
        self.label3 = QLabel(self.aboutme,self)
        self.label3.setGeometry(330,555,380,80)
        self.label3.setStyleSheet("QLabel{background:yellow;color:red;font-size:33px;font-weight:bold;font-family:宋体;}")

        self.btn1 = QPushButton("返回", self)
        self.btn1.setGeometry(400,650,240,40)
        self.btn1.clicked.connect(self.close)



if __name__ == '__main__':

        #每个QT5程序必须创建一个应用程序对象，
        #sys.argv参数是来自命令行的参数列表。 Python脚本可以从shell运行。 写了这句话就能让我们的程序从命令行启动。
    app = QApplication(sys.argv)

    ok = jijinzhuyemian()
    ex = mywindos()
    ab = aboutme()

    ex.show()

    ex.qbtn.clicked.connect(ok.show)
    ex.qbtn.clicked.connect(ex.close)
    ex.qbtn1.clicked.connect(ex.reInfo)
    ok.btn1.clicked.connect(ex.setcolum)
    ok.btn1.clicked.connect(ex.show)
    ex.qbtn3.clicked.connect(ab.show)




    sys.exit(app.exec_())