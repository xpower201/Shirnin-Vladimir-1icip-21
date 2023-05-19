import sys


from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget, QRadioButton



class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        rb1 = QRadioButton(text="lol")
        rb2 = QRadioButton(text="fuck")
        rb3 = QRadioButton(text="bitch")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        
        rb1_1 = QRadioButton(text="amigo")
        rb2_1 = QRadioButton(text="kurwa")
        rb3_1 = QRadioButton(text="pierdol")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(rb2_1)
        vbox2.addWidget(rb3_1)
 
        
        rb1_2 = QRadioButton(text="chupapi")
        rb2_2 = QRadioButton(text="vitali")
        rb3_2 = QRadioButton(text="Pudge")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(rb1_2)
        vbox3.addWidget(rb2_2)
        vbox3.addWidget(rb3_2)
    
        

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(button_layout)
        
        btnb = QPushButton("back")
        btn = QPushButton("next")
        
        btn.clicked.connect(self.activate_tab_1)
        self.stacklayout.addWidget(widget)
        button_layout.addWidget(btn)
        button_layout.addWidget(btnb)



        # btn.clicked.connect(self.activate_tab_1)
        btnb.clicked.connect(self.activate_tab_2)
        self.stacklayout.addWidget(widget2)
        button_layout.addWidget(btn)
        button_layout.addWidget(btnb)
        

        # btn.clicked.connect(self.activate_tab_1)
        # btnb.clicked.connect(self.activate_tab_2)
        self.stacklayout.addWidget(widget3)
        button_layout.addWidget(btn)
        button_layout.addWidget(btnb)


        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)
        
    

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)

