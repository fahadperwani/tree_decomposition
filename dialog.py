from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from coloring import Ui_Coloring


class Ui_Dialog(object):
    def __init__(self, data=None, nice=None, node=None):
        self.data = data
        self.nice = nice
        self.node = node
        print('\n',self.data, '\n')
        print(self.nice)

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Coloring(self.data, self.nice, self.node, self.get_num())
        self.ui.setupUi(self.window)
        self.window.show()

    def get_num(self):
        num = self.textEdit.toPlainText()
        try:
            num = int(num)
        except ValueError:
            QMessageBox.critical(None, "Invalid input", "Please enter a valid integer")
            return None
        return num
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 110, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(299, 130, 55, 30))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 220, 81, 31))
        self.pushButton.clicked.connect(self.openWindow)           # this line to call the next window.
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number of colors : "))
        self.pushButton.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
