from PyQt6.QtWidgets import QLabel,QPushButton, QVBoxLayout, QMainWindow,QWidget,QLineEdit,QMessageBox
from test import TestWindow

class Greeting (QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.lbl = QLabel("Привет")
        lbl1 =QLabel("Вы готовы пройти тест?")
        btn_ok =QPushButton("Да")
        btn_no = QPushButton("Нет")
        
        btn_ok.clicked.connect(self.ok)
        btn_no.clicked.connect(self.no)
        
        layout.addWidget(self.lbl)
        layout.addWidget(lbl1)
        layout.addWidget(btn_ok)
        layout.addWidget(btn_no)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        with open("test_app/style.css", "r") as css:
            widget.setStyleSheet(css.read())  
        
    def ok(self):
        self.sw = TestWindow()
        self.sw.show()
    def no(self):
        Greeting.close(self)
        

        

              