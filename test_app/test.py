from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget, QRadioButton

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        rb1 = QRadioButton(text="lol")
        rb2 = QRadioButton(text="LOL")
        rb3 = QRadioButton(text="Leage of Legens")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        
        rb1_1 = QRadioButton(text="amigo")
        rb2_1 = QRadioButton(text="salut")
        rb3_1 = QRadioButton(text="si")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(rb2_1)
        vbox2.addWidget(rb3_1)
 
        
        rb1_2 = QRadioButton(text="chupa-chups")
        rb2_2 = QRadioButton(text="Mac Donalds")
        rb3_2 = QRadioButton(text="Burger King")
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
        btn_itog = QPushButton("result")
        
        btn.clicked.connect(self.activate_tab_1)
        self.stacklayout.addWidget(widget)
        button_layout.addWidget(btn)
        button_layout.addWidget(btnb)
        button_layout.addWidget(btn_itog)
        btn_itog.clicked.connect(self.btn_it)



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
        
    def btn_itog(self):
        pass

