import sys
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog
import random
from engine import text, session
from test import TestWindow

class CaptchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)
        self.generate_captcha()

        
        self.timer_label = QLabel("Таймер: 0")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)


        if captcha.lower() == self.label.text(): 
            self.accept()
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
            self.generate_captcha()
        self.captcha_label = QLabel(self)
        self.captcha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

    def generate_captcha(self):
        captcha1 = str(random.randint(1000, 9999))
        self.label.setText(captcha1)




class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")

        self.label_username = QLabel("Имя пользователя:")
        self.login_edit = QLineEdit()
        self.label_password = QLabel("Пароль:")
        self.password_edit = QLineEdit()
        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.login)

        self.captcha_dialog = CaptchaDialog(parent=self)
        self.captcha_dialog.setModal(True)

        self.login_attempts = 0

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.login_edit)
        layout.addWidget(self.label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

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
                exe.close()
            else:
                
                if self.captcha_dialog.exec() == QDialog.DialogCode.Accepted:
                    QMessageBox.information(self, "Успех", "Вход выполнен после капчи")
                
                else:
                    QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
                    self.captcha_dialog.start_timer()
                    self.login_attempts = 0
                    self.generate_captcha()
                

app = QApplication(sys.argv)
exe = LoginWindow()
exe.show()
app.exec()