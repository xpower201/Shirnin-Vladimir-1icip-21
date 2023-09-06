from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Main")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_red = QtWidgets.QLabel(self.centralwidget)
        self.label_red.setGeometry(QtCore.QRect(180, 50, 81, 41))
        self.label_red.setObjectName("label_red:")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(180, 90, 71, 31))
        self.label_text.setObjectName("label_text")
        self.pushButton_red = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_red.setGeometry(QtCore.QRect(40, 60, 93, 28))
        self.pushButton_red.setObjectName("pushButton_red")
        self.pushButton_text = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_text.setGeometry(QtCore.QRect(30, 100, 111, 28))
        self.pushButton_text.setObjectName("pushButton_text")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(40, 140, 93, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setGeometry(QtCore.QRect(40, 180, 93, 28))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_db = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_db.setGeometry(QtCore.QRect(40, 220, 93, 28))
        self.pushButton_db.setObjectName("pushButton_db")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(10, 500, 93, 28))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(410, 40, 361, 461))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_red.setText(_translate("MainWindow", "TextLabel"))
        self.label_text.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_red.setText(_translate("MainWindow", "красный"))
        self.pushButton_text.setText(_translate("MainWindow", "поменять текст"))
        self.pushButton_add.setText(_translate("MainWindow", "добавитть бд"))
        self.pushButton_remove.setText(_translate("MainWindow", "удалить бд"))
        self.pushButton_db.setText(_translate("MainWindow", "данные бд"))
        self.pushButton_exit.setText(_translate("MainWindow", "выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
