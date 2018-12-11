from PyQt5 import QtCore, QtGui, QtWidgets
from product import Ui_ProductWindow
from Main import Ui_MainWindow
from Login import Ui_LoginWindow
import inputmain
import naivebayes_implementation


class ProductWindow( QtWidgets.QMainWindow, Ui_ProductWindow):
    def __init__(self, parent=None):
        super(ProductWindow, self).__init__(parent)
        self.setupUi(self)
        self.predictB.clicked.connect(self.predict)

    def predict(self):
        Newitem=[[]]
        Newitem[0].append(float(self.price.text()))
        Newitem[0].append(self.type.currentIndex ()+2)
        Newitem[0].append(int(self.quantity.text()))
        Newitem[0].append(int(self.fq.text()))
        Newitem[0].append(int(self.mq.text()))
        naivebayes_implementation.main(Newitem)
        Str = naivebayes_implementation.FS
        
   

        

class MainWindow( QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ProductPrediction.clicked.connect(self.handleProduct)
        self.ProductPrediction_2.clicked.connect(self.handleCustomer)

    def handleProduct(self):
        window = ProductWindow(self)
        self.close()
        window.show()

    def handleCustomer(self):
        inputmain.Customer()
        
        


class LoginWindow( QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.toMain)

    def toMain(self):
        window = MainWindow(self)
        self.close()
        window.show()

        

def main():
    import sys
    qApp = QtWidgets.QApplication(sys.argv)
    aw = LoginWindow()
    aw.show()
    sys.exit(qApp.exec_())

if __name__ == '__main__':
    main()
