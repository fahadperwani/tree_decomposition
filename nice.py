from PyQt5 import QtCore, QtGui, QtWidgets
import time
from dec1 import nice_tree


class Ui_Nice(object):
    def __init__(self):
        pass
    def __init__(self, data):
        self.data = data

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 831, 530))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)  # important lines
        self.graphicsView.setScene(self.scene)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(690, 560, 83, 25))
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.graph_show)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(790, 560, 83, 25))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(lambda: MainWindow.close())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def close_window(self, MainWindow):
        MainWindow.close()

    def graph_show(self):
        from Graph_draw import Draw_Graph
        from PyQt5.QtGui import QPixmap
        from dec1 import decomposition
        from validation import TreeDecomposition

        _translate = QtCore.QCoreApplication.translate

        # start = time.time()
        # width, edges = decomposition(self.data)
        edges = nice_tree(self.data)
        Draw_Graph(edges, 'nice')
        end = time.time()
        pixmap = QPixmap("nice.gy.png")
        self.scene.addPixmap(pixmap)
        # v = TreeDecomposition(self.data, edges)
        # print(v.is_valid())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh.setText(_translate("MainWindow", "Show"))
        self.exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Nice()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
