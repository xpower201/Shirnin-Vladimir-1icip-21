import sys
import test_window
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel

class Main(test_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.pushButton_red.clicked.connect(self.pushButton_red_click)
        self.pushButton_text.clicked.connect(self.text_click)
        
    def text_click(self):
        self.label_text.setText("124")  
             
    def pushButton_red_click(self):
        self.label_red.setStyleSheet("color: red;")
        
        
                
# app = QApplication(sys.argv)
# window = Main()
# window.show()
# app.exec()