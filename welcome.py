from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from window01 import Ui_Window01


class Ui_MainWindow(object):

    # def __init__(self):
    #     self.pushButton = None
    #     self.textEdit = None
    #     self.label = None
    #     self.centralwidget = None
    #     self.ui = None
    #     self.window = None

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window01()
        edges = self.get_edges()
        if edges is not None:
            self.ui.edges = edges
            self.ui.setupUi(self.window)
            self.window.show()

    def get_edges(self):
        edges_text = self.textEdit.toPlainText()
        try:
            edges = int(edges_text)
        except ValueError:
            QMessageBox.critical(None, "Invalid input", "Please enter a valid integer")
            return None
        return edges

    # def openWindow(self):
    #     self.window  = QtWidgets.QMainWindow()
    #     self.ui = Ui_Window01()
    #     self.get_edges()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    # def get_edges(self):
    #     edges = self.textEdit.toPlainText()
    #     edges = int(edges)
    #     # sending variables to the next Window
    #     self.ui.edges = edges


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 281, 71))
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
        self.label.setText(_translate("MainWindow", "How many Edges has the Graph : "))
        self.pushButton.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
