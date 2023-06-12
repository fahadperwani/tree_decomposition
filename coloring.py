from PyQt5 import QtCore, QtGui, QtWidgets
import time
from dec1 import coloring


class Ui_Coloring(object):
    def __init__(self, data=None, nice=None):
        self.data = data
        self.nice = nice
        print('\n',self.data, '\n')
        print(self.nice)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 831, 351))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.scene = QtWidgets.QGraphicsScene(self.centralwidget)  # important lines
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.graphicsView.setScene(self.scene)
        self.label.setGeometry(QtCore.QRect(50, 400, 280, 25))
        self.label1.setGeometry(QtCore.QRect(50, 370, 230, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label1.setFont(font)
        self.label.setObjectName("label")
        self.label1.setObjectName("label1")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(690, 400, 83, 25))
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.graph_show)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(790, 400, 83, 25))
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

        start = time.time()
        print('\n',self.data, '\n')
        colors = coloring(self.data, self.nice)
        print('\n edges',self.data, '\n')
        Draw_Graph(self.data, 'graph', colors)
        end = time.time()
        if colors:
            self.label.setText(
                _translate(
                    "MainWindow",
                    "Graph decomposition takes time : " + str(round(end - start, 2)) + "s",
                )
            )
        else:
            self.label.setText(
                _translate(
                    "MainWindow",
                    "Graph can't be colored with three colors",
                )
            )

        pixmap = QPixmap("graph.gy.png")
        self.scene.addPixmap(pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Coloring takes time :"))
        self.label1.setText(_translate("MainWindow", "Tree width of Graph g is :"))
        self.refresh.setText(_translate("MainWindow", "Show"))
        self.exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Coloring()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
