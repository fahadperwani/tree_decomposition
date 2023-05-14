from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from decomposition import Ui_Decomposition
import graphviz


class Ui_Window01(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Decomposition(self.get_data())
        # self.get_edges()                             # it's important for get num function to be before Show function.
        self.ui.setupUi(self.window)
        self.scene.clear()
        self.window.show()

    def btn_refresh(self):
        self.get_data()
        self.graph_show()  # These efunctions will be created.

    def get_data(self):
        user_input = self.textEdit.toPlainText()
        user_input = user_input.replace(" ", "")
        edge_list = user_input.split(";")
        return edge_list

    def graph_show(self):
        from Graph_draw import Draw_Graph
        from PyQt5.QtGui import QPixmap

        edges = self.get_data()
        print("edges", edges)

        try:
            Draw_Graph(edges)
        except:
            print("Invalid String")
        pixmap = QPixmap("graph.gy.png")
        self.scene.addPixmap(pixmap)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(530, 40, 421, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)  # important lines
        self.graphicsView.setScene(self.scene)  # important lines
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(730, 520, 80, 27))
        self.refresh.clicked.connect(self.graph_show)  # Refresh Button
        font = QtGui.QFont()
        font.setPointSize(9)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(820, 520, 126, 27))
        self.next.clicked.connect(self.openWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 441, 91))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 77, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.next.setText(_translate("MainWindow", "decomposition"))
        self.label.setText(_translate("MainWindow", "Edges : "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window01()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
