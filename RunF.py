import sys
import threading
import time

import keyboard
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QWidget, \
    QLabel, QVBoxLayout, QApplication, QSystemTrayIcon, QAction, QMenu, QLineEdit, QPushButton, QHBoxLayout

import RunAA
import favor10
import strengthen
import ys_fx
from favor10 import Favor


class WinF(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('RunF2.4')
        self.setWindowIcon(QIcon('./HTicon.ico'))
        # 隐藏整个菜单栏
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 显示关闭按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.initUI()
        self.tp_ui()

    def initUI(self):
        # 画label
        label1 = QLabel('f启动：按 alt+f')
        label2 = QLabel('f暂停：长按 v')
        label3 = QLabel('w启动：按 ctrl+w')
        label4 = QLabel('w暂停：长按 空格')
        label5 = QLabel('space启动：按 alt+空格')
        label6 = QLabel('space暂停：长按 z')
        label7 = QLabel('全部暂停：长按 t')
        label8 = QLabel('强化次数：')
        label9 = QLabel('长按t停止 ')
        label10 = QLabel('10次好感：')

        # 输入框 整数校验器 限制输入1-100之间的整数
        self.qh_LineEdit = QLineEdit('1')
        self.qh_LineEdit.setMaximumSize(100, 100)
        reg_00 = QRegExp('^([1-9][0-9]{0,1}|100)$')
        int_re_validator = QRegExpValidator()
        int_re_validator.setRegExp(reg_00)
        self.qh_LineEdit.setValidator(int_re_validator)
        # self.qh_LineEdit.textChanged.connect(self.editChanged)
        qh_button = QPushButton('开始强化')
        qh_button.clicked.connect(self.qhRelics)

        hg10_button = QPushButton('开始任务')

        # 强化和10好感的布局
        h1box = QHBoxLayout()
        h1box.addWidget(label8)
        h1box.addWidget(self.qh_LineEdit)
        h1box.addStretch(1)
        h2box = QHBoxLayout()
        h2box.addWidget(label9)
        h2box.addWidget(qh_button)
        h2box.addStretch(1)
        h3box = QHBoxLayout()
        h3box.addWidget(label10)
        h3box.addWidget(hg10_button)
        h3box.addStretch(1)

        hg10_button.clicked.connect(self.favor_run10)

        # 画分割线
        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.HLine)
        line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        line2 = QtWidgets.QFrame()
        line2.setFrameShape(QtWidgets.QFrame.HLine)
        line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        line3 = QtWidgets.QFrame()
        line3.setFrameShape(QtWidgets.QFrame.HLine)
        line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        line4 = QtWidgets.QFrame()
        line4.setFrameShape(QtWidgets.QFrame.HLine)
        line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        line5 = QtWidgets.QFrame()
        line5.setFrameShape(QtWidgets.QFrame.HLine)
        line5.setFrameShadow(QtWidgets.QFrame.Sunken)


        # 线和label放入布局 加入框架
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(line1)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(line2)
        vbox.addWidget(label5)
        vbox.addWidget(label6)
        vbox.addWidget(line3)
        vbox.addWidget(label7)
        vbox.addWidget(line4)
        vbox.addLayout(h1box)
        vbox.addLayout(h2box)
        vbox.addWidget(line5)
        vbox.addLayout(h3box)

        self.setLayout(vbox)

    def edit_value(self):
        """获取文本框改变后的值"""
        global qh_num
        # 如qh_LineEdit.text()里面为空值 则 qh_num赋值为1
        try:
            qh_num = int(self.qh_LineEdit.text())
        except:
            qh_num = 1

    def qhRelics(self):
        """强化圣遗物执行函数"""
        self.edit_value()
        qhzb = strengthen.QH()
        qhzb.get_real_resolution()

        i = 1
        while True:
            qhzb.qh()
            # print(qh_num)
            # time.sleep(1)
            i = i + 1
            if i > qh_num:
                break
            if keyboard.is_pressed('t'):
                break

    def favor_run10(self):
        main.close()
        time.sleep(1)
        favor = Favor()
        i = 1
          # 用来统计找到好感图片的次数
        # count2 = 0  # 用来统计未找到好感图片的次数 留着以后可能扩展日志用
        while True:
            if ys_fx.find_p(ys_fx.p_swz, n=180):  # p_swz 守望者任务图片
                favor.hg10()
                # print("count1 = %d " % favor10.count1)
                i += 1

            if i > 20:
                break

            if favor10.count1 > 10:
                break

            if keyboard.is_pressed('t'):
                break

            # else:
            #     # print("超时没有找到任务，重进游戏")
            #     ys_fx.cjyx()


    def tp_ui(self):
        # 在系统托盘处显示图标
        tp = QSystemTrayIcon(self)
        tp.setIcon(QIcon('./HTicon.ico'))

        # 退出
        def quitApp():
            QCoreApplication.instance().quit()
            tp.setVisible(False)

        self.a1 = QAction('&主界面', triggered = self.show)
        self.a2 = QAction('&退出', triggered = quitApp)

        tpMenu = QMenu()
        tpMenu.addAction(self.a1)
        tpMenu.addAction(self.a2)
        tp.setContextMenu(tpMenu)
        # 不调用show不会显示系统托盘
        tp.show()

        def act(reason):
            # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
            if reason == 2 or reason == 3:
                tpMenu.show()
                self.show()

        tp.activated.connect(act)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)
    go_a = RunAA.RunA()
    main = WinF()
    main.show()

    # 每个自动按键都独立线程，互不影响
    th_WW = threading.Thread(target=go_a.th_w, daemon=True)
    th_WW.start()

    th_FF = threading.Thread(target=go_a.th_f, daemon=True)
    th_FF.start()

    th_SS = threading.Thread(target=go_a.th_space, daemon=True)
    th_SS.start()

    sys.exit(app.exec_())

# pyinstaller -Fw -i HTicon.ico RunF.py

# pyi-makespec -w -i HTicon.ico -D RunF.py
# datas=[('youyongpc','youyongpc')],
# pyinstaller RunF.spec

