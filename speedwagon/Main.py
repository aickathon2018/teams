# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jckekth\Desktop\Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from product import Ui_ProductWindow


        
class Ui_MainWindow(object):  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProductPrediction = QtWidgets.QPushButton(self.centralwidget)
        self.ProductPrediction.setGeometry(QtCore.QRect(100, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProductPrediction.setFont(font)
        self.ProductPrediction.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProductPrediction.setMouseTracking(False)
        self.ProductPrediction.setAutoFillBackground(False)
        self.ProductPrediction.setStyleSheet("QPushButton{\n"
"background-color: rgb(12, 112, 200);\n"
"color: white;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 97, 138);\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.ProductPrediction.setFlat(False)
        self.ProductPrediction.setObjectName("ProductPrediction")
        self.ProductPrediction_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ProductPrediction_2.setGeometry(QtCore.QRect(310, 290, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProductPrediction_2.setFont(font)
        self.ProductPrediction_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProductPrediction_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(12, 112, 200);\n"
"color: white;\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(30, 97, 138);\n"
"}\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.ProductPrediction_2.setFlat(False)
        self.ProductPrediction_2.setObjectName("ProductPrediction_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -20, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-40, -10, 661, 481))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 180, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 370, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 20, 151, 191))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 230, 191, 151))
        self.label_6.setObjectName("label_6")
        self.label_2.raise_()
        self.ProductPrediction.raise_()
        self.ProductPrediction_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProductPrediction.setText(_translate("MainWindow", "Predict Product"))
        self.ProductPrediction_2.setText(_translate("MainWindow", "Customer :D"))
        self.label.setText(_translate("MainWindow", "Main Menu"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/back/38416658-clean-light-gentle-geometrical-modern-seamless-pattern-colorful-rectangles-simple-background-vector.jpg\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<< Predict the salability of new products"))
        self.label_4.setText(_translate("MainWindow", "Extract and compound the customer using Face API>>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icon1/icon1.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icon1/th.jpg\"/></p></body></html>"))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
