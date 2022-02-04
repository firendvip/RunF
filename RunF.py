import sys
import threading
from PyQt5 import QtWidgets

import RunAA
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, \
    QLabel, QVBoxLayout, QApplication


class WinF(QWidget):
    def __init__(self):
        super().__init__()
        # 固定窗口大小
        self.setFixedSize(420, 520)
        self.setWindowTitle('RunF')
        self.setWindowIcon(QIcon('./HTicon.ico'))

        # 窗口在最前端
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):

        label1 = QLabel('f启动：按 alt+f')
        label2 = QLabel('f暂停：长按 v')
        label1.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")
        label2.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")

        label3 = QLabel('w启动：按 alt+w')
        label4 = QLabel('w暂停：长按 空格')
        label3.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")
        label4.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")

        label5 = QLabel('space启动：按 alt+空格')
        label6 = QLabel('space暂停：长按 z')
        label5.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")
        label6.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")

        label7 = QLabel('全部暂停：长按 t')
        label7.setStyleSheet("QLabel{font-size:30px;font-weight:normal}")

        self.line1 = QtWidgets.QFrame()
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line2 = QtWidgets.QFrame()
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line3 = QtWidgets.QFrame()
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(self.line1)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(self.line2)
        vbox.addWidget(label5)
        vbox.addWidget(label6)
        vbox.addWidget(self.line3)
        vbox.addWidget(label7)
        self.setLayout(vbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./HTicon.ico'))

    go_a = RunAA.RunA()

    main = WinF()
    main.show()

    th_WW = threading.Thread(target=go_a.th_w, daemon=True)
    th_WW.start()

    th_FF = threading.Thread(target=go_a.th_f, daemon=True)
    th_FF.start()

    th_SS = threading.Thread(target=go_a.th_space, daemon=True)
    th_SS.start()

    sys.exit(app.exec_())

# pyinstaller -Fw -i HTicon.ico RunF.py
