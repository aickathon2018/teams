# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jckekth\Desktop\product.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_ProductWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 10, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.price = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(170, 60, 81, 21))
        self.price.setObjectName("price")
        
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(170, 90, 81, 21))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.quantity = QtWidgets.QSpinBox(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(170, 120, 81, 21))
        self.quantity.setObjectName("quantity")
        self.quantity.setMaximum(999)
        self.quantity.setValue(243)
        self.fq = QtWidgets.QSpinBox(self.centralwidget)
        self.fq.setGeometry(QtCore.QRect(170, 150, 81, 21))
        self.fq.setObjectName("fq")
        self.fq.setMaximum(999)
        self.fq.setValue(111)
        self.mq = QtWidgets.QSpinBox(self.centralwidget)
        self.mq.setGeometry(QtCore.QRect(170, 180, 81, 21))
        self.mq.setObjectName("mq")
        self.mq.setMaximum(999)
        self.mq.setValue(132)
        self.predictB = QtWidgets.QPushButton(self.centralwidget)
        self.predictB.setGeometry(QtCore.QRect(70, 230, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.predictB.setFont(font)
        self.predictB.setStyleSheet("QPushButton{\n"
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
        self.predictB.setObjectName("predictB")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(290, 120, 161, 101))
        self.output.setObjectName("output")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(-90, -40, 651, 321))
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.price.raise_()
        self.type.raise_()
        self.quantity.raise_()
        self.fq.raise_()
        self.mq.raise_()
        self.predictB.raise_()
        self.output.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
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
        self.label.setText(_translate("MainWindow", "Price (RM):"))
        self.label_2.setText(_translate("MainWindow", "Quantity:"))
        self.label_3.setText(_translate("MainWindow", "Type:"))
        self.label_4.setText(_translate("MainWindow", "Female Quantity:"))
        self.label_5.setText(_translate("MainWindow", "Male Quantity:"))
        self.label_7.setText(_translate("MainWindow", "<<Product Prediction>>"))
        self.type.setCurrentText(_translate("MainWindow", "Grocery"))
        self.type.setItemText(0, _translate("MainWindow", "Grocery"))
        self.type.setItemText(1, _translate("MainWindow", "Home"))
        self.type.setItemText(2, _translate("MainWindow", "Pet Supplies"))
        self.predictB.setText(_translate("MainWindow", "Product Prediction"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/back/38416658-clean-light-gentle-geometrical-modern-seamless-pattern-colorful-rectangles-simple-background-vector.jpg\"/></p></body></html>"))

import logo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
