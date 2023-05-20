from PyQt6.QtWidgets import QLabel,QPushButton, QVBoxLayout, QMainWindow,QWidget,QLineEdit,QMessageBox
from engine import add_data

class Registration(QMainWindow):
    def __init__(self):
        super().__init__()

        lbl1 = QLabel("Придумайте логин")
        self.line1 = QLineEdit()
        # lbl2 = QLabel("(пример: user)")
        lbl3 = QLabel("Придумайте пароль")
        self.line2 = QLineEdit()
        # lbl4 = QLabel("Подтвердите пароль")
        # self.line3 = QLineEdit()
        btn = QPushButton("Создать")
        
        btn.clicked.connect(self.add)
        
        
        layout = QVBoxLayout()
        layout.addWidget(lbl1)
        layout.addWidget(self.line1)
        layout.addWidget(lbl3)
        layout.addWidget(self.line2)
        # layout.addWidget(lbl4)
        # layout.addWidget(self.line3)
        layout.addWidget(btn)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def add(self):
        login = self.line1.text()
        password = self.line2.text()
        # if self.line2.text() == self.line3.text():
        #     password = self.line2.text()
        # else:
        #     QMessageBox.warning(self, "Ошибка", "Не правильно введён пароль")
        
        add_data(login, password)
        QMessageBox.information(self, "Успех", "Ученик Добавлен")
