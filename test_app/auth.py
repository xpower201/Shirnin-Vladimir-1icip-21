import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget,QMainWindow
import random
from engine import text, session
from test import TestWindow
from reg import Registration

class CaptchaDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.lbl  =QLabel(str(random.randint(1000,9999)))
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)
        # self.generate_captcha()

        
        self.timer_label = QLabel("Таймер: 0")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lbl)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        with open("test_app/style.css", "r") as css:
            widget.setStyleSheet(css.read())    

    def verify_captcha(self):
        # captcha = self.textbox.text()
        print("Проверка капчи:")


        if  self.lbl.text() == self.textbox.text():
            QMessageBox.information(self, "успех","капча пройдена")
            CaptchaDialog.close(self)
            
        else:
            self.textbox.setDisabled(True)  
            self.timer_counter = 11
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        self.timer_counter = 10
        self.timer.start()

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0:
            self.timer.stop()
            self.textbox.setDisabled(False)
            # self.generate_captcha()
        self.captcha_label = QLabel(self)
        self.captcha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

    def generate_captcha(self):
        captcha1 = str(random.randint(1000, 9999))
        self.label.setText(captcha1)




class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")

        self.label_username = QLabel("Имя пользователя:")
        self.login_edit = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        self.button_login = QPushButton("Войти")
        self.btn_exit = QPushButton("Выход")
        self.btn_reg = QPushButton("Регистрация")
        self.button_login.clicked.connect(self.login)
        self.btn_reg.clicked.connect(self.reg)
        self.btn_exit.clicked.connect(self.exit)

        self.login_attempts = 0

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.button_login)
        layout.addWidget(self.btn_reg)
        layout.addWidget(self.btn_exit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        with open("test_app/style.css", "r") as css:
            widget.setStyleSheet(css.read())  

    def login(self):
        self.sw = TestWindow()

        sql = text("SELECT * FROM public.auth")
        obj = session.execute(sql)
        for row in obj:
            for login in  row:
                self.login = login
            for password in row:
                self.password = password
                if self.login_edit.text() == self.login and self.password_edit.text() == self.password:
                    self.sw.show()
                    w.close()
            else:
                self.sw1 = CaptchaDialog()
                self.sw1.show()

    def reg(self):
        self.sw2 = Registration()
        self.sw2.show()
                    
                    
                    
    def exit(slef):
        w.close()
        
app = QApplication(sys.argv)
w = LoginWindow()
w.show()
sys.exit(app.exec())